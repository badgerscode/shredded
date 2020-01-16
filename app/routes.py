from app import app, request, jsonify, db
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
        workouts = Workout.query.outerjoin(Workout.exercises).filter(owner == owner).all()
        data = []    
        for workout in workouts:
            dict_workout = {
                'id': workout.id,
                'owner': workout.owner,
                'name': workout.name        
            }

            exercises = list()        
            for exercise in workout.exercises:
                dict_exercise = {
                    'id': exercise.id,
                    'description': exercise.description                
                }
                exercises.append(dict_exercise)
            
            dict_workout['exercises'] = exercises
            data.append(dict_workout)
        
        response = jsonify(data)
        response.status_code = 200
        return response
    else:    
        return 'Bad request. Need to informe owner of the workout', 400
