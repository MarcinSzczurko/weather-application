import argparse
from configparser import ConfigParser
from urllib import parse

BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"


def read_user_cli_args():
    """Handles the CLI user interactions.

    Returns:
        argparse.Namespace: Populated namespace object
    """
    parser = argparse.ArgumentParser(
        description="Gets weather and temperature information for a city"
    )
    parser.add_argument("city", nargs="+", type=str, help="Enter the city name")
    parser.add_argument(
        "-f",
        "--fahrenheit",
        action="store_true",
        help="Display the temperature in fahrenheit",
    )
    return parser.parse_args()


def build_weather_query(city_input, fahrenheit=False):
    """Builds the URL for an API request to OpenWeather's Weather API.

    Args:
        city_input (List[str]): Name of a city as collected by argparse
        fahrenheit (bool): Whether or not to use fahrenheit units for temperature

    Returns:
        str: URL formatted for a call to OpenWeather's city name endpoint
    """
    api_key = _get_api_key()
    city_name = " ".join(city_input)
    url_encoded_city_name = parse.quote_plus(city_name)
    units = "imperial" if fahrenheit else "metric"
    url = (
        f"{BASE_WEATHER_API_URL}?q={url_encoded_city_name}"
        f"&units={units}&appid={api_key}"
    )
    return url


def _get_api_key():
    """Fetch the API key from secrets.ini configuration file.

    Configuration file structure:

        [openweather]
        api_key=<YOUR-OPENWEATHER-API-KEY>
    """
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]


if __name__ == "__main__":
    user_args = read_user_cli_args()
    query_url = build_weather_query(user_args.city, user_args.fahrenheit)
