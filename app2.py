from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and Email are required"}), 400

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        return jsonify({"error": "Invalid email format"}), 400

    return jsonify({
        "message": "Registration Successful",
        "name": name,
        "email": email
    }), 201

if __name__ == "__main__":
    app.run(debug=True)