from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize SQLAlchemy and Migrate without an app instance
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

    # Initialize SQLAlchemy and Migrate with the app instance
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models to ensure they are registered with SQLAlchemy
    with app.app_context():
        from model import User, Workout, Activity, Goal, Progress, Nutrition, Meal, Achievement

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

