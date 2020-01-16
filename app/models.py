from app import db

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    owner = db.Column(db.String(64))
    name = db.Column(db.String(64))
    exercises = db.relationship('Exercise', backref='workouts', lazy='dynamic')
    
    def __repr__(self):
        return '<Workout {} {} {}>'.format(self.id, self.owner, self.name)

    def to_json(self):
        return {            
            'id': self.id,
            'owner': self.owner,
            'name': self.name,
            'exercises': list()
        }

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(100))
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))

    def __repr__(self):
        return '<Exercise {} {}>'.format(self.id, self.description)
    
    def to_dictionary(self):
        return { 'id': self.id, 'description': self.description }