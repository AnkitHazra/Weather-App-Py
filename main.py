import requests
import json
import pyttsx3


engine = pyttsx3.init()


city = input("Enter the name of the city: ")


url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dc00e7befacd6fa343aa2156480376aa"


try:
    r = requests.get(url)
    r.raise_for_status()
    wDic = json.loads(r.text)


    temp_k = wDic["main"]["temp"]
    temp_feels_like = wDic["main"]["feels_like"]
    temp_c = int(temp_k - 273)
    temp_feels_like_c = int(temp_feels_like - 273)
    wth = wDic["weather"][0]["main"]
    wth_sky = wDic["weather"][0]["description"]
    max_t = int(wDic["main"]["temp_max"]) - 273
    min_t = int(wDic["main"]["temp_min"]) - 273


    print(f"The temperature of {city} is {temp_c}°C.")
    print(f"The temperature of {city} feels like {temp_feels_like_c}°C.")
    print(f"The weather is {wth} and the sky is {wth_sky}.")
    print(f"The minimum temperature is {min_t}°C and the maximum temperature is {max_t}°C.")


    engine.say(f"The temperature of {city} is {temp_c} degrees Celsius.")
    engine.runAndWait()
    engine.say(f"It feels like {temp_feels_like_c} degrees Celsius.")
    engine.runAndWait()
    engine.say(f"The weather is {wth} and the sky is {wth_sky}.")
    engine.runAndWait()
    engine.say(f"The minimum temperature is {min_t} degrees Celsius and the maximum is {max_t} degrees Celsius.")
    engine.runAndWait()

except requests.exceptions.HTTPError:
    print("Error: Unable to fetch weather data. Please check the city name.")
    engine.say("Unable to fetch weather data. Please check the city name.")
    engine.runAndWait()

except KeyError:
    print("Error: Unexpected data format received from the API.")
    engine.say("Unexpected data format received from the API.")
    engine.runAndWait()

except Exception as e:
    print(f"An error occurred: {e}")
    engine.say("An unexpected error occurred.")
    engine.runAndWait()
