from flask import Blueprint, request, jsonify
from app.models import db, User
from app.schemas import UserSchema

auth = Blueprint('auth', __name__)
reports = Blueprint('reports', __name__)

@auth.route('/signup', methods=['POST'])
def signup():
    schema = UserSchema()

    try:
        user_data = schema.load(request.json)
    except Exception as e:
        return jsonify({'message': 'Invalid input', 'errors': str(e)}), 400

    # Check if username already exists
    if User.query.filter_by(username=user_data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400

    # Create new user
    user = User(username=user_data['username'], password=user_data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    schema = UserSchema()

    try:
        user_data = schema.load(request.json)
    except Exception as e:
        return jsonify({'message': 'Invalid input', 'errors': str(e)}), 400

    user = User.query.filter_by(username=user_data['username']).first()

    if not user or user.password != user_data['password']:
        return jsonify({'message': 'Invalid username or password'}), 401

    # Handle authentication and return response

@reports.route('/api/reports', methods=['GET'])
def get_reports():
    # Handle search functionality and return reports

    return jsonify(reports), 200
