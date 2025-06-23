from flask import Blueprint, request, jsonify
from ..models.pizza import Pizza
from ..extensions import db

pizza_bp = Blueprint('pizzas', __name__, url_prefix='/pizzas')

# GET /pizzas - Retrieve all pizzas
@pizza_bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "ingredients": p.ingredients
        } for p in pizzas
    ]), 200

# POST /pizzas - Create a new pizza
@pizza_bp.route('', methods=['POST'])
def create_pizza():
    data = request.get_json()
    try:
        new_pizza = Pizza(
            name=data['name'],
            ingredients=data['ingredients']
        )
        db.session.add(new_pizza)
        db.session.commit()

        return jsonify({
            "id": new_pizza.id,
            "name": new_pizza.name,
            "ingredients": new_pizza.ingredients
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# PUT /pizzas/<id> - Update a pizza
@pizza_bp.route('/<int:id>', methods=['PUT'])
def update_pizza(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({"error": "Pizza not found"}), 404

    data = request.get_json()
    pizza.name = data.get('name', pizza.name)
    pizza.ingredients = data.get('ingredients', pizza.ingredients)

    db.session.commit()
    return jsonify({
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients
    }), 200

# DELETE /pizzas/<id> - Delete a pizza
@pizza_bp.route('/<int:id>', methods=['DELETE'])
def delete_pizza(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({"error": "Pizza not found"}), 404

    db.session.delete(pizza)
    db.session.commit()
    return '', 204
