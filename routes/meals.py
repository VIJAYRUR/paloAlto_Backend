from flask import Blueprint, request, jsonify
from models import db, Meal, User, Influencer
from flask_jwt_extended import jwt_required, get_jwt_identity

meals_bp = Blueprint('meals', __name__)

@meals_bp.route('/', methods=['GET'])
def get_meals():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    tag = request.args.get('tag')
    influencer_id = request.args.get('influencer_id', type=int)
    
    query = Meal.query
    
    if tag:
        query = query.filter(Meal.tags.like(f'%{tag}%'))
    
    if influencer_id:
        query = query.filter_by(influencer_id=influencer_id)
    
    meals = query.order_by(Meal.created_at.desc()).paginate(page=page, per_page=per_page)
    
    return jsonify({
        'meals': [meal.to_dict() for meal in meals.items],
        'total': meals.total,
        'pages': meals.pages,
        'current_page': meals.page
    }), 200

@meals_bp.route('/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    meal = Meal.query.get(meal_id)
    
    if not meal:
        return jsonify({'error': 'Meal not found'}), 404
    
    return jsonify(meal.to_dict()), 200

@meals_bp.route('/', methods=['POST'])
@jwt_required()
def create_meal():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user or not user.is_influencer:
        return jsonify({'error': 'Only influencers can create meals'}), 403
    
    influencer = Influencer.query.filter_by(user_id=user_id).first()
    
    if not influencer:
        return jsonify({'error': 'Influencer profile not found'}), 404
    
    data = request.get_json()
    
    # Check if required fields are present
    if not all(k in data for k in ('title', 'description')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Create new meal
    meal = Meal(
        influencer_id=influencer.id,
        title=data['title'],
        description=data['description'],
        image_url=data.get('image_url', ''),
        ingredients=data.get('ingredients', '[]'),  # JSON string
        instructions=data.get('instructions', ''),
        prep_time=data.get('prep_time'),
        cook_time=data.get('cook_time'),
        servings=data.get('servings'),
        calories=data.get('calories'),
        protein=data.get('protein'),
        carbs=data.get('carbs'),
        fat=data.get('fat'),
        tags=','.join(data.get('tags', [])),
        affiliate_links=data.get('affiliate_links', '[]')  # JSON string
    )
    
    db.session.add(meal)
    db.session.commit()
    
    return jsonify({
        'message': 'Meal created successfully',
        'meal': meal.to_dict()
    }), 201

@meals_bp.route('/<int:meal_id>', methods=['PUT'])
@jwt_required()
def update_meal(meal_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user or not user.is_influencer:
        return jsonify({'error': 'Only influencers can update meals'}), 403
    
    meal = Meal.query.get(meal_id)
    
    if not meal:
        return jsonify({'error': 'Meal not found'}), 404
    
    influencer = Influencer.query.filter_by(user_id=user_id).first()
    
    if not influencer or meal.influencer_id != influencer.id:
        return jsonify({'error': 'You can only update your own meals'}), 403
    
    data = request.get_json()
    
    # Update meal fields
    if 'title' in data:
        meal.title = data['title']
    if 'description' in data:
        meal.description = data['description']
    if 'image_url' in data:
        meal.image_url = data['image_url']
    if 'ingredients' in data:
        meal.ingredients = data['ingredients']
    if 'instructions' in data:
        meal.instructions = data['instructions']
    if 'prep_time' in data:
        meal.prep_time = data['prep_time']
    if 'cook_time' in data:
        meal.cook_time = data['cook_time']
    if 'servings' in data:
        meal.servings = data['servings']
    if 'calories' in data:
        meal.calories = data['calories']
    if 'protein' in data:
        meal.protein = data['protein']
    if 'carbs' in data:
        meal.carbs = data['carbs']
    if 'fat' in data:
        meal.fat = data['fat']
    if 'tags' in data:
        meal.tags = ','.join(data['tags'])
    if 'affiliate_links' in data:
        meal.affiliate_links = data['affiliate_links']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Meal updated successfully',
        'meal': meal.to_dict()
    }), 200

@meals_bp.route('/<int:meal_id>', methods=['DELETE'])
@jwt_required()
def delete_meal(meal_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user or not user.is_influencer:
        return jsonify({'error': 'Only influencers can delete meals'}), 403
    
    meal = Meal.query.get(meal_id)
    
    if not meal:
        return jsonify({'error': 'Meal not found'}), 404
    
    influencer = Influencer.query.filter_by(user_id=user_id).first()
    
    if not influencer or meal.influencer_id != influencer.id:
        return jsonify({'error': 'You can only delete your own meals'}), 403
    
    db.session.delete(meal)
    db.session.commit()
    
    return jsonify({
        'message': 'Meal deleted successfully'
    }), 200

@meals_bp.route('/favorite/<int:meal_id>', methods=['POST'])
@jwt_required()
def favorite_meal(meal_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    meal = Meal.query.get(meal_id)
    
    if not meal:
        return jsonify({'error': 'Meal not found'}), 404
    
    if meal in user.favorite_meals:
        return jsonify({'error': 'Meal already favorited'}), 400
    
    user.favorite_meals.append(meal)
    db.session.commit()
    
    return jsonify({
        'message': 'Meal favorited successfully'
    }), 200

@meals_bp.route('/favorite/<int:meal_id>', methods=['DELETE'])
@jwt_required()
def unfavorite_meal(meal_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    meal = Meal.query.get(meal_id)
    
    if not meal:
        return jsonify({'error': 'Meal not found'}), 404
    
    if meal not in user.favorite_meals:
        return jsonify({'error': 'Meal not in favorites'}), 400
    
    user.favorite_meals.remove(meal)
    db.session.commit()
    
    return jsonify({
        'message': 'Meal unfavorited successfully'
    }), 200
