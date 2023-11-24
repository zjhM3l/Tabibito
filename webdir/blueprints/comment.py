from datetime import datetime

import flask
import flask_login
from flask import Blueprint, request, jsonify
from flask_login import current_user

from exts import db
from models import Comment, CommentPicture, CommentLike

bp = Blueprint("Comment", __name__, url_prefix="/comment")


@bp.route("/add_comment", methods=["POST"])
def add_comment():
    if current_user.is_authenticated:
        data = request.get_json(silent=True)
        comment = Comment(location_grade=data["location_grade"], staff_grade=data["staff_grade"],
                          cleanliness_grade=data["cleanliness_grade"]
                          , value_for_money_grade=data["value_for_money_grade"], comfort_grade=data["comfort_grade"],
                          facilities_grade=data["facilities_grade"], free_wifi_grade=data["free_wifi_grade"],
                          datetime=datetime.now(), title=data["title"], des=data["des"], user_id=data["user_id"],
                          product_id=data["product_id"])
        db.session.add(comment)
        db.session.commit()
        if data["pics"]:
            for picture in data["pics"]:
                comment_picture = CommentPicture(address=picture["pic_url"], comment_id=comment.id)
                db.session.add(comment_picture)
            db.session.commit()
        return jsonify(code=200, message="add comment success"), 200
    else:
        return jsonify(code=201, message="user need login"), 201


@bp.route("/delete", methods=["POST"])
def delete_comment():
    data = request.get_json(silent=True)
    comment = Comment.query.filter_by(id=data["id"]).first()
    db.session.delete(comment)
    db.session.commit()
    return jsonify(code=200, message="delete comment success")


@bp.route("/get_comment_detail", methods=["POST"])
def get_comment_detail():
    data = request.get_json(silent=True)
    comment = Comment.query.filter_by(id=data["comment_id"]).first()
    if comment:
        return jsonify(code=200, detail=comment.serialize_product_page())
    else:
        return jsonify(code=201, message="Wrong comment id")


@bp.route("/add_like", methods=["POST"])
def add_like():
    # 判断是否已经点赞 （前端）
    data = request.get_json(silent=True)
    if_like = data["if_like"]
    comment = Comment.query.filter_by(id=data["comment_id"]).first()
    if if_like:
        new_like = CommentLike(comment_id=comment.id, user_id=data["user_id"])
        db.session.add(new_like)
        comment.like_num += 1
        db.session.commit()
        return jsonify(code=200, message="add like success")
    else:
        the_like = CommentLike.query.filter_by(comment_id=comment.id, user_id=data["user_id"]).first()
        db.session.delete(the_like)
        comment.like_num -= 1
    db.session.commit()
    return jsonify(code=200, message="delete like success")


@bp.route("/get_product_comment", methods=["GET"])
def get_product_comment():
    data = request.get_json(silent=True)
    product_id = data["product_id"]
    comments = Comment.query.filter_by(product_id=product_id).all()
    return jsonify(code=200, data=[comment.serialize_product_page() for comment in comments])


@bp.route("/get_page", methods=['GET', 'POST'])
def get_page_comments():
    data = request.get_json(silent=True)
    page = data['page_number']
    page_size = data['page_size']
    comments = current_user.get_comments()
    return jsonify(comments=comments[(page-1)*page_size:page*page_size]), 200


@bp.route("/user_all_number", methods=['GET', 'POST'])
def get_all_comments_number():
    number = len(current_user.get_comments())
    return jsonify(number=number), 200



