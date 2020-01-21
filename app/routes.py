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

        if ('owner' in data) and ('name' in data) and ('exercises' in data):            
            service = WorkoutService()
            response = jsonify(service.add_workout(data))
            response.status_code = 200

            return response
        else:
            raise Exception("Wrong values passed to the endpoint")
    except Exception as error:
        response = jsonify(error)
        response.status_code = 400
        return response


@app.route('/getworkoutfrom/', methods=['GET'])
def get_workout_from():
    owner = request.args.get('owner')
    if owner is not None and owner:
        service = WorkoutService()
        response = jsonify(service.get_workout_from(owner))
        response.status_code = 200
        return response
    else:
        return 'Bad request. Need to informe owner of the workout', 400
