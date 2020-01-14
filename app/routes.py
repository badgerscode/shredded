from app import app, request, jsonify

@app.route('/')
@app.route('/hello')
def helloworld():
    return "Hello to Schredded"

@app.route('/addworkout', methods=['POST'])
def add_workout():
    data = request.get_json()
    
    return jsonify(data)