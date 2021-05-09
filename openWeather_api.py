import requests , json
import os

def openWeatherApi():

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    URL = BASE_URL + "q=" + "Surat" + "&appid=" + "fb83eb2363f2411f83bf1d406d1b185f"

    strt = ""
    response = requests.get(URL)
    if response.status_code == 200:
      # getting data in the json format
      data = response.json()
      # getting the main dict block
      main = data['main']
      # getting temperature
      temperature = main['temp']
      # getting the humidity
      humidity = main['humidity']
      # getting the pressure
      pressure = main['pressure']
      # weather report
      report = data['weather']
      strt = strt + "------------ Surat -------------" + "\n"
      strt = strt + "temperature = " + str(temperature) + "\n"
      strt = strt + "humidity = " + str(humidity) + "\n"
      strt = strt + "pressure = " + str(pressure) + "\n"
      strt = strt + "weather report = " + str(report[0]['description']) + "\n"
      return strt
    else:
      # showing the error message
      strt = "Error in the HTTP request"
      return strt

  
