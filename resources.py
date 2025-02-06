# Import necessary modules from Flask-RESTful
from flask_restful import Resource, reqparse

# Import the VideoGame model and database instance from models.py
from models import db, VideoGame

# Define a request parser to parse incoming request data
videogame_parser = reqparse.RequestParser()
videogame_parser.add_argument('title', type=str, required=True, help='Title of the video game')
videogame_parser.add_argument('platform', type=str, required=True, help='Platform of the video game')
videogame_parser.add_argument('publisher', type=str, required=True, help='Publisher of the video game')
videogame_parser.add_argument('genre', type=str, required=True, help='Genre of the video game')
videogame_parser.add_argument('release_year', type=int, required=True, help='Year of release')

# Define a resource class for handling the list of video games
class VideoGameListResource(Resource):
    def get(self):
        # Parse the 'sort_by' argument from the query string
        parser = reqparse.RequestParser()
        parser.add_argument('sort_by', type=str, choices=('platform', 'publisher', 'genre'), help='Sort by platform, publisher, or genre')
        args = parser.parse_args()

        # Create a base query to get all video games
        query = VideoGame.query
        # If 'sort_by' argument is provided, order the query by the specified column
        if args['sort_by']:
            query = query.order_by(getattr(VideoGame, args['sort_by']))

        # Execute the query and return the list of video games in JSON format
        videogames = query.all()
        return [videogame.json() for videogame in videogames]

    def post(self):
        # Parse the request data using the defined parser
        args = videogame_parser.parse_args()
        # Create a new VideoGame object with the parsed data
        videogame = VideoGame(
            title=args['title'],
            platform=args['platform'],
            publisher=args['publisher'],
            genre=args['genre'],
            release_year=args['release_year']
        )
        # Add the new video game to the database and commit the transaction
        db.session.add(videogame)
        db.session.commit()
        # Return the newly created video game in JSON format with a 201 status code
        return videogame.json(), 201

# Define a resource class for handling individual video games
class VideoGameResource(Resource):
    def get(self, videogame_id):
        # Get the video game by ID or return a 404 error if not found
        videogame = VideoGame.query.get_or_404(videogame_id)
        # Return the video game in JSON format
        return videogame.json()

    def put(self, videogame_id):
        # Parse the request data using the defined parser
        args = videogame_parser.parse_args()
        # Get the video game by ID or return a 404 error if not found
        videogame = VideoGame.query.get_or_404(videogame_id)
        # Update the video game attributes with the parsed data
        videogame.title = args['title']
        videogame.platform = args['platform']
        videogame.publisher = args['publisher']
        videogame.genre = args['genre']
        videogame.release_year = args['release_year']
        # Commit the changes to the database
        db.session.commit()
        # Return the updated video game in JSON format
        return videogame.json()

    def delete(self, videogame_id):
        # Get the video game by ID or return a 404 error if not found
        videogame = VideoGame.query.get_or_404(videogame_id)
        # Delete the video game from the database and commit the transaction
        db.session.delete(videogame)
        db.session.commit()
        # Return an empty response with a 204 status code
        return '', 204