from flask import Blueprint, request, jsonify
from models import db, User, Influencer
from flask_jwt_extended import jwt_required, get_jwt_identity

influencers_bp = Blueprint('influencers', __name__)

@influencers_bp.route('/', methods=['GET'])
def get_influencers():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    specialty = request.args.get('specialty')
    
    query = Influencer.query
    
    if specialty:
        query = query.filter(Influencer.specialty.like(f'%{specialty}%'))
    
    influencers = query.order_by(Influencer.created_at.desc()).paginate(page=page, per_page=per_page)
    
    return jsonify({
        'influencers': [influencer.to_dict() for influencer in influencers.items],
        'total': influencers.total,
        'pages': influencers.pages,
        'current_page': influencers.page
    }), 200

@influencers_bp.route('/<int:influencer_id>', methods=['GET'])
def get_influencer(influencer_id):
    influencer = Influencer.query.get(influencer_id)
    
    if not influencer:
        return jsonify({'error': 'Influencer not found'}), 404
    
    return jsonify(influencer.to_dict()), 200

@influencers_bp.route('/profile', methods=['POST'])
@jwt_required()
def create_influencer_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    if Influencer.query.filter_by(user_id=user_id).first():
        return jsonify({'error': 'Influencer profile already exists'}), 400
    
    data = request.get_json()
    
    # Create influencer profile
    influencer = Influencer(
        user_id=user_id,
        specialty=data.get('specialty', ''),
        social_media_links=data.get('social_media_links', '{}')  # JSON string
    )
    
    # Update user to be an influencer
    user.is_influencer = True
    
    db.session.add(influencer)
    db.session.commit()
    
    return jsonify({
        'message': 'Influencer profile created successfully',
        'influencer': influencer.to_dict()
    }), 201

@influencers_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_influencer_profile():
    user_id = get_jwt_identity()
    
    influencer = Influencer.query.filter_by(user_id=user_id).first()
    
    if not influencer:
        return jsonify({'error': 'Influencer profile not found'}), 404
    
    data = request.get_json()
    
    # Update influencer fields
    if 'specialty' in data:
        influencer.specialty = data['specialty']
    if 'social_media_links' in data:
        influencer.social_media_links = data['social_media_links']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Influencer profile updated successfully',
        'influencer': influencer.to_dict()
    }), 200

@influencers_bp.route('/follow/<int:influencer_id>', methods=['POST'])
@jwt_required()
def follow_influencer(influencer_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    influencer = Influencer.query.get(influencer_id)
    
    if not influencer:
        return jsonify({'error': 'Influencer not found'}), 404
    
    if influencer in user.following:
        return jsonify({'error': 'Already following this influencer'}), 400
    
    user.following.append(influencer)
    db.session.commit()
    
    return jsonify({
        'message': 'Now following influencer'
    }), 200

@influencers_bp.route('/unfollow/<int:influencer_id>', methods=['DELETE'])
@jwt_required()
def unfollow_influencer(influencer_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    influencer = Influencer.query.get(influencer_id)
    
    if not influencer:
        return jsonify({'error': 'Influencer not found'}), 404
    
    if influencer not in user.following:
        return jsonify({'error': 'Not following this influencer'}), 400
    
    user.following.remove(influencer)
    db.session.commit()
    
    return jsonify({
        'message': 'Unfollowed influencer'
    }), 200
