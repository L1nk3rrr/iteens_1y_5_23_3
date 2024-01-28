from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from sqlalchemy import select

from app.database import Session
from app.models import Post


bp = Blueprint("post", __name__)


@bp.route("/<int:post_id>")
def get_post(post_id):
    with Session() as session:
        query = select(Post).where(Post.id == post_id)
        post = session.scalars(query).one()
        if not post:
            abort(404)
    return render_template('post.html', post=post)


@bp.route('/create', methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash("Title is required")
        else:
            with Session() as session:
                new_post = Post(title=title, content=content)
                session.add(new_post)
                session.commit()
            return redirect(url_for('default.index'))
    return render_template('create.html')


@bp.route("/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    with Session() as session:
        post = session.scalars(select(Post).where(Post.id == post_id)).one()

    if not post:
        abort(404)

    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash("Title is required")
        else:
            with Session() as session:
                post.update(
                    {"title": title,
                     "content": content}
                )
                session.commit()
            return redirect(url_for('default.index'))
    return render_template('edit.html', post=post)


@bp.route("/<int:post_id>/delete", methods=["GET", "POST"])
def delete_post(post_id):
    with Session() as session:
        post = session.scalars(select(Post).where(Post.id == post_id)).one()

    if not post:
        abort(404)
    title = post.title
    with Session() as session:
        session.delete(post)
        session.commit()
    flash(f"{title} was successfully deleted")
    return redirect(url_for('default.index'))