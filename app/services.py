from app import db
from app.models import Workout, Exercise


class WorkoutService(object):
    def get_workout_from(self, owner):
        workouts = Workout.query.outerjoin(Workout.exercises).filter(Workout.owner == owner).all()
        data = []
        for workout in workouts:
            dict_workout = {
                'id': workout.id,
                'owner': workout.owner,
                'name': workout.name
            }

            exercises = list()
            for exercise in workout.exercises: 
                exercises.append(exercise.to_dictionary())

            dict_workout['exercises'] = exercises
            data.append(dict_workout)
        return data

    def add_workout(self, json_dict):
        workout = Workout(owner=json_dict['owner'], name=json_dict['name'])
        db.session.add(workout)
        
        exercises = json_dict["exercises"]
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

        return json

    def get_exercises_from_workout(self, workout_id):
        workout = Workout.query.filter(Workout.id == workout_id).first()
        if workout:
            exercises = workout.exercises.all()
            json = []
            for exercise in exercises:
                json.append(exercise.to_dictionary())
            
            return json
        else:
            return []
