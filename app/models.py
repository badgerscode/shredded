from app import db

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    owner = db.Column(db.String(64), index = True, unique = True)
    exercises = db.relationship('Exercise', backref='workouts', lazy='dynamic')

    def __repr__(self):
        return '<Workout {}>'.format(self.owner)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(100))
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))

    def __repr__(self):
        return '<Exercise {}>'.format(self.description)
