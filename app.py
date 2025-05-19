app.py


from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from argon2 import PasswordHasher
from flask_talisman import Talisman

app = Flask(__name__)
# Configure JWT
app.config["JWT_SECRET_KEY"] = "your-very-secret-key"
jwt = JWTManager(app)

# Enforce security headers
Talisman(app)

# In-memory user store
ph = PasswordHasher()
users = {}  # format: {username: hashed_password}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users:
        return jsonify({"msg": "Username already exists"}), 400
    # Hash password
    hashed = ph.hash(password)
    users[username] = hashed
    return jsonify({"msg": "User registered"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    hashed = users.get(username)
    if not hashed:
        return jsonify({"msg": "Bad credentials"}), 401
    try:
        ph.verify(hashed, password)
    except:
        return jsonify({"msg": "Bad credentials"}), 401
    # Create JWT
    token = create_access_token(identity=username)
    return jsonify(access_token=token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run()

