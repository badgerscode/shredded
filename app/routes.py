from app import app

@app.route('/')
@app.route('/hello')
def helloworld():
    return "Hello to Schredded"