import requests, json
from tkinter import *


def fetch():
    # Enter your API key here
    api_key = "8ec6af652686cbe5b7b800002c8fba1a"

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
        current_temperature= int(current_temperature)
        current_temperature=current_temperature - 273
        temp = current_temperature
        

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
        current_humidity = float(current_humidity)
        current_humidity= current_humidity/100

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
        result = (" Temperature (in celsius  unit) = " +
                        str(temp) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in decimal value) = " +
                        str(humid) +
            "\n description = " +
                        str(weather_description))

    else:
        print(" City Not Found ")
root = Tk()
root.geometry("500x500")
root.title('Weather forecast')
root.configure(bg='cyan')
w = Label(root, text='Enter the name of the city to fetch the weather:', font=("goudy old style", 30),bg="#053246",fg="violet",relief='solid')
i=Entry(root, width=30, font=('Arial 24'),relief='solid',borderwidth=2)
b=Button(root,text='submit',command=fetch,font=("goudy old style",10),bg="blue",fg="white",height=2, width=15,relief='solid',borderwidth=5)
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
root.mainloop()