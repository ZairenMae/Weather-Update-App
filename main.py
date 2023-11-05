import customtkinter
from PIL import Image
import datetime

# YOUR open weather api key = 4cd3973b9696a86169cb13dbfba173c8
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
configDict=get_default_config()
configDict['language']='en'
owmKey='4cd3973b9696a86169cb13dbfba173c8'

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Weather Update App")
app.geometry("480x380")

def getDateNow():
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    year = int(datetime.datetime.now().year)
    month_name = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    return f"{month_name[month-1]} {day}, {year}"

weatherData = {
    'place': 'Iloilo, PH',
    'status': 'default',
    'temp': 0,
    'heatIndex': None,
    'humidity': 0
}

frame=customtkinter.CTkLabel(app,text="")
frame.grid(row=0,column=0,sticky="w",padx=50,pady=20)

def dynamiclabels():
    cityLabel=customtkinter.CTkLabel(frame,text=weatherData['place'],font=('Arial BOLD', 25),anchor="w",width=180)
    cityLabel.grid(row=0,column=0,sticky="w")
    dateLabel=customtkinter.CTkLabel(frame,text=getDateNow(),font=('Arial', 15),anchor="e",width=200)
    dateLabel.grid(row=0,column=1,sticky="e")
    try:
        weatherImg=customtkinter.CTkImage(Image.open(f"weatherImages/{weatherData['status']}.png"),size=(120,120))
    except Exception as e:
        weatherImg=customtkinter.CTkImage(Image.open(f"weatherImages/default.png"),size=(120,120))
        print('image not found, default image will be selected.')
    weatherImgLabel=customtkinter.CTkLabel(frame,text='',image=weatherImg,anchor="center")
    weatherImgLabel.grid(row=1,column=0,columnspan=2,pady=20,sticky="nsew")
    weatherLabel=customtkinter.CTkLabel(frame,text=weatherData['status'],font=('Arial BOLD',15),anchor="center")
    weatherLabel.grid(row=2,column=0,columnspan=2,pady=[0,20],sticky="nsew")
    tempLabel=customtkinter.CTkLabel(frame,text=f"Temp: {weatherData['temp']}°(celcius) ",font=('Arial',12),anchor="w")
    tempLabel.grid(row=3,column=0,padx=2,pady=0,sticky="w")
    humLabel=customtkinter.CTkLabel(frame,text=f"Humidity: {weatherData['humidity']}",font=('Arial',12),anchor="w")
    humLabel.grid(row=4,column=0,padx=2,pady=0,sticky="w")
    heatLabel=customtkinter.CTkLabel(frame,text=f"Heat Index: {weatherData['heatIndex']}",font=('Arial',12),anchor="w")
    heatLabel.grid(row=5,column=0,padx=2,pady=0,sticky="w")

dynamiclabels()

def getweather(place):
    owm=OWM(owmKey,configDict)
    mgr=owm.weather_manager()
    observation=mgr.weather_at_place(place)
    w=observation.weather
    weatherData['status']=w.detailed_status
    weatherData['temp']=w.temperature('celsius')['temp_max']
    weatherData['heatIndex']=w.heat_index
    weatherData['humidity']=w.humidity
    dynamiclabels()
    print(weatherData)

def updateWeather():
    weatherData['place']=str(placesCombo.get())
    getweather(weatherData['place'])

getweather(weatherData['place'])

placesCombo=customtkinter.CTkComboBox(frame,values=["Iloilo, PH","Manila, PH","Cebu, PH","Bacolod, PH"])
placesCombo.grid(row=4,column=1,padx=2,pady=0,sticky="e")
submitBtn=customtkinter.CTkButton(frame,text="Get Weather",width=50,command=updateWeather)
submitBtn.grid(row=5,column=1,padx=1,pady=5,ipady=0,sticky="e")

app.resizable(False, False) 
app.mainloop()