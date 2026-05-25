from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# A simple HTML form
HTML_PAGE = """
    <h2>Weather Predictor</h2>
    <form action="/submit" method="post">
        Humidity: <input type="text" name="humidity"><br><br>
        Wind Speed: <input type="text" name="wind_speed"><br><br>
        <input type="submit" value="Predict Temperature">
    </form>
"""

@app.route('/')
def home():
    return HTML_PAGE

@app.route('/submit', methods=['POST'])
def submit():
    # Get user input from the HTML form
    h = float(request.form['humidity'])
    w = float(request.form['wind_speed'])
    
    # Send it to our FastAPI backend (which runs on port 8000 by default)
   # Change it to look exactly like this:
    fastapi_response = requests.post(
        "http://fastapi_server:8000/api/predict",
        json={"humidity": h, "wind_speed": w}
    )
    
    result = fastapi_response.json()
    return f"<h3>The predicted temperature is: {result['predicted_temperature']} °C</h3>"

if __name__ == '__main__':
    # Run Flask on port 5000
    
    app.run(host="0.0.0.0", port=5000)