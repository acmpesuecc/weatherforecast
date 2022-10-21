
import requests
import json
from tkinter import *


def fetch():
    # Enter your API key here
    api_key = "a50d669741efb4e89ada018225a09126"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name
    city_name = i.get()

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print following values
        print(" Temperature (in degree celsius) = " +
              str(round(current_temperature, 3) - 273.15) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in decimal) = " +
              str(current_humidity / 100) +
              "\n description = " +
              str(weather_description))

    else:
        print(" City Not Found ")


root = Tk()
root.title('Weather forecast')
w = Label(root, text='Enter the name of the city to fetch the weather:')
i = Entry(root)
b = Button(root, text='submit', command=fetch)
w.pack()
i.pack()
b.pack()
root.mainloop()
