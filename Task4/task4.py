
from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Missing name or email"}), 400

    users.append({
        "name": data['name'],
        "email": data['email']
    })

    return jsonify({'message': 'User added successfully'}), 201

@app.route('/users/<int:index>', methods=['PUT'])
def update_user(index):

    if index < 0 or index >= len(users):
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()

    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Missing name or email"}), 400

    users[index] = {
        "name": data['name'],
        "email": data['email']
    }

    return jsonify({'message': 'User updated successfully'}), 200

@app.route('/users/<int:index>', methods=['DELETE'])
def delete_user(index):

    if index < 0 or index >= len(users):
        return jsonify({'error': 'User not found'}), 404


    users.pop(index)

    return jsonify({'message': 'User deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
