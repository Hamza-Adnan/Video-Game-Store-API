# Import SQLAlchemy from Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy
db = SQLAlchemy()

# Define a model class for VideoGame
class VideoGame(db.Model):
    # Define the primary key column
    id = db.Column(db.Integer, primary_key=True)
    
    # Define other columns for the video game attributes
    title = db.Column(db.String(100), nullable=False)
    platform = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)

    # Method to convert the video game object to a JSON serializable format
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'platform': self.platform,
            'publisher': self.publisher,
            'genre': self.genre,
            'release_year': self.release_year
        }