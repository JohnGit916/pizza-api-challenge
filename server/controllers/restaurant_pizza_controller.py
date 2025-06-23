from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

# POST /restaurant_pizzas - Create a new restaurant-pizza relationship
@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    # Required fields check
    required_fields = ['price', 'pizza_id', 'restaurant_id']
    for field in required_fields:
        if field not in data:
            return jsonify({"errors": [f"'{field}' is required."]}), 400

    try:
        # Validate foreign key existence
        pizza = Pizza.query.get(data['pizza_id'])
        restaurant = Restaurant.query.get(data['restaurant_id'])

        if not pizza or not restaurant:
            return jsonify({"errors": ["Pizza or Restaurant not found."]}), 404

        rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(rp)
        db.session.commit()

        return jsonify({
            "id": rp.id,
            "price": rp.price,
            "pizza_id": rp.pizza_id,
            "restaurant_id": rp.restaurant_id,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        }), 201

    except ValueError as ve:
        # Catch price validation error
        return jsonify({"errors": [str(ve)]}), 400

    except Exception as e:
        return jsonify({"errors": [f"Unexpected error: {str(e)}"]}), 500
