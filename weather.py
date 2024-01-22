from configparser import ConfigParser


def _get_api_key():
    """Fetch the API key from secrets.ini configuration file.

    Configuration file structure:

        [openweather]
        api_key=<YOUR-OPENWEATHER-API-KEY>
    """
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]
