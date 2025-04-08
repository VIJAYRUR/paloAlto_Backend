# FitFoodie Backend API Documentation

This document provides detailed information about the FitFoodie Backend API endpoints, request/response formats, and authentication requirements.

## Base URL

For local development:
```
http://localhost:5000/api
```

For production:
```
https://api.fitfoodie.com/api
```

## Authentication

Most API endpoints require authentication. Include the JWT token in the Authorization header:

```
Authorization: Bearer <token>
```

### Getting a Token

To get a token, use the login endpoint:

```
POST /auth/login
```

## API Endpoints

### Health Check

#### Check API Status

```
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "version": "1.0.0"
}
```

### Authentication

#### Register a New User

```
POST /auth/register
```

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword",
  "username": "johndoe"
}
```

**Response:**
```json
{
  "success": true,
  "message": "User registered successfully",
  "user": {
    "id": "60d21b4667d0d8992e610c85",
    "name": "John Doe",
    "email": "john@example.com",
    "username": "johndoe"
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

#### Login

```
POST /auth/login
```

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Login successful",
  "user": {
    "id": "60d21b4667d0d8992e610c85",
    "name": "John Doe",
    "email": "john@example.com",
    "username": "johndoe"
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

#### Get Current User

```
GET /auth/me
```

**Response:**
```json
{
  "success": true,
  "user": {
    "id": "60d21b4667d0d8992e610c85",
    "name": "John Doe",
    "email": "john@example.com",
    "username": "johndoe",
    "avatar": "https://example.com/avatar.jpg",
    "bio": "Fitness enthusiast",
    "is_influencer": false
  }
}
```

### Users

#### Get User Profile

```
GET /users/profile
```

**Response:**
```json
{
  "success": true,
  "profile": {
    "id": "60d21b4667d0d8992e610c85",
    "name": "John Doe",
    "email": "john@example.com",
    "username": "johndoe",
    "avatar": "https://example.com/avatar.jpg",
    "bio": "Fitness enthusiast",
    "is_influencer": false,
    "physical_profile": {
      "height": 178,
      "weight": 75,
      "age": 28,
      "activity_level": "Moderate"
    },
    "dietary_preferences": ["High Protein", "Low Carb"],
    "allergies": ["Peanuts"],
    "health_goals": ["Weight Management", "Muscle Gain"]
  }
}
```

#### Update User Profile

```
PUT /users/profile
```

**Request Body:**
```json
{
  "bio": "Fitness enthusiast and healthy food lover",
  "physical_profile": {
    "weight": 73
  },
  "dietary_preferences": ["High Protein", "Low Carb", "Gluten Free"]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Profile updated successfully",
  "profile": {
    "id": "60d21b4667d0d8992e610c85",
    "name": "John Doe",
    "bio": "Fitness enthusiast and healthy food lover",
    "physical_profile": {
      "height": 178,
      "weight": 73,
      "age": 28,
      "activity_level": "Moderate"
    },
    "dietary_preferences": ["High Protein", "Low Carb", "Gluten Free"]
  }
}
```

#### Get User Favorites

```
GET /users/favorites
```

**Response:**
```json
{
  "success": true,
  "favorites": {
    "meals": [
      {
        "id": "60d21b4667d0d8992e610c86",
        "title": "Protein-Packed Breakfast Bowl",
        "image": "https://example.com/meal.jpg",
        "macros": {
          "calories": 450,
          "protein": 30,
          "carbs": 45,
          "fat": 15
        },
        "influencer": {
          "id": "60d21b4667d0d8992e610c87",
          "name": "Fitness Chef",
          "avatar": "https://example.com/chef.jpg"
        }
      }
    ],
    "influencers": [
      {
        "id": "60d21b4667d0d8992e610c87",
        "name": "Fitness Chef",
        "avatar": "https://example.com/chef.jpg",
        "is_verified": true
      }
    ]
  }
}
```

#### Change Password

```
PUT /users/change-password
```

**Request Body:**
```json
{
  "current_password": "currentpassword",
  "new_password": "newpassword",
  "confirm_password": "newpassword"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Password changed successfully"
}
```

### Meals

#### Get All Meals

```
GET /meals
```

**Query Parameters:**
- `page` (optional): Page number for pagination (default: 1)
- `limit` (optional): Number of meals per page (default: 10)
- `influencer_id` (optional): Filter by influencer
- `tags` (optional): Filter by tags (comma-separated)

**Response:**
```json
{
  "success": true,
  "meals": [
    {
      "id": "60d21b4667d0d8992e610c86",
      "title": "Protein-Packed Breakfast Bowl",
      "description": "Start your day with this protein-rich breakfast bowl",
      "image": "https://example.com/meal.jpg",
      "macros": {
        "calories": 450,
        "protein": 30,
        "carbs": 45,
        "fat": 15
      },
      "influencer": {
        "id": "60d21b4667d0d8992e610c87",
        "name": "Fitness Chef",
        "avatar": "https://example.com/chef.jpg"
      },
      "likes": 120,
      "comments": 15
    }
  ],
  "pagination": {
    "total": 45,
    "page": 1,
    "limit": 10,
    "pages": 5
  }
}
```

#### Get Meal by ID

```
GET /meals/:id
```

**Response:**
```json
{
  "success": true,
  "meal": {
    "id": "60d21b4667d0d8992e610c86",
    "title": "Protein-Packed Breakfast Bowl",
    "description": "Start your day with this protein-rich breakfast bowl",
    "image": "https://example.com/meal.jpg",
    "macros": {
      "calories": 450,
      "protein": 30,
      "carbs": 45,
      "fat": 15
    },
    "ingredients": [
      {
        "name": "Greek Yogurt",
        "amount": "1 cup",
        "affiliate_link": "https://example.com/greek-yogurt"
      },
      {
        "name": "Granola",
        "amount": "1/4 cup",
        "affiliate_link": "https://example.com/granola"
      }
    ],
    "instructions": [
      "Add Greek yogurt to a bowl",
      "Top with granola and fresh fruits",
      "Drizzle with honey"
    ],
    "tags": ["breakfast", "high-protein", "quick"],
    "influencer": {
      "id": "60d21b4667d0d8992e610c87",
      "name": "Fitness Chef",
      "avatar": "https://example.com/chef.jpg"
    },
    "likes": 120,
    "comments": 15,
    "created_at": "2023-06-15T10:30:00Z"
  }
}
```

#### Create a Meal (Influencer Only)

```
POST /meals
```

**Request Body:**
```json
{
  "title": "Green Smoothie Bowl",
  "description": "Nutrient-packed smoothie bowl with spinach and fruits",
  "image": "https://example.com/smoothie.jpg",
  "macros": {
    "calories": 320,
    "protein": 12,
    "carbs": 60,
    "fat": 8
  },
  "ingredients": [
    {
      "name": "Spinach",
      "amount": "1 cup",
      "affiliate_link": "https://example.com/spinach"
    },
    {
      "name": "Banana",
      "amount": "1 medium",
      "affiliate_link": "https://example.com/banana"
    }
  ],
  "instructions": [
    "Blend spinach and banana with almond milk",
    "Pour into a bowl",
    "Top with granola and berries"
  ],
  "tags": ["breakfast", "vegan", "smoothie"]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Meal created successfully",
  "meal": {
    "id": "60d21b4667d0d8992e610c88",
    "title": "Green Smoothie Bowl",
    "description": "Nutrient-packed smoothie bowl with spinach and fruits",
    "image": "https://example.com/smoothie.jpg",
    "macros": {
      "calories": 320,
      "protein": 12,
      "carbs": 60,
      "fat": 8
    }
  }
}
```

#### Update a Meal (Influencer Only)

```
PUT /meals/:id
```

**Request Body:**
```json
{
  "title": "Updated Green Smoothie Bowl",
  "description": "Updated description",
  "macros": {
    "calories": 340,
    "protein": 14,
    "carbs": 62,
    "fat": 9
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Meal updated successfully",
  "meal": {
    "id": "60d21b4667d0d8992e610c88",
    "title": "Updated Green Smoothie Bowl",
    "description": "Updated description",
    "macros": {
      "calories": 340,
      "protein": 14,
      "carbs": 62,
      "fat": 9
    }
  }
}
```

#### Delete a Meal (Influencer Only)

```
DELETE /meals/:id
```

**Response:**
```json
{
  "success": true,
  "message": "Meal deleted successfully"
}
```

#### Favorite a Meal

```
POST /meals/favorite/:id
```

**Response:**
```json
{
  "success": true,
  "message": "Meal added to favorites"
}
```

#### Unfavorite a Meal

```
DELETE /meals/favorite/:id
```

**Response:**
```json
{
  "success": true,
  "message": "Meal removed from favorites"
}
```

### Influencers

#### Get All Influencers

```
GET /influencers
```

**Query Parameters:**
- `page` (optional): Page number for pagination (default: 1)
- `limit` (optional): Number of influencers per page (default: 10)

**Response:**
```json
{
  "success": true,
  "influencers": [
    {
      "id": "60d21b4667d0d8992e610c87",
      "name": "Fitness Chef",
      "username": "@fitnesschef",
      "avatar": "https://example.com/chef.jpg",
      "bio": "Healthy recipes for fitness enthusiasts",
      "is_verified": true,
      "specialty": "High-protein meals",
      "followers": 15000
    }
  ],
  "pagination": {
    "total": 25,
    "page": 1,
    "limit": 10,
    "pages": 3
  }
}
```

#### Get Influencer by ID

```
GET /influencers/:id
```

**Response:**
```json
{
  "success": true,
  "influencer": {
    "id": "60d21b4667d0d8992e610c87",
    "name": "Fitness Chef",
    "username": "@fitnesschef",
    "avatar": "https://example.com/chef.jpg",
    "bio": "Healthy recipes for fitness enthusiasts",
    "is_verified": true,
    "specialty": "High-protein meals",
    "followers": 15000,
    "stats": {
      "total_posts": 45,
      "total_likes": 5600,
      "total_comments": 890
    },
    "social_media": {
      "instagram": "https://instagram.com/fitnesschef",
      "twitter": "https://twitter.com/fitnesschef",
      "youtube": "https://youtube.com/fitnesschef"
    }
  }
}
```

#### Get Influencer Meals

```
GET /influencers/:id/meals
```

**Query Parameters:**
- `page` (optional): Page number for pagination (default: 1)
- `limit` (optional): Number of meals per page (default: 10)

**Response:**
```json
{
  "success": true,
  "meals": [
    {
      "id": "60d21b4667d0d8992e610c86",
      "title": "Protein-Packed Breakfast Bowl",
      "description": "Start your day with this protein-rich breakfast bowl",
      "image": "https://example.com/meal.jpg",
      "macros": {
        "calories": 450,
        "protein": 30,
        "carbs": 45,
        "fat": 15
      },
      "likes": 120,
      "comments": 15,
      "created_at": "2023-06-15T10:30:00Z"
    }
  ],
  "pagination": {
    "total": 45,
    "page": 1,
    "limit": 10,
    "pages": 5
  }
}
```

#### Create Influencer Profile (User Only)

```
POST /influencers/profile
```

**Request Body:**
```json
{
  "specialty": "High-protein meals",
  "bio": "Healthy recipes for fitness enthusiasts",
  "social_media": {
    "instagram": "https://instagram.com/fitnesschef",
    "twitter": "https://twitter.com/fitnesschef",
    "youtube": "https://youtube.com/fitnesschef"
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Influencer profile created successfully",
  "influencer": {
    "id": "60d21b4667d0d8992e610c87",
    "name": "Fitness Chef",
    "username": "@fitnesschef",
    "specialty": "High-protein meals",
    "bio": "Healthy recipes for fitness enthusiasts",
    "social_media": {
      "instagram": "https://instagram.com/fitnesschef",
      "twitter": "https://twitter.com/fitnesschef",
      "youtube": "https://youtube.com/fitnesschef"
    }
  }
}
```

#### Update Influencer Profile (Influencer Only)

```
PUT /influencers/profile
```

**Request Body:**
```json
{
  "specialty": "Updated specialty",
  "bio": "Updated bio",
  "social_media": {
    "instagram": "https://instagram.com/updated",
    "twitter": "https://twitter.com/updated",
    "youtube": "https://youtube.com/updated"
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Influencer profile updated successfully",
  "influencer": {
    "id": "60d21b4667d0d8992e610c87",
    "name": "Fitness Chef",
    "username": "@fitnesschef",
    "specialty": "Updated specialty",
    "bio": "Updated bio",
    "social_media": {
      "instagram": "https://instagram.com/updated",
      "twitter": "https://twitter.com/updated",
      "youtube": "https://youtube.com/updated"
    }
  }
}
```

#### Follow an Influencer

```
POST /influencers/follow/:id
```

**Response:**
```json
{
  "success": true,
  "message": "Now following Fitness Chef"
}
```

#### Unfollow an Influencer

```
DELETE /influencers/unfollow/:id
```

**Response:**
```json
{
  "success": true,
  "message": "Unfollowed Fitness Chef"
}
```

### Orders

#### Create an Order

```
POST /orders
```

**Request Body:**
```json
{
  "items": [
    {
      "ingredient_name": "Greek Yogurt",
      "amount": "1 cup",
      "price": 3.99,
      "affiliate_link": "https://example.com/greek-yogurt"
    },
    {
      "ingredient_name": "Granola",
      "amount": "1/4 cup",
      "price": 2.49,
      "affiliate_link": "https://example.com/granola"
    }
  ],
  "promo_code": "SUMMER10"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Order created successfully",
  "order": {
    "id": "60d21b4667d0d8992e610c89",
    "items": [
      {
        "ingredient_name": "Greek Yogurt",
        "amount": "1 cup",
        "price": 3.99,
        "affiliate_link": "https://example.com/greek-yogurt"
      },
      {
        "ingredient_name": "Granola",
        "amount": "1/4 cup",
        "price": 2.49,
        "affiliate_link": "https://example.com/granola"
      }
    ],
    "subtotal": 6.48,
    "discount": 0.65,
    "total_price": 5.83,
    "status": "pending",
    "created_at": "2023-06-20T14:25:00Z"
  }
}
```

#### Get User Orders

```
GET /orders
```

**Query Parameters:**
- `page` (optional): Page number for pagination (default: 1)
- `limit` (optional): Number of orders per page (default: 10)

**Response:**
```json
{
  "success": true,
  "orders": [
    {
      "id": "60d21b4667d0d8992e610c89",
      "items": [
        {
          "ingredient_name": "Greek Yogurt",
          "amount": "1 cup",
          "price": 3.99,
          "affiliate_link": "https://example.com/greek-yogurt"
        },
        {
          "ingredient_name": "Granola",
          "amount": "1/4 cup",
          "price": 2.49,
          "affiliate_link": "https://example.com/granola"
        }
      ],
      "total_price": 5.83,
      "status": "processing",
      "created_at": "2023-06-20T14:25:00Z"
    }
  ],
  "pagination": {
    "total": 3,
    "page": 1,
    "limit": 10,
    "pages": 1
  }
}
```

#### Get Order by ID

```
GET /orders/:id
```

**Response:**
```json
{
  "success": true,
  "order": {
    "id": "60d21b4667d0d8992e610c89",
    "items": [
      {
        "ingredient_name": "Greek Yogurt",
        "amount": "1 cup",
        "price": 3.99,
        "affiliate_link": "https://example.com/greek-yogurt"
      },
      {
        "ingredient_name": "Granola",
        "amount": "1/4 cup",
        "price": 2.49,
        "affiliate_link": "https://example.com/granola"
      }
    ],
    "subtotal": 6.48,
    "discount": 0.65,
    "total_price": 5.83,
    "status": "processing",
    "created_at": "2023-06-20T14:25:00Z",
    "updated_at": "2023-06-20T14:30:00Z"
  }
}
```

#### Cancel an Order

```
PUT /orders/:id/cancel
```

**Response:**
```json
{
  "success": true,
  "message": "Order cancelled successfully",
  "order": {
    "id": "60d21b4667d0d8992e610c89",
    "status": "cancelled",
    "updated_at": "2023-06-20T15:00:00Z"
  }
}
```

## Error Responses

All API endpoints return a consistent error format:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": {
      "field": "email",
      "value": null
    }
  }
}
```

### Common Error Codes

- `VALIDATION_ERROR`: Invalid input data
- `AUTHENTICATION_ERROR`: Authentication failed
- `AUTHORIZATION_ERROR`: User not authorized to perform the action
- `NOT_FOUND`: Resource not found
- `SERVER_ERROR`: Internal server error

## Rate Limiting

The API implements rate limiting to prevent abuse:

- 100 requests per minute for authenticated users
- 20 requests per minute for unauthenticated users

When the rate limit is exceeded, the API returns a 429 Too Many Requests response:

```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests, please try again later",
    "details": {
      "retry_after": 30
    }
  }
}
```

## Versioning

The API uses URL versioning. The current version is v1:

```
https://api.fitfoodie.com/api/v1/meals
```

Future versions will be available at:

```
https://api.fitfoodie.com/api/v2/meals
```
