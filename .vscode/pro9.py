
from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

API_KEY = '0c7e043cfe1db0fcfe6df0bfc72773e7'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'London').strip()

    if not city:
        return jsonify({"error": "City name cannot be empty"}), 400

    if not API_KEY:
        return jsonify({"error": "Weather API key is not configured"}), 500

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404:
            return jsonify({"error": "City not found"}), 404

        response.raise_for_status()
        data = response.json()

        formatted = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data.get("wind", {}).get("speed", 0)
        }
if __name__ == "__main__":
    app.run(debug=True)
