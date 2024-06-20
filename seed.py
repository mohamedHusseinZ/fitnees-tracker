from app import create_app, db
from model import User, Workout, Activity, Goal, Progress, Nutrition, Meal, Achievement
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

app = create_app()

with app.app_context():
    # Drop and recreate the database tables
    db.drop_all()
    db.create_all()

    # Create sample users
    user1 = User(username='john_doe', email='john@example.com', password_hash=generate_password_hash('password123'))
    user2 = User(username='jane_doe', email='jane@example.com', password_hash=generate_password_hash('password123'))

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Create sample workouts
    workout1 = Workout(user_id=user1.user_id, workout_date=datetime.utcnow().date(), workout_type='Running', duration=30, calories_burned=300, notes='Morning run')
    workout2 = Workout(user_id=user2.user_id, workout_date=datetime.utcnow().date(), workout_type='Cycling', duration=45, calories_burned=450, notes='Evening cycling')

    db.session.add(workout1)
    db.session.add(workout2)
    db.session.commit()

    # Create sample activities
    activity1 = Activity(user_id=user1.user_id, activity_date=datetime.utcnow().date(), activity_type='Yoga', duration=60, notes='Morning yoga session')
    activity2 = Activity(user_id=user2.user_id, activity_date=datetime.utcnow().date(), activity_type='Swimming', duration=30, notes='Afternoon swim')

    db.session.add(activity1)
    db.session.add(activity2)
    db.session.commit()

    # Create sample goals
    goal1 = Goal(user_id=user1.user_id, goal_type='Weight Loss', target_value=5, current_value=1, start_date=datetime.utcnow().date(), end_date=(datetime.utcnow() + timedelta(days=30)).date(), status='active')
    goal2 = Goal(user_id=user2.user_id, goal_type='Muscle Gain', target_value=3, current_value=1, start_date=datetime.utcnow().date(), end_date=(datetime.utcnow() + timedelta(days=30)).date(), status='active')

    db.session.add(goal1)
    db.session.add(goal2)
    db.session.commit()

    # Create sample progress entries
    progress1 = Progress(user_id=user1.user_id, goal_id=goal1.goal_id, progress_date=datetime.utcnow().date(), progress_value=1)
    progress2 = Progress(user_id=user2.user_id, goal_id=goal2.goal_id, progress_date=datetime.utcnow().date(), progress_value=1)

    db.session.add(progress1)
    db.session.add(progress2)
    db.session.commit()

    # Create sample nutrition entries
    nutrition1 = Nutrition(user_id=user1.user_id, date=datetime.utcnow().date(), total_calories=2000, total_protein=150, total_carbs=250, total_fats=70, notes='Balanced diet')
    nutrition2 = Nutrition(user_id=user2.user_id, date=datetime.utcnow().date(), total_calories=2500, total_protein=200, total_carbs=300, total_fats=80, notes='High protein diet')

    db.session.add(nutrition1)
    db.session.add(nutrition2)
    db.session.commit()

    # Create sample meals
    meal1 = Meal(user_id=user1.user_id, nutrition_id=nutrition1.nutrition_id, meal_time=datetime.utcnow(), meal_type='Breakfast', calories=500, protein=20, carbs=60, fats=20, description='Oatmeal and eggs')
    meal2 = Meal(user_id=user2.user_id, nutrition_id=nutrition2.nutrition_id, meal_time=datetime.utcnow(), meal_type='Lunch', calories=700, protein=40, carbs=80, fats=25, description='Chicken and rice')

    db.session.add(meal1)
    db.session.add(meal2)
    db.session.commit()

    # Create sample achievements
    achievement1 = Achievement(user_id=user1.user_id, achievement_date=datetime.utcnow().date(), description='Completed first 5K run', social_share=True)
    achievement2 = Achievement(user_id=user2.user_id, achievement_date=datetime.utcnow().date(), description='Swam 100 laps', social_share=False)

    db.session.add(achievement1)
    db.session.add(achievement2)
    db.session.commit()

    print('Database seeded successfully!')
