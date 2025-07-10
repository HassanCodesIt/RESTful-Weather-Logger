from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

# WeatherAPI.com credentials
WEATHERAPI_KEY = "691e916ce1f14924a9a165111251007"

# List of default cities
DEFAULT_CITIES = ["London", "New York", "Tokyo", "Paris", "Sydney"]

def fetch_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHERAPI_KEY}&q={city}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return {"city": city.title(), "error": f"API error: {response.status_code}"}
        data = response.json()
        current = data.get("current", {})
        condition = current.get("condition", {})
        location = data.get("location", {})
        return {
            "city": location.get("name", city.title()),
            "timestamp": current.get("last_updated"),
            "description": condition.get("text"),
            "icon": "https:" + condition.get("icon") if condition.get("icon") else None,
            "temperature": current.get("temp_c"),
            "humidity": current.get("humidity"),
            "wind_speed": current.get("wind_kph"),
            "cloudiness": current.get("cloud"),
            "error": None
        }
    except Exception as e:
        return {"city": city.title(), "error": str(e)}

@app.route("/", methods=["GET"])
def index():
    weather_logs = [fetch_weather(city) for city in DEFAULT_CITIES]
    return render_template("index.html", weather_logs=weather_logs)

if __name__ == "__main__":
    app.run(debug=True) 