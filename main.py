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
                        (str(weather_description)).capitalize())
        print(result)

    else:
        print(" City Not Found ")
root = Tk()
root.title('Weather Forecast')

root.configure(bg='light blue')
root.geometry("750x500")
w = Label(root, text='Enter the name of the city to fetch the weather:',font=('Helvetica 15 bold',30),borderwidth=5)
w.config(bg="#053246", fg= "violet")
w.pack(padx=30,pady=3)

i=Entry(root,font=('Helvetica 15 bold',20),width=40)
i.pack(padx=10,pady=10)
b=Button(root,text='Submit',command=fetch,borderwidth=5,fg="white",bg="blue",width=20).place(x=480,y=150)

btn=Button(root, text="Chg color", command= change_color,bg="blue",borderwidth=5,fg="white",width=20).place(x=120,y=150)

l1 = Label(root, text = 'Temperature :',bg="white",fg="black").place(x=230,y=230)
label1 = Label(root, text = '',bg="white",fg="black",width=2).place(x=320,y=230)
l2 = Label(root, text = 'Pressure :',bg="white",fg="black").place(x=420,y=230)
label2 = Label(root, text = '',bg="white",fg="black",width=2).place(x=490,y=230)
l3 = Label(root, text = 'Humidity :',bg="white",fg="black",width=10).place(x=230,y=280)
label3 = Label(root, text = '',bg="white",fg="black",width=2).place(x=320,y=280)
l4 = Label(root, text = 'Weather :',bg="white",fg="black").place(x=420,y=280)
label4 = Label(root, text = '',bg="white",fg="black",width=2).place(x=490,y=280)

w.pack()
i.pack()


root.mainloop()
