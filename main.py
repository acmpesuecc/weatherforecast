import requests, json
from tkinter import *


def fetch():
    # Enter your API key here
    api_key = "3fab24e55b9b359c3be0456c71b01e27"

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
        temp = current_temperature

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
        humid = current_humidity

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
        label1.config(text = str(temp))
        label2.config(text = str(current_pressure))
        label3.config(text = str(humid))
        label4.config(text = str(weather_description))
      
        # print following values
        result = (" Temperature (in kelvin unit) = " +
                        str(temp) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(humid) +
            "\n description = " +
                        str(weather_description))

    else:
        print(" City Not Found ")
root = Tk()
root.title('Weather forecast')
w = Label(root, text='Enter the name of the city to fetch the weather:')
i=Entry(root)
b=Button(root,text='submit',command=fetch)
l1 = Label(root, text = 'temperature =')
label1 = Label(root, text = '')
l2 = Label(root, text = 'pressure =')
label2 = Label(root, text = '')
l3 = Label(root, text = 'humidity =')
label3 = Label(root, text = '')
l4 = Label(root, text = 'weather =')
label4 = Label(root, text = '')
w.pack()
i.pack()
b.pack()
l1.pack()
label1.pack()
l2.pack()
label2.pack()
l3.pack()
label3.pack()
l4.pack()
label4.pack()
root.mainloop()
