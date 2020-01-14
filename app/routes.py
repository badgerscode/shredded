from app import app, request, jsonify, db
from app.models import Workout

@app.route('/')
@app.route('/hello')
def helloworld():
    return "Hello to Schredded"

@app.route('/addworkout', methods=['POST'])
def add_workout():
    data = request.get_json()    
    workout = Workout(owner = data["owner"], name = data["name"])    
    db.session.add(workout)
    db.session.commit()
    
    json = {
        'id': workout.id,
        'owner': workout.owner,
        'name': workout.name
    }
    response = jsonify(json)
    response.status_code = 200
    return response