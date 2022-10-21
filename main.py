import requests, json
from tkinter import *


def fetch():
    # Enter your API key here
    api_key = "b55ed3cfb145f3978f3ff4a02dfd3db4"

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
        '''current_temperature = y["temp"]
        current_temperature= int(current_temperature)
        current_temperature=current_temperature - 273
        temp = current_temperature'''

        #optimised
        temp = int(y['temp']) - 273
        

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        '''current_humidity = y["humidity"]
        current_humidity = float(current_humidity)
        current_humidity= current_humidity/100'''

        #optimised
        humid = float(y['humidity'])/100
        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
        label1.config(text = str(temp) + ' C')
        label2.config(text = str(current_pressure) + ' hPa')
        label3.config(text = str(humid))
        label4.config(text = str(weather_description))
      
        # print following values
        result = (" Temperature= " +
                        str(temp) + " C" +
            "\n atmospheric pressure = " +
                        str(current_pressure) + " hPa" +
            "\n humidity = " +
                        str(humid) +
            "\n description = " +
                        str(weather_description))
        print(result)

    else:
        print(" City Not Found ")
root = Tk()
root.title('Weather Forecast')
root.configure(bg='light blue')
w = Label(root, text='Enter the name of the city to fetch the weather:')
w.config(bg= "pink", fg= "black")
i=Entry(root)

b=Button(root,text='Submit',command=fetch, bg = 'cyan')
l1 = Label(root, text = 'Temperature :')
label1 = Label(root, text = '')
l1.config(bg= "pink", fg= "black")
l2 = Label(root, text = 'Pressure :')
label2 = Label(root, text = '')
l2.config(bg= "pink", fg= "black")
l3 = Label(root, text = 'Humidity :')
label3 = Label(root, text = '')
l3.config(bg= "pink", fg= "black")
l4 = Label(root, text = 'Weather :')
label4 = Label(root, text = '')
l4.config(bg= "pink", fg= "black")
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

f = ("Times bold", 14)
def prevPage():
    root.destroy()
    import page2

Button(
    root,
    text="Next Page",
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

root.mainloop()
