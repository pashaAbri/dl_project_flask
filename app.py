from flask import Flask
from routes import bp as bp_routes

app = Flask(__name__)

# register the routes blueprint
app.register_blueprint(bp_routes)


if __name__ == '__main__':
  app.run(debug=True)