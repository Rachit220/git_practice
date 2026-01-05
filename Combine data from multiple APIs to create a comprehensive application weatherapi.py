import requests

def get_weather(city):
    """
    Fetch current temperature for a city using Open-Meteo
    """
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_res = requests.get(geo_url, params={"name": city, "count": 1})
    geo_data = geo_res.json()

    if "results" not in geo_data:
        return None
    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_res = requests.get(
        weather_url,
        params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }
    )
    weather_data = weather_res.json()
    return weather_data["current_weather"]["temperature"]
