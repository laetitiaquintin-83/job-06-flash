from flask import Blueprint, jsonify, request
from datetime import datetime

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return jsonify({
        'message': 'Hello Docker + Flask!',
        'timestamp': datetime.now().isoformat()
    })


@main.route('/health')
def health():
    return jsonify({'status': 'ok'})


@main.route('/api/users', methods=['GET'])
def users():
    return jsonify([
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ])


@main.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'error': 'Corps JSON requis'}), 400

    return jsonify({
        'message': 'Utilisateur ajouté avec succès !',
        'user_created': data
    }), 201