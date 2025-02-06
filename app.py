# Import necessary modules from Flask and Flask-RESTful
from flask import Flask
from flask_restful import Api

# Import the resource classes from resources.py
from resources import VideoGameResource, VideoGameListResource

# Create a Flask application instance
app = Flask(__name__)

# Create an Api instance and wrap the Flask app
api = Api(app)

# Configure the Flask app to use SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import the database instance from models.py
from models import db

# Initialize the database with the Flask app
db.init_app(app)

# Add resources and their routes to the API
api.add_resource(VideoGameListResource, '/videogames')
api.add_resource(VideoGameResource, '/videogames/<int:videogame_id>')

# Run the Flask app in debug mode if the script is executed directly
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables before running the app
    app.run(debug=True)