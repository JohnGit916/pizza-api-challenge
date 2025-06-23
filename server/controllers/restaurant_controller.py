from flask import Blueprint, jsonify, request
from ..models.restaurant import Restaurant
from ..extensions import db

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

# GET /restaurants/<id> - Get one restaurant by ID with nested pizzas
@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_one_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": [
            {
                "id": rp.pizza.id,
                "name": rp.pizza.name,
                "ingredients": rp.pizza.ingredients
            } for rp in restaurant.restaurant_pizzas
        ]
    }), 200

# POST /restaurants - Create a new restaurant
@restaurant_bp.route('/', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    try:
        new_restaurant = Restaurant(
            name=data['name'],
            address=data['address']
        )
        db.session.add(new_restaurant)
        db.session.commit()

        return jsonify({
            "id": new_restaurant.id,
            "name": new_restaurant.name,
            "address": new_restaurant.address
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# PUT /restaurants/<id> - Update a restaurant
@restaurant_bp.route('/<int:id>', methods=['PUT'])
def update_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    data = request.get_json()
    restaurant.name = data.get('name', restaurant.name)
    restaurant.address = data.get('address', restaurant.address)
    db.session.commit()

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
