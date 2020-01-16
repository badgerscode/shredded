from app import app, request, jsonify, db
from app.services import WorkoutService
from app.models import Workout, Exercise

@app.route('/')
@app.route('/hello')
def helloworld():
    return "Hello to Schredded"

@app.route('/addworkout', methods=['POST'])
def add_workout():    
    try:
        data = request.get_json()    
        
        workout = Workout(owner = data["owner"], name = data["name"])    
        db.session.add(workout)
        
        exercises = data["exercises"]
        for element in exercises:
            exercise = Exercise(description = element["description"], workouts = workout)
            db.session.add(exercise)
        
        db.session.commit()    
        print(workout.exercises.all())

        json = {
            'id': workout.id,
            'owner': workout.owner,
            'name': workout.name
        }

        response = jsonify(json)
        response.status_code = 200    
        
        return response
    except Exception as error:
        response = jsonify(error)
        response.status_code = 500
        return response

@app.route('/getworkoutfrom/', methods = ['GET'])
def get_workout_from():
    owner = request.args.get('owner')
    if owner is not None and owner :       
        service = WorkoutService()
        response = jsonify(service.get_workout_from(owner))
        response.status_code = 200
        return response
    else:    
        return 'Bad request. Need to informe owner of the workout', 400
