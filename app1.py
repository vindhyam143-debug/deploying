from flask import Flask, jsonify

# Create Flask application
app = Flask(__name__)

# Static user data
users = [
    {
        "id": 1,
        "name": "John",
        "email": "john@gmail.com"
    },
    {
        "id": 2,
        "name": "Alice",
        "email": "alice@gmail.com"
    },
    {
        "id": 3,
        "name": "Bob",
        "email": "bob@gmail.com"
    },
    {
        "id": 4,
        "name": "David",
        "email": "david@gmail.com"
    },
    {
        "id": 5,
        "name": "Emma",
        "email": "emma@gmail.com"
    }
]


# API to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# API to get a single user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):

    for user in users:
        if user["id"] == id:
            return jsonify(user)

    return jsonify({
        "message": "User not found"
    })


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)