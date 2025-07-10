# RESTful Weather Logger

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![REST API](https://img.shields.io/badge/REST%20API-Enabled-brightgreen)](https://en.wikipedia.org/wiki/Representational_state_transfer)
[![RapidAPI](https://img.shields.io/badge/RapidAPI-Weather-blue?logo=rapidapi)](https://rapidapi.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Project Overview

**RESTful Weather Logger** is a full-stack web application that demonstrates the power of REST APIs. It allows users to view real-time weather data for multiple cities, fetched from a third-party weather API via RapidAPI. The backend is built with Flask and exposes its own RESTful endpoints, making it a perfect project to showcase on your resume as a REST API implementation.

---

## 🛠️ Tech Stack

- **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
- **Frontend:** HTML5, CSS3 (Jinja2 templating)
- **REST API Consumption:** [RapidAPI Weather API](https://rapidapi.com/)
- **REST API Exposure:** Custom Flask endpoints returning JSON
- **Other:** Requests, Jinja2

---

## 📦 Features

- **RESTful API Endpoints:**  
  - `GET /api/weather` — Get weather data for all default cities (JSON)
  - `GET /api/weather/<city>` — Get weather data for a specific city (JSON)
- **Modern Web UI:**  
  - Responsive, clean interface
  - Weather icons, temperature, humidity, wind, and more
- **Error Handling:**  
  - Graceful handling of API errors and invalid cities
- **Easy Configuration:**  
  - Change default cities in one place
- **Ready for Deployment:**  
  - Simple to run locally or deploy to the cloud

---

## 📖 API Documentation

### `GET /api/weather`
Returns weather data for all default cities.

**Response:**
```json
[
  {
    "city": "London",
    "timestamp": "2025-07-10 20:37:36",
    "description": "Few clouds",
    "icon": "https://openweathermap.org/img/wn/02d@2x.png",
    "temperature": 20.5,
    "humidity": 60,
    "wind_speed": 3.2,
    "cloudiness": 21,
    "error": null
  },
  ...
]
```

### `GET /api/weather/<city>`
Returns weather data for a specific city.

**Example:**  
`GET /api/weather/London`

---

## 🚦 Quick Start

1. **Clone the repo:**
   ```bash
   git clone https://github.com/HassanCodesIt/RESTful-Weather-Logger.git
   cd RESTful-Weather-Logger
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your RapidAPI credentials in `app.py`:**
   ```python
   RAPIDAPI_KEY = "your_rapidapi_key"
   RAPIDAPI_HOST = "weather-api167.p.rapidapi.com"
   ```

4. **Run the app:**
   ```bash
   python app.py
   ```

5. **Open in your browser:**  
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🧩 Project Structure

```
RESTful-Weather-Logger/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## 📝 How to Use

- Visit the homepage to see weather for default cities.
- Use `/api/weather` to get all weather data as JSON (for Postman, curl, or frontend apps).
- Use `/api/weather/<city>` to get weather for a specific city as JSON.

---

## 📚 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Credits

- [RapidAPI Weather API](https://rapidapi.com/)
- [Flask](https://flask.palletsprojects.com/)
- [OpenWeatherMap Icons](https://openweathermap.org/weather-conditions)

---

> _Showcase your REST API skills with this project!_  
> _Perfect for resumes, portfolios, and learning full-stack development._ 