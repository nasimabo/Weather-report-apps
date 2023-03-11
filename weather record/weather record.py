from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiErcises")
    location=geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    #weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    desctiption = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"o"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"o"))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=desctiption)
    p.config(text=pressure)


#search box
Search_imge = PhotoImage(file="draw-black-line-transparent-png-11.png")
myimage = Label(image=Search_imge)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=55,y=35)
textfield.focus()

Search_icon=PhotoImage(file="icons8-search-50.png")
myimage_icon=Button(image=Search_icon,borderwidth=1,width=50,height=38,padx=7,pady=8,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=350,y=34)

#logo
Logo_image = PhotoImage(file="images.png")
logo=Label(image=Logo_image,width=180,height=180,border=20)
logo.place(x=155,y=150)


#Botton box
#Frame_image = PhotoImage(file="blue-button-png-6.png",width=1000,height=100)
#frame_myimage=Label(image=Frame_image)

#frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text= "PRESSURE",font=("Helvetica",15,'bold'),fg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)


w=Label(text="...",font=("arial",20,"bold"))
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"))
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"))
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"))
p.place(x=670,y=430)


root.mainloop()
