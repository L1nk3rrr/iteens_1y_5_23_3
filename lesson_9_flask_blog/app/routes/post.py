from flask import Blueprint, render_template, abort
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
