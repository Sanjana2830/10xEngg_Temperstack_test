# 10xEngg_Temperstack_test

# Movie Database API

This project is a Django-based RESTful API for managing a movie database. The API allows users to create, retrieve, update, and delete movies, performers, genres, and other related entities. It also supports filtering, searching, and pagination.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Docker Setup](#docker-setup) (if applicable)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create, retrieve, update, and delete movies.
- Manage performers, genres, languages, and more.
- Filtering and searching capabilities.
- [Optional] Dockerized setup for easy deployment.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/moviedatabaseapi.git
   cd moviedatabaseapi

2. **Create and Activate a Virtual Environment:**
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **install dependencies**
  pip install -r requirements.txt

4. **migrate**
   python manage.py migrate

5. **Run the Development Server:**
  python manage.py runserver

## Usage

After running the development server, you can access the API endpoints in your browser or using tools like Postman.

- **Home Page:** `http://127.0.0.1:8000/`
- **API Index:** `http://127.0.0.1:8000/api/`

Example to fetch all movies:
GET http://127.0.0.1:8000/api/movies/

## API Endpoints

### Movies

- **List/Create Movies**  
  `GET /api/movies/`  
  `POST /api/movies/`
  
  Example Request:
  bash
  GET http://127.0.0.1:8000/api/movies/
Retrieve/Update/Delete Movie
GET /api/movies/{id}/
PUT /api/movies/{id}/
DELETE /api/movies/{id}/

  Example Request:
  GET http://127.0.0.1:8000/api/movies/1/
  Performers
  List/Create Performers
  GET /api/performers/
  POST /api/performers/
  
  Retrieve/Update/Delete Performer
  GET /api/performers/{id}/
  PUT /api/performers/{id}/
  DELETE /api/performers/{id}/
  
  Genres, Languages, etc.
  Follow the same structure for other models.
  Filtering, Searching, and Ordering
  Filtering: GET /api/movies/?genre=Action
  Searching: GET /api/movies/?search=Inception
  Ordering: GET /api/movies/?ordering=year_of_release


## Testing

To run the automated tests, use the following command:

bash
python manage.py test

## Docker Setup

If you'd like to run the project in a Docker container, follow these steps:
**Build the Docker Image:**
   ```bash
   docker build -t my-django-app .
**Run the Docker Container:**
  docker run -p 8000:8000 my-django-app
**Using Docker Compose (Optional):**
  docker-compose up

Your application will be available at http://localhost:8000.

![image](https://github.com/user-attachments/assets/fe46ee0d-e0fd-4272-b7d0-cf86a35cc652)

![image](https://github.com/user-attachments/assets/051e6548-234f-4f4b-91a7-662f5c07dc07)

![image](https://github.com/user-attachments/assets/6007c5be-c885-406a-bebe-4f82aa748ec9)

