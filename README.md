Pizza Restaurant API

A RESTful JSON API built with Flask, SQLAlchemy, and PostgreSQL that manages restaurants, pizzas, and the prices of pizzas at different restaurants.

---

## 📁 Project Structure

pizza-api-challenge/
├── server/
│ ├── app.py
│ ├── config.py
│ ├── extensions.py
│ ├── models/
│ │ ├── pizza.py
│ │ ├── restaurant.py
│ │ └── restaurant_pizza.py
│ ├── controllers/
│ │ ├── pizza_controller.py
│ │ ├── restaurant_controller.py
│ │ └── restaurant_pizza_controller.py
│ ├── seed.py
│ └── ...
├── migrations/
├── Pipfile
├── README.md


---

## ⚙️ Setup Instructions

1. **Clone the repository**

. Clone Your Repo

git clone https://github.com/YourUsername/pizza-api-challenge.git
cd pizza-api-challenge

2. Install Dependencies
Make sure they have Python installed. Then:

pip install pipenv
pipenv install

3. Set Environment Variable for Flask
Tell Flask where to find the app.

Linux/macOS:

export FLASK_APP=server.app:app

Windows CMD:

set FLASK_APP=server.app:app

Windows PowerShell:

$env:FLASK_APP = "server.app:app"

4. Setup database & Run Migrations

Ensure PostgreSQL is running and create a database named (or update credentials in config.py):

createdb pizza_api_db

pipenv run flask db upgrade

5. Seed the Database

pipenv run python server/seed.py

This will insert sample pizzas, restaurants, and prices.

6. Run the Flask Server
pipenv run flask run
The API will now be available at:
http://127.0.0.1:5000

🚀 API Routes
🎯 Pizzas
GET /pizzas
Returns all pizzas with id, name, and ingredients.

🏬 Restaurants
GET /restaurants
Returns all restaurants with id, name, and address.

GET /restaurants/<int:id>
Returns a specific restaurant and its associated pizzas.

DELETE /restaurants/<int:id>
Deletes a restaurant and associated restaurant-pizzas.

🍕 Restaurant Pizzas
POST /restaurant_pizzas
Creates a new restaurant-pizza (relationship between a pizza and a restaurant with a price).

Testing with Postman
=====================
Open Postman and import the file challenge-1-pizzas.postman_collection.json.

Use POST to /restaurant_pizzas to create relationships.

Use GET endpoints to confirm data is returned correctly.

Use DELETE to test data deletion.

🧠 Technologies Used
Flask

SQLAlchemy

Flask-Migrate

PostgreSQL

Pipenv

