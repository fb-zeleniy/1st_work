import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешить запросы из других источников

CITY = "Almaty"
# WTTR_URL = f"http://wttr.in/{CITY}?format=j1"


def get_weather(city):
    weather_url = f"http://wttr.in/{city}?format=j1"
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()
        current_data = data['current_condition'][0]
        return {
            "city": city,
            "temperature": current_data["temp_C"],
            "condition": current_data["weatherDesc"][0]["value"],
            "feels_like": current_data["FeelsLikeC"],
            "humidity": current_data["humidity"],
        }
    else:
        return {"error": f"Ошибка: {response.status_code}, {response.text}"}


@app.route('/api/weather', methods=['GET'])
def weather_api():
    weather_data = get_weather(CITY)
    return jsonify(weather_data)


if __name__ == "__main__":
    app.run(debug=True)