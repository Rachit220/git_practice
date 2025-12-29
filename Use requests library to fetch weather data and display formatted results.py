import requests

API_KEY = "4e73117b7487faa5bd77a31884b75119"
CITY = "Ahmedabad"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # Celsius
    }

    response = requests.get(BASE_URL, params=params)

    # ERROR HANDLING
    if response.status_code != 200:
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return

    # SUCCESS CASE
    data = response.json()

    weather_info = {
        "City": data["name"],
        "Country": data["sys"]["country"],
        "Temperature": data["main"]["temp"],
        "Feels Like": data["main"]["feels_like"],
        "Humidity": data["main"]["humidity"],
        "Weather": data["weather"][0]["description"].title(),
        "Wind Speed": data["wind"]["speed"]
    }

    display_weather(weather_info)

def display_weather(info):
    print("\n WEATHER REPORT ")
    print("-" * 30)
    for key, value in info.items():
        print(f"{key:15}: {value}")
    print("-" * 30)

if __name__ == "__main__":
    get_weather(CITY)

