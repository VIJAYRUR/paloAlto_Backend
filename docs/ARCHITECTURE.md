# FitFoodie Backend Architecture

This document provides an overview of the FitFoodie Backend architecture, including the system design, data models, and key components.

## System Architecture

The FitFoodie Backend follows a layered architecture pattern:

```
┌─────────────────┐
│                 │
│    API Layer    │
│    (Routes)     │
│                 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│                 │
│  Business Logic │
│    (Services)   │
│                 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│                 │
│   Data Access   │
│    (Models)     │
│                 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│                 │
│    Database     │
│   (MongoDB)     │
│                 │
└─────────────────┘
```

### Key Components

1. **API Layer (Routes)**
   - Handles HTTP requests and responses
   - Implements RESTful API endpoints
   - Manages authentication and authorization
   - Validates input data

2. **Business Logic Layer (Services)**
   - Implements business rules and logic
   - Coordinates operations across multiple models
   - Handles complex operations and transactions

3. **Data Access Layer (Models)**
   - Defines data models and schemas
   - Provides methods for CRUD operations
   - Handles data validation and transformation

4. **Database Layer**
   - MongoDB for data storage
   - Indexes for optimized queries
   - Data persistence and retrieval

## Directory Structure

```
FitFoodie-Backend/
├── app.py                  # Main application file
├── config.py               # Configuration settings
├── models.py               # Database models
├── routes/                 # API routes
│   ├── __init__.py
│   ├── auth.py             # Authentication routes
│   ├── users.py            # User-related routes
│   ├── meals.py            # Meal-related routes
│   └── influencers.py      # Influencer-related routes
├── utils/                  # Utility functions
│   ├── __init__.py
│   ├── auth.py             # Authentication utilities
│   └── helpers.py          # Helper functions
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_meals.py
├── requirements.txt        # Python dependencies
└── run.py                  # Script to run the server
```

## Data Models

### User Model

```python
{
    "_id": ObjectId,
    "name": str,
    "email": str,
    "password": str,  # Hashed
    "username": str,
    "avatar": str,  # URL to avatar image
    "bio": str,
    "is_influencer": bool,
    "physical_profile": {
        "height": float,  # cm
        "weight": float,  # kg
        "age": int,
        "activity_level": str
    },
    "dietary_preferences": [str],
    "allergies": [str],
    "health_goals": [str],
    "favorite_meals": [ObjectId],  # References to Meal documents
    "favorite_influencers": [ObjectId],  # References to User documents
    "settings": {
        "notifications": bool,
        "dark_mode": bool,
        "metric_units": bool,
        "privacy_mode": bool
    },
    "created_at": datetime,
    "updated_at": datetime
}
```

### Meal Model

```python
{
    "_id": ObjectId,
    "title": str,
    "description": str,
    "image": str,  # URL to meal image
    "influencer_id": ObjectId,  # Reference to User document
    "macros": {
        "calories": int,
        "protein": float,  # g
        "carbs": float,  # g
        "fat": float  # g
    },
    "ingredients": [
        {
            "name": str,
            "amount": str,
            "affiliate_link": str  # URL to purchase
        }
    ],
    "instructions": [str],
    "tags": [str],
    "likes": int,
    "comments": int,
    "created_at": datetime,
    "updated_at": datetime
}
```

### Order Model

```python
{
    "_id": ObjectId,
    "user_id": ObjectId,  # Reference to User document
    "items": [
        {
            "ingredient_name": str,
            "amount": str,
            "price": float,
            "affiliate_link": str
        }
    ],
    "total_price": float,
    "status": str,  # "pending", "processing", "completed", "cancelled"
    "created_at": datetime,
    "updated_at": datetime
}
```

## Authentication Flow

The backend uses JWT (JSON Web Tokens) for authentication:

1. **Registration**:
   - User submits registration data
   - Backend validates the data
   - Password is hashed
   - User document is created in the database
   - JWT token is generated and returned

2. **Login**:
   - User submits email/username and password
   - Backend validates credentials
   - JWT token is generated and returned

3. **Authentication**:
   - Client includes JWT token in the Authorization header
   - Backend validates the token
   - If valid, the request is processed
   - If invalid, a 401 Unauthorized response is returned

## API Design

The API follows RESTful principles:

- Uses standard HTTP methods (GET, POST, PUT, DELETE)
- Returns appropriate HTTP status codes
- Uses JSON for request and response bodies
- Implements pagination for list endpoints
- Provides filtering and sorting options

## Error Handling

The backend implements a consistent error handling approach:

- Returns appropriate HTTP status codes
- Provides detailed error messages
- Logs errors for debugging
- Handles expected and unexpected errors

Example error response:

```json
{
  "error": "VALIDATION_ERROR",
  "message": "Email is required",
  "details": {
    "field": "email",
    "value": null
  }
}
```

## Security Considerations

The backend implements several security measures:

- Password hashing using bcrypt
- JWT for secure authentication
- Input validation to prevent injection attacks
- CORS configuration to control access
- Rate limiting to prevent abuse
- Environment variables for sensitive configuration

## Performance Considerations

To ensure good performance, the backend:

- Uses database indexes for frequently queried fields
- Implements pagination for large result sets
- Uses caching where appropriate
- Optimizes database queries
- Implements efficient data structures

## Scalability Considerations

The backend is designed to scale:

- Stateless design for horizontal scaling
- Database connection pooling
- Separation of concerns for modular growth
- Efficient resource utilization

## Monitoring and Logging

The backend includes:

- Structured logging for debugging and monitoring
- Performance metrics collection
- Error tracking and reporting
- Health check endpoints

## Testing Strategy

The backend is tested using:

- Unit tests for individual functions
- Integration tests for API endpoints
- Mock objects for external dependencies
- Test coverage reporting
