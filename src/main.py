from email import message
from tkinter import messagebox
import requests, json
from tkinter import *
from random import shuffle
import time

API_KEY = "" # Enter your API key here

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?" # base_url variable to store url!!

def fetch():
    # Give city name
    city_name = i.get() 

    # complete_url variable to store
    # complete url address
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name

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
    try:
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
            "\n Atmospheric pressure = " +
                        str(current_pressure) + " hPa" +
            "\n Humidity = " +
                        str(humid) +
            "\n Description = " +
                        str(weather_description))
        print(result)
    except Exception:
        messagebox.showerror("Error!", "City not found!")
   
# Define the backround color for all the widgets
def change_color():
   colors= ['#e9c46a','#92a898','#c5d485','#85b2d4','#e85d04','#a2d2ff','#06d6a0','#4d908e','#6468ed']
   while True:
      shuffle(colors)
      for i in range(0,len(colors)):
         root.config(background=colors[i])
         root.update()
         time.sleep(1)

root = Tk()
root.title('Weather Forecast')
root.configure(bg='#a6deb5')

w = Label(root, text='Enter the name of the city to fetch the weather:')
w.config(bg= "#346641", fg= "black")
i = Entry(root)

b = Button(root,text='Submit',command=fetch, bg = '#346641')
btn = Button(root, text="Chg color", command= change_color,bg="#346641",borderwidth=5,fg="white")

l1 = Label(root, text = 'Temperature :')
label1 = Label(root, text = '')
l1.config(bg= "#346641", fg= "black")

l2 = Label(root, text = 'Pressure :')
label2 = Label(root, text = '')
l2.config(bg= "#346641", fg= "black")

l3 = Label(root, text = 'Humidity :')
label3 = Label(root, text = '')
l3.config(bg= "#346641", fg= "black")

l4 = Label(root, text = 'Weather :')
label4 = Label(root, text = '')
l4.config(bg= "#346641", fg= "black")

w.pack()
i.pack()
b.pack()
btn.pack()
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
    import page2 as page2

Button(
    root,
    text="Next Page",
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

root.mainloop()
