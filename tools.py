import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_current_weather(city):
    if not OPENWEATHER_API_KEY:
        return "OpenWeather API key missing."

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    r = requests.get(url).json()

    if "main" not in r:
        return "Weather not found."

    return f"{city}: {r['weather'][0]['description']}, {r['main']['temp']}°C"


def get_weather_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    r = requests.get(url).json()

    if "list" not in r:
        return "Forecast not available."

    return "\n".join([f"{f['dt_txt']} → {f['main']['temp']}°C" for f in r["list"][:5]])


def get_flights(city):
    return f"Flights to {city}: Indigo ₹8k | Air India ₹10k"


def get_hotels(city):
    return f"Hotels in {city}: Taj ₹12k/night | Budget ₹3k/night"