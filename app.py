from flask import Flask
from flask_cors import CORS

from routes import bp as bp_routes

app = Flask(__name__)

# List of allowed origins
allowed_origins = [
    "https://tlkrizdks0.execute-api.us-east-1.amazonaws.com",
]

CORS(app)
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

# register the routes blueprint
app.register_blueprint(bp_routes)


if __name__ == '__main__':
  app.run(debug=True)