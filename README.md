# Video Game Store API

## Overview

The Video Game Store API is a RESTful web service that allows users to perform CRUD operations on a collection of video games. Users can add new video games, retrieve a list of all video games, get details of a specific video game by ID, update details of a specific video game by ID, delete a specific video game by ID, and sort video games by platform, publisher, and genre.

## Technologies Used

- Python
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- SQLite

## Project Structure

```plaintext
videogame-store-api
├── app.py
├── models.py
├── resources.py
├── db.sqlite
└── requirements.txt
```

## Setup and Installation
1. Clone the repository:
```bash
git clone https://github.com/Hamza-Adnan/Video-Game-Store-API.git
cd videogame-store-api
```
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Flask application:
```bash
python app.py
```
The application will be running on http://127.0.0.1:5000.

## API Endpoints
1. Get All Video Games
* Endpoint: Get /videogames
* Description: Retrieve a list of all video games.
* Query Parameters:
    * ```sort_by``` (optional): Sort video games by platform, publisher, or genre.
Example Request:
```bash
curl http://127.0.0.1:5000/videogames
```
Example Request with Sorting:
```bash
curl http://127.0.0.1:5000/videogames?sort_by=platform
```
2. Add a New Video Game
* Endpoint: ```POST /videogames```
* Description: Add a new video game to the store.
* Request Body:
```JSON
{
  "title": "Game Title",
  "platform": "Platform",
  "publisher": "Publisher",
  "genre": "Genre",
  "release_year": 2025
}
```
Example Request:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "Game Title", "platform": "Platform", "publisher": "Publisher", "genre": "Genre", "release_year": 2025}' http://127.0.0.1:5000/videogames
```
3. Get a Specific Video Game by ID
* Endpoint: ```GET /videogames/<videogame_id>```
* Description: Retrieve details of a specific video game by ID.
Example Request:
```bash
curl http://127.0.0.1:5000/videogames/1
```
4. Update a Video Game by ID
* Endpoint: ```PUT /videogames/<videogame_id>```
* Description: Update details of a specific video game by ID.
* Request Body:
```JSON
{
  "title": "Updated Title",
  "platform": "Updated Platform",
  "publisher": "Updated Publisher",
  "genre": "Updated Genre",
  "release_year": 2026
}
```
Example Request:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Title", "platform": "Updated Platform", "publisher": "Updated Publisher", "genre": "Updated Genre", "release_year": 2026}' http://127.0.0.1:5000/videogames/1
```
5. Delete a Video Game by ID
* Endpoint: ```DELETE /videogames/<videogame_id>```
* Description: Delete a specific video game by ID.

Example Request:
```bash
curl -X DELETE http://127.0.0.1:5000/videogames/1
```












