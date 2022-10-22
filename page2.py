from tkinter import *
import requests
ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg'] = '#ffbf00'

api_key = "b55ed3cfb145f3978f3ff4a02dfd3db4"

f = ("Times bold", 14)

def fetch():
    zipcode = i.get()
    countrycode = "US"
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{countrycode}&appid={api_key}"

    response = requests.get(url)

    x = response.json()
    print(x)
    #if x["cod"] != "404":
    la = x["lat"]
    lo= x["lon"]


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