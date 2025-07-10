from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

# RapidAPI credentials (new key)
RAPIDAPI_KEY = "417d687e53msh5101a2846c2e74ap1c6754jsne544b3821492"
RAPIDAPI_HOST = "weather-api167.p.rapidapi.com"

# List of default cities
DEFAULT_CITIES = ["London", "New York", "Tokyo", "Paris", "Sydney"]

def fetch_weather(city):
    url = f"https://weather-api167.p.rapidapi.com/api/weather/current?place={city}&units=metric&lang=en&mode=json"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return {"city": city.title(), "error": f"API error: {response.status_code}"}
        data = response.json()
        if not data or ("cod" in data and data["cod"] != 200):
            return {"city": city.title(), "error": "Invalid city or data not found."}
        # Extract relevant fields
        weather = data.get("weather", [{}])[0]
        main = data.get("main", {})
        wind = data.get("wind", {})
        clouds = data.get("clouds", {})
        icon_url = weather.get("icon")
        if icon_url and not icon_url.startswith("http"):
            icon_url = f"https://openweathermap.org/img/wn/{icon_url}@2x.png"
        return {
            "city": city.title(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": weather.get("description", "N/A").title(),
            "icon": icon_url,
            "temperature": main.get("temprature"),
            "humidity": main.get("humidity"),
            "wind_speed": wind.get("speed"),
            "cloudiness": clouds.get("cloudiness"),
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