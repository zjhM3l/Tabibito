import math

from sqlalchemy import func
from flask import Blueprint, jsonify, request
import datetime
from exts import db
from models import Product, Tag, UserBrowse, Comment, User, Order, ProductType, PType
from collections import Counter
from sqlalchemy import and_

bp = Blueprint("Homepage", __name__, url_prefix="/homepage")


@bp.route("/most_popular_products", methods=["POST", "GET"])
def test():
    top_three_products = (
        db.session.query(Product)
        .outerjoin(UserBrowse)
        .group_by(Product.id)
        .order_by(func.count(UserBrowse.id).desc())
        .limit(3)
        .all()
    )

    return jsonify(products=[product.serialize_homepage() for product in top_three_products])


@bp.route("/search", methods=['GET'])
def search():
    location = request.json.get('location')
    tags = request.json.get('tags')
    start_time = datetime.datetime.fromtimestamp(request.json.get('start_time') / 1000)
    end_time = datetime.datetime.fromtimestamp(request.json.get('end_time') / 1000)
    products = Product.query.filter(Product.raw_loc.ilike(f'%{location}%'),
                                    Product.start_time >= start_time,
                                    Product.end_time <= end_time,
                                    Product.tags.any(Tag.key.in_(tags))
                                    ).all()
    return jsonify(products=[product.serialize_search() for product in products])


@bp.route("/location", methods=['GET'])
def locations():
    products = Product.query.all()
    all_locations = [product.raw_loc.split(",")[-1].strip() for product in products]
    location_counts = Counter(all_locations)

    most_common_locations = location_counts.most_common(8)
    most_common_locations = [lc[0] for lc in most_common_locations]

    covers = {}
    for loc in most_common_locations:
        product = Product.query.filter(Product.raw_loc.like("%"+loc+"%")).first()
        if product:
            covers[loc] = product.pictures[0].address

    result = {
        "locations": [
            {
                "name": loc,
                "project_count": location_counts[loc],
                "picture": covers[loc]
            }
            for loc in most_common_locations
        ]
    }
    return result


@bp.route("/lowest_discount", methods=['GET'])
def lowest_discount_products():
    products = Product.query.order_by(Product.discount).limit(3).all()
    return jsonify(products=[product.serialize_homepage() for product in products])


@bp.route("/four_number", methods=['GET'])
def four_number():
    reviews = Comment.query.count()
    products = Product.query.count()
    # 计算平均分大于4的用户数量
    users_count = (
        db.session.query(User)
        .join(Comment)
        .with_entities(User.user_id)
        .group_by(User.user_id)
        .having(func.avg(
            Comment.location_grade +
            Comment.staff_grade +
            Comment.cleanliness_grade +
            Comment.value_for_money_grade +
            Comment.comfort_grade +
            Comment.facilities_grade +
            Comment.free_wifi_grade
        ) > 4.5)
        .count()
    )
    orders = Order.query.count()

    return jsonify(review_count=reviews, product_count=products, happy_customer_count=users_count, order_count=orders)


@bp.route("/next_two_months", methods=['GET'])
def next_two_months():
    now = datetime.datetime.now()
    end_date = now + datetime.timedelta(days=60)

    products = Product.query.filter(and_(Product.start_time >= now, Product.start_time <= end_date)).all()
    return jsonify(products=[product.serialize_homepage() for product in products])


@bp.route("/most_popular_comments", methods=["GET"])
def get_popular_comments():
    comments = db.session.query(Comment).order_by(Comment.like_num.desc()).limit(5).all()
    return jsonify(code=200, data=[comment.serialize_homepage() for comment in comments])


# 可以使用推荐算法筛选3个项目
@bp.route("/inspiration", methods=["GET"])
def get_inspiration():
    products = db.session.query(Product).limit(3).all()
    return jsonify(code=200, inspirations=[product.serialize_inspiration() for product in products])


@bp.route("/more", methods=["GET", "POST"])
def more_products():
    page_number = 0
    search_type = request.json.get('type')
    value = request.json.get('value')
    print(search_type, value)
    if search_type == "popular":
        page_number = 2
    elif search_type == "type":
        print(value)
        page_number = math.ceil(Product.query.filter(Product.types.any(ProductType.type == PType(value))).count()/4)
    elif search_type == "location":
        print(value)

        page_number = math.ceil(Product.query.filter(Product.raw_loc.like("%"+value+"%")).count() / 4)
    else:
        page_number = 0
    return jsonify(page_number=page_number, code=200)


@bp.route("/more_program_list", methods=["GET", "POST"])
def more_program_list():
    search_type = request.json.get('type')
    value = request.json.get('value')
    page = request.json.get('page')
    products = []
    if search_type == "popular":
        products = Product.query.outerjoin(UserBrowse).group_by(Product.id).order_by(func.count(UserBrowse.id).desc()).paginate(page=page, per_page=4)
    elif search_type == "type":
        products = Product.query.filter(Product.types.any(ProductType.type == PType(value))).paginate(page=page, per_page=4)
    elif search_type == "location":
        products = Product.query.filter(Product.raw_loc.like("%"+value+"%")).paginate(page=page, per_page=4)
        print(value)
        print([product.serialize_more() for product in products])
    return jsonify(products=[product.serialize_more() for product in products])


@bp.route("/all_location", methods=["GET", "POST"])
def all_locations():
    products = Product.query.all()
    result = sorted(list(set([product.raw_loc.split(",")[-1].strip() for product in products])))
    return jsonify(locations=result), 200