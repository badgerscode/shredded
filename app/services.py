from app import db
from app.models import Workout, Exercise


class WorkoutService(object):
    def get_workout_from(self, owner):
        workouts = Workout.query.filter_by(owner=owner).outerjoin(Workout.exercises).all()
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
        return data