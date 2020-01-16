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