from flask import Flask, request, jsonify

app = Flask(__name__)

temperature = {"value": 25.5}  
@app.route('/temperature', methods=['GET'])
def get_temp():
    return jsonify(temperature)

@app.route('/temperature', methods=['POST'])
def set_temp():
    data = request.get_json()  
    temperature["value"] = data.get("value")
    return jsonify({"message": "Temperature updated", "new_value": temperature["value"]})

app.run()
