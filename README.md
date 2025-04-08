# paloAlto_Backend

This is the backend API for the FitFoodie application, built with Flask.

## Features

- User authentication (register, login)
- User profiles with physical attributes and dietary preferences
- Influencer profiles with specialties and social media links
- Meal creation and management by influencers
- Meal discovery with macronutrient information
- Favoriting meals and following influencers
- Affiliate links for ingredients and products

## Tech Stack

- Flask: Web framework
- Flask-SQLAlchemy: ORM for database operations
- Flask-JWT-Extended: JWT authentication
- Flask-CORS: Cross-Origin Resource Sharing
- SQLite (development) / PostgreSQL (production)

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Set up environment variables (copy `.env.example` to `.env` and modify as needed)
6. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```
7. Run the development server:
   ```
   flask run
   ```

## API Endpoints

### Authentication

- `POST /api/auth/register`: Register a new user
- `POST /api/auth/login`: Login a user
- `GET /api/auth/me`: Get current user information

### Users

- `GET /api/users/profile`: Get user profile
- `PUT /api/users/profile`: Update user profile
- `GET /api/users/favorites`: Get user's favorite meals
- `GET /api/users/following`: Get influencers the user is following
- `PUT /api/users/change-password`: Change user password

### Meals

- `GET /api/meals`: Get all meals (with pagination and filtering)
- `GET /api/meals/<id>`: Get a specific meal
- `POST /api/meals`: Create a new meal (influencers only)
- `PUT /api/meals/<id>`: Update a meal (influencers only)
- `DELETE /api/meals/<id>`: Delete a meal (influencers only)
- `POST /api/meals/favorite/<id>`: Favorite a meal
- `DELETE /api/meals/favorite/<id>`: Unfavorite a meal

### Influencers

- `GET /api/influencers`: Get all influencers (with pagination and filtering)
- `GET /api/influencers/<id>`: Get a specific influencer
- `POST /api/influencers/profile`: Create an influencer profile
- `PUT /api/influencers/profile`: Update an influencer profile
- `POST /api/influencers/follow/<id>`: Follow an influencer
- `DELETE /api/influencers/unfollow/<id>`: Unfollow an influencer

## Error Handling

The API returns appropriate HTTP status codes and error messages in JSON format:

```json
{
  "error": "Error type",
  "message": "Detailed error message"
}
```

## Database Schema

The database consists of the following main tables:

- `users`: User information and preferences
- `influencers`: Influencer profiles linked to users
- `meals`: Meal information with macronutrients and instructions
- `user_favorites`: Association table for user-meal favorites
- `user_following`: Association table for user-influencer following
