import argparse
from configparser import ConfigParser


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
    read_user_cli_args()
