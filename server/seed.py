from .app import app, db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza


with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Mario's Pizza", address="123 Pizza St")
    r2 = Restaurant(name="Luigi's Pies", address="456 Pasta Ave")

    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Hawaiian", ingredients="Pineapple, Ham, Cheese")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=15, pizza_id=p2.id, restaurant_id=r1.id)
    rp3 = RestaurantPizza(price=8, pizza_id=p1.id, restaurant_id=r2.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("Database seeded successfully!")
