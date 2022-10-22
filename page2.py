from tkinter import *
import requests
ws = Tk()
ws.geometry('400x300')
ws.title('AQI based on PIN Code')
ws['bg'] = '#ffbf00'

api_key = "b55ed3cfb145f3978f3ff4a02dfd3db4"

f = ("Times bold", 14)

def fetch():
    zipcode = i.get()
    countrycode = "US"

    response = requests.get('https://thezipcodes.com/api/v1/search?zipCode='+zipcode+'&apiKey=e6fb2c75c061c85c065ae4bf6ba8e229');

    x = response.json()
    if x["success"] == True:
        la = x["location"][0]["latitude"]
        lo = x["location"][0]["longitude"]
    #if x["cod"] != "404":

        final_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={la}&lon={lo}&appid={api_key}"

        response1 = requests.get(final_url)

        x1 = response1.json()
        print(x1)
        aqi=x1['list'][0]['main']['aqi']
        label1.config(text=str(aqi))







def nextPage():
    ws.destroy()
    import main


i=Entry(ws)
i.pack()
button_submit = Button(ws, text ="Submit", command=fetch).pack()



#aqi = int(y['aqi']) - 273
#label1.config(text = str(aqi) + ' C')
l1 = Label(ws, text = 'AQI :').pack()
label1 = Label(ws, text = '')
label1.pack()
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