# Import flask dependencies
from flask import Blueprint, jsonify, request, abort
from flask_login import current_user
from flask_security import auth_required, anonymous_user_required
from flask_security.utils import hash_password, login_user, verify_password, logout_user
from api.user.models import Role, RolesUsers

import hashlib

# Import the database object from the main app module
from api import db, security

# Import User models and schemas
from api.user.schemas import SignupInputSchema, SigninInputSchema, UserSchema, ProfileUpdateSchema

# Mount the user_module on '/api'
user_module = Blueprint('user_api', __name__, url_prefix='/api')

# Signup
@anonymous_user_required
@user_module.route('/signup', methods=['POST'])
def signup():
    data = {k: v.strip() for k, v in request.get_json().items()}
    schema = SignupInputSchema()
    errors = schema.validate(data)

    if errors:
        # Validation Error
        abort(422, str(errors))
    elif security.datastore.find_user(email=data['email']):
        # User already Exists
        abort(409, 'User already exists')
    else:
        uid = hashlib.sha256(data['roll_number'].encode('utf-8')).hexdigest()
        user = security.datastore.create_user(first_name=data['first_name'],
                                    last_name=data['last_name'],
                                    email=data['email'],
                                    roll_number=data['roll_number'],
                                    fs_uniquifier=uid,
                                    password=hash_password(data['password']))
        db.session.commit()
        
        role = Role.query.filter_by(name='Student').first()
        role_user=RolesUsers(user_id=user.id, role_id=role.id)
        db.session.add(role_user)
        db.session.commit()
        
        return jsonify({'status': 'OK', 'message': 'Signup successful'}), 201
        
# Signin
@user_module.route('/signin', methods=['POST'])
@anonymous_user_required
def signin():
    data = {k: v.strip() for k, v in request.get_json().items()}
    schema = SigninInputSchema()
    errors = schema.validate(data)

    if errors:
        # Validation Error
        abort(422, str(errors))
    else:
        user = security.datastore.find_user(email=data['email'])
        # return data['password'], 200
        if user and verify_password(data['password'], user.password):
            login_user(user)
            return jsonify({'status': 'OK', 'message': 'Signin successful', 'auth_token': user.get_auth_token()}), 201
        else:
            # Bad Password or user doesn't exist
            abort(401, 'Authentication failure')

# Show current user
@user_module.route('/profile', methods=['GET'])
@auth_required('token', 'session')
def show():
    user = current_user
    # schema = UserSchema()
    # return schema.dump(user)
    output = {
        "email": user.email,
        "first_name": user.first_name,
        "id": user.id,
        "last_name": user.last_name,
        "roll_number": user.roll_number,
        "role_id": current_user.roles[0].id
    }
    return jsonify(output)

# Signout
@user_module.route('/signout', methods=['POST'])
@auth_required('token', 'session')
def signout():
    logout_user()
    return jsonify({'status': 'OK', 'message': 'Signout sucessful'}), 204

# Profile Update
@user_module.route('/profile/update', methods=['PUT'])
@auth_required('token', 'session')
def update():
    data = {k: v.strip() for k, v in request.get_json().items()}
    schema = ProfileUpdateSchema()
    errors = schema.validate(data)

    if errors:
        # Validation Error
        abort(422, str(errors))
    else:
        user = current_user
        user.first_name=data['first_name']
        user.last_name=data['last_name']
        user.email=data['email']
        user.password=hash_password(data['password'])
        db.session.commit()
        return jsonify({'status': 'OK', 'message': 'Update sucessful'}), 204