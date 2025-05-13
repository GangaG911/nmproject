from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('first.html')

@app.route('/second')
def second():
    return render_template('second.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sunlight = data.get('sunlight')
    wind = data.get('wind')
    rainfall = data.get('rainfall')

    if sunlight > 70 and rainfall < 20:
        result = "Recommended Source: Solar"
    elif wind > 15:
        result = "Recommended Source: Wind"
    else:
        result = "Recommended Source: Grid"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
