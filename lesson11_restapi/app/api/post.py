from datetime import datetime

from flask import jsonify
from sqlalchemy import select, update, delete
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app.models import Post
from app.database import Session


class PostApi(Resource):
    def get(self, id):
        query = select(Post).where(Post.id == id)
        with Session() as session:
            post = session.scalars(query).one_or_none()
        if post:
            post_json = row_to_json(post)
            return post_json
        return "Post not found", 404

    def post(self):
        parser = RequestParser()
        parser.add_argument("created_date")
        parser.add_argument("title")
        parser.add_argument("author")
        parser.add_argument("content")
        params = parser.parse_args()
        new_post = Post(
            created_date=datetime.strptime(params["created_date"], "%y-%m-%d") if params["created_date"] else None,
            title=params["title"] or "",
            author=params["author"] or "",
            content=params["content"] or "",
        )
        with Session() as session:
            session.add(new_post)
            session.commit()
        json_data = jsonify(f"Record was created with id {new_post.id}")
        json_data.status_code = 201
        return json_data
    
    def put(self, id):
        parser = RequestParser()
        parser.add_argument("created_date")
        parser.add_argument("title")
        parser.add_argument("author")
        parser.add_argument("content")
        params = parser.parse_args()
        params_dict = dict(
            created_date=datetime.strptime(params["created_date"], "%a, %d %b %Y %H:%M:%S %Z") if params["created_date"] else None,
            title=params["title"] or "",
            author=params["author"] or "",
            content=params["content"] or "",
        )
        query = select(Post).where(Post.id == id)
        with Session() as session:
            post = session.execute(query).scalar_one_or_none()
            if not post:
                return "Post not found", 404
            
            session.execute(update(Post).where(Post.id == id).values(**params_dict))
            session.commit()
            json_data = jsonify(f"Record was edited with id {post.id}")
            json_data.status_code = 202
            return json_data
        
    def delete(self, id):
        with Session() as session:
            post = session.query(Post).get(id)
            if not post:
                return "Post not found", 404
            session.delete(post)
            session.commit()
        json_data = jsonify(f"Record was deleted with id {id}")
        json_data.status_code = 204
        return json_data
        


def row_to_json(post):
    data = {
        "id": post.id,
        "created_date": post.created_date,
        "title": post.title,
        "author": post.author,
        "content": post.content,
    }
    json_data = jsonify(data)
    json_data.status_code = 200
    return json_data

