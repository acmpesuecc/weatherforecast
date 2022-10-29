from tkinter import *
from tkinter import messagebox
import requests

ws = Tk()
ws.geometry('400x300')
ws.title('AQI based on PIN Code')
ws['bg'] = '#ffbf00'

API_KEY = "" # Enter your openweather API key here
ZIP_API_KEY = "" # Enter your zipcode API key here

f = ("Times bold", 14)

def fetch():
    zipcode = i.get()
    countrycode = "US"

    zip_url = "https://thezipcodes.com/api/v1/search?zipCode=" + zipcode + f"&apiKey={ZIP_API_KEY}"

    response = requests.get(zip_url)

    x = response.json()
    try:
        la = x["location"][0]["latitude"]
        lo = x["location"][0]["longitude"]

        final_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={la}&lon={lo}&appid={API_KEY}"

        response1 = requests.get(final_url)

        x1 = response1.json()
        print(x1)
        aqi=x1['list'][0]['main']['aqi']
        pm2_5=x1['list'][0]['components']['pm2_5']
        pm10 = x1['list'][0]['components']['pm10']
        label1.config(text=str(aqi))
        label2.config(text='PM 2.5 = '+str(pm2_5)+', PM 10 = '+str(pm10))
    except Exception:
        messagebox.showerror("Error!", "Zip code not found!")

def nextPage():
    ws.destroy()
    import main as main

label3 = Label(ws,text = "Enter your pincode")
i=Entry(ws)
label3.pack()
i.pack()
button_submit = Button(ws, text ="Submit", command=fetch).pack()

#aqi = int(y['aqi']) - 273
#label1.config(text = str(aqi) + ' C')
l1 = Label(ws, text = 'AQI :').pack()
label1 = Label(ws, text = '')
label2=Label(ws,text='')
label3=Label(ws,text='Particulate matter values:')
label1.pack()
label3.pack()
label2.pack()
Label(
    ws,
    padx=20,
    pady=20,
    bg='#ffbf00',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Previous Page",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()