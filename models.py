from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Association table for user favorites
user_favorites = db.Table('user_favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('meal_id', db.Integer, db.ForeignKey('meals.id'), primary_key=True)
)

# Association table for user following influencers
user_following = db.Table('user_following',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('influencer_id', db.Integer, db.ForeignKey('influencers.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    height = db.Column(db.Float)  # in cm
    weight = db.Column(db.Float)  # in kg
    age = db.Column(db.Integer)
    activity_level = db.Column(db.String(50))
    dietary_preferences = db.Column(db.String(200))  # Comma-separated values
    is_influencer = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    favorite_meals = db.relationship('Meal', secondary=user_favorites, backref=db.backref('favorited_by', lazy='dynamic'))
    following = db.relationship('Influencer', secondary=user_following, backref=db.backref('followers', lazy='dynamic'))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'name': self.name,
            'bio': self.bio,
            'height': self.height,
            'weight': self.weight,
            'age': self.age,
            'activity_level': self.activity_level,
            'dietary_preferences': self.dietary_preferences.split(',') if self.dietary_preferences else [],
            'is_influencer': self.is_influencer,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Influencer(db.Model):
    __tablename__ = 'influencers'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    specialty = db.Column(db.String(100))
    social_media_links = db.Column(db.Text)  # JSON string
    verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref=db.backref('influencer_profile', uselist=False))
    meals = db.relationship('Meal', backref='influencer', lazy='dynamic')
    
    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.to_dict(),
            'specialty': self.specialty,
            'social_media_links': self.social_media_links,  # Frontend will need to parse this JSON
            'verified': self.verified,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Meal(db.Model):
    __tablename__ = 'meals'
    
    id = db.Column(db.Integer, primary_key=True)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencers.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    ingredients = db.Column(db.Text)  # JSON string
    instructions = db.Column(db.Text)
    prep_time = db.Column(db.Integer)  # in minutes
    cook_time = db.Column(db.Integer)  # in minutes
    servings = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    protein = db.Column(db.Float)  # in grams
    carbs = db.Column(db.Float)  # in grams
    fat = db.Column(db.Float)  # in grams
    tags = db.Column(db.String(200))  # Comma-separated values
    affiliate_links = db.Column(db.Text)  # JSON string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'influencer_id': self.influencer_id,
            'influencer': self.influencer.user.name,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
            'ingredients': self.ingredients,  # Frontend will need to parse this JSON
            'instructions': self.instructions,
            'prep_time': self.prep_time,
            'cook_time': self.cook_time,
            'servings': self.servings,
            'calories': self.calories,
            'protein': self.protein,
            'carbs': self.carbs,
            'fat': self.fat,
            'tags': self.tags.split(',') if self.tags else [],
            'affiliate_links': self.affiliate_links,  # Frontend will need to parse this JSON
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
