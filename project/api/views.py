# project/api/views.py
from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc
from project import db
from project.api.models import User

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@users_blueprint.route('/users', methods=['POST'])
def add_user():
    # 获取POST的数据
    post_data = request.get_json()
    email = post_data.get('email')
    user = User(username=post_data.get('username'), email=email)
    db.session.add(user)
    db.session.commit()
    response_data = {
        'status': 'success',
        'message': '%s was added!' % email
    }
    return jsonify(response_data), 201
