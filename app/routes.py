from app import app, request, jsonify, db
from app.models import Workout

@app.route('/')
@app.route('/hello')
def helloworld():
    return "Hello to Schredded"

@app.route('/addworkout', methods=['POST'])
def add_workout():
    data = request.get_json()
    owner = data["owner"]
    workouts = Workout.query.filter(owner == owner).all()
    if(len(workouts) > 0):
        return "Workout already exist", 400
    else:
        workout = Workout(owner = data["owner"], name = data["name"])    
        db.session.add(workout)
        db.session.commit()
        return jsonify(workout)