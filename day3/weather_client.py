
import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 11.0168,
    "longitude": 76.9558,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

headers = {
    "Accept": "application/json"
}

try:
    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    current = data["current"]

    print("===== COIMBATORE WEATHER =====")
    print(f"Temperature: {current['temperature_2m']} °C")
    print(f"Humidity: {current['relative_humidity_2m']} %")
    print(f"Wind Speed: {current['wind_speed_10m']} km/h")
    print(f"Updated at: {current['time']}")

except requests.exceptions.Timeout:
    print("Error: The request took too long.")

except requests.exceptions.HTTPError as error:
    print(f"HTTP Error: {error}")

except requests.exceptions.RequestException as error:
    print(f"Network Error: {error}")

except (KeyError, ValueError) as error:
    print(f"Error reading weather data: {error}")
