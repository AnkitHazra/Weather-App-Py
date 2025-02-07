# Weather Reporter Project

This project fetches real-time weather data for a given city and provides an audio and text-based weather report. The user inputs the name of the city, and the program uses the OpenWeatherMap API to get the weather details, such as temperature, humidity, and weather conditions. The weather report is then printed to the console and spoken aloud using the `pyttsx3` library.

## Features

- Fetches weather data for any city worldwide.
- Converts the temperature from Kelvin to Celsius.
- Provides information on the weather condition, temperature, and sky description.
- Reads out the weather information using text-to-speech.
- Handles errors for invalid city names or unexpected API responses.

## Requirements

The project requires the following libraries:

- **`requests`**: To fetch weather data from the OpenWeatherMap API.
- **`json`**: For parsing the response data.
- **`pyttsx3`**: For text-to-speech functionality.

You can install the required libraries using pip:

```bash
pip install requests pyttsx3
