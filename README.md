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

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd pizza-api-challenge
Create a virtual environment

bash
Copy
Edit
pipenv install
pipenv shell
Configure the database

PostgreSQL must be installed and running.

Create a database (e.g., pizza_db):

bash
Copy
Edit
createdb pizza_db
Update your Config in server/config.py:

python
Copy
Edit
SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@localhost:5432/pizza_db'
Run migrations

bash
Copy
Edit
pipenv run flask db init
pipenv run flask db migrate -m "Initial migration"
pipenv run flask db upgrade
Seed the database

bash
Copy
Edit
pipenv run python -m server.seed
Run the server

bash
Copy
Edit
pipenv run flask run
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
Import the API endpoints manually or create a collection.

Use POST to /restaurant_pizzas with raw JSON body to create relationships.

Test GET endpoints to confirm data is returned correctly.

🧠 Technologies Used
Flask

SQLAlchemy

Flask-Migrate

PostgreSQL

Pipenv

