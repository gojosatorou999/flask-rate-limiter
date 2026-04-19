from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Initialize Limiter
# default_limits: Global limits applied to all routes
# key_func: Identifier for the requester (IP address in this case)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",  # Using in-memory storage for simplicity
)

@app.route("/")
def index():
    return jsonify({
        "message": "Welcome to the Rate Limited API",
        "status": "Running"
    })

@app.route("/ping")
@limiter.limit("5 per minute")  # Specific limit for this route
def ping():
    return jsonify({
        "message": "pong",
        "client_ip": request.remote_addr
    })

@app.route("/slow")
@limiter.limit("1 per minute")
def slow():
    return jsonify({
        "message": "This is a very slow route, limited to 1 request per minute"
    })

# Custom error handler for rate limit exceedance
@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({
        "error": "Rate limit exceeded",
        "message": str(e.description),
        "status_code": 429
    }), 429

if __name__ == "__main__":
    app.run(debug=True)
