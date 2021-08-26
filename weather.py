# -*- coding: utf-8 -*
import tkinter as tk
from tkinter import *
import requests


def findWeather():
    global temperature, windSpeed, humidity, pressure, discription, city, weather_image
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID=851432836a2e75d1e7c089fa9c4b7d27&units=metric".format(
        city.get())
    res = requests.get(url)
    data = res.json()
    temp_data = data['main']['temp']
    pressure_data = data['main']['pressure']
    wind_speed_data = data['wind']['speed']
    description_weather = data['weather'][0]['description']
    humidity_data = data['main']['humidity']

    discription.config(text=description_weather)
    temperature.config(text=str("{}\u00b0C".format(temp_data)))
    windSpeed.config(text=str("{}m/s".format(wind_speed_data)))
    humidity.config(text=str("{}%".format(humidity_data)))
    pressure.config(text=str("{}hPa".format(pressure_data)))

    description_weather.lower()

    if 'clear sky' in description_weather:
        weather_image.config(file="./icon/01d.png")

    if 'few clouds' in description_weather:
        weather_image.config(file="./icon/02d.png")

    if 'scattered clouds' in description_weather or 'clouds' in description_weather:
        weather_image.config(file="./icon/03d.png")

    if 'broken clouds' in description_weather:
        weather_image.config(file="./icon/04d.png")

    if 'shower rain' in description_weather or 'drizzle' in description_weather:
        weather_image.config(file="./icon/09d.png")

    if 'rain' in description_weather:
        weather_image.config(file="./icon/10d.png")

    if 'thunderstorm' in description_weather:
        weather_image.config(file="./icon/11d.png")

    if 'snow' in description_weather:
        weather_image.config(file="./icon/13d.png")

    if 'smoke' in description_weather or 'haze' in description_weather or 'mist' in description_weather or 'dust' in description_weather or 'fog' in description_weather or 'sand' in description_weather or 'ash' in description_weather or 'squall' in description_weather or 'tornado' in description_weather:
        weather_image.config(file="./icon/50d.png")


window = Tk()
canvas = tk.Canvas(window)
canvas.pack()

city = StringVar(window)

window.title('Weather Forecast By Shitij Agrawal')
window.geometry('300x250')
window.resizable(False, False)

weather_image = tk.PhotoImage(file='./icon/01d.png')

weather_icon = tk.Label(window, image=weather_image)
weather_icon.place(x=250, y=0, height=50, width=50)

tk.Label(window, text="City ").place(x=5, y=13)

city_box = tk.Entry(window, textvariable=city)
city_box.place(x=50, y=10, height=25, width=120)

canvas.create_line(0, 70, 300, 70, fill="yellow", width=1)

tk.Label(window, text=" * Details * ", fg="black").place(x=0, y=80)
canvas.create_line(0, 105, 100, 105, fill="black", width=1)
tk.Label(window, text="Temperature : ", fg="Red").place(x=20, y=110)
tk.Label(window, text="Wind Speed : ", fg="magenta").place(x=20, y=140)
tk.Label(window, text="Pressure : ", fg="yellow").place(x=20, y=170)
tk.Label(window, text="Humidity : ", fg="blue").place(x=20, y=200)

# All Change possible labels
discription = tk.Label(window, text="None", fg="DeepSkyBlue3")
discription.place(x=10, y=45)

temperature = tk.Label(window, text="None", fg="Red")
temperature.place(x=150, y=110)

windSpeed = tk.Label(window, text="None", fg="magenta")
windSpeed.place(x=150, y=140)

pressure = tk.Label(window, text="None", fg="yellow")
pressure.place(x=150, y=170)

humidity = tk.Label(window, text="None", fg="blue")
humidity.place(x=150, y=200)

find = tk.Button(window, text="Find", command=findWeather)
find.place(x=180, y=10, height=25, width=50)

window.mainloop()
