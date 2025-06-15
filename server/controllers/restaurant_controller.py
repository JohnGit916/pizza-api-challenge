from flask import Blueprint, jsonify, request
from ..models.restaurant import Restaurant
from ..app import db

restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')

# GET /restaurants - Get all restaurants
@restaurant_bp.route('/', methods=['GET'])
def get_all_restaurants():
    restaurants = Restaurant.query.all()
    result = [
        {
            "id": r.id,
            "name": r.name,
            "address": r.address
        } for r in restaurants
    ]
    return jsonify(result), 200

# GET /restaurants/<id> - Get one restaurant by ID
@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_one_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address
    }), 200

# DELETE /restaurants/<id> - Delete restaurant by ID
@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
