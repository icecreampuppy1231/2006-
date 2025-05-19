# 2006-
portfolio

# Flask JWT Authentication Demo

This project implements a simple Flask web application demonstrating a secure login system using JSON Web Tokens (JWT), strong password hashing, and security headers via Flask-Talisman.

## Features
- User registration with Argon2 password hashing
- Login endpoint returning a JWT access token
- Protected route requiring valid JWT
- Flask-Talisman to enforce security headers (CSP, HSTS, etc.)

## Getting Started
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
export JWT_SECRET_KEY="your-very-secret-key"
flask run
```

Then use `POST /register` and `POST /login` to interact.
