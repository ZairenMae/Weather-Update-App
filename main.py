import customtkinter
from PIL import Image
import datetime

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

frame= customtkinter.CTkLabel(app, text="")
frame.grid(row=0,column=0,sticky="w", padx=50, pady=20)

cityLabel = customtkinter.CTkLabel(frame, text=weatherData['place'],font=('Arial BOLD', 25),anchor="w", width=180)
cityLabel.grid(row=0,column=0,sticky="w")

dateLabel = customtkinter.CTkLabel(frame, text=getDateNow(),font=('Arial', 15),anchor="e",width=200)
dateLabel.grid(row=0,column=1,sticky="e")

weatherImg = customtkinter.CTkImage(Image.open(f"weatherImages/{weatherData['status']}.png"),size=(120, 120))
weatherLabel = customtkinter.CTkLabel(frame,text='', image=weatherImg,anchor="center")
weatherLabel.grid(row=1,column=0,columnspan=2,pady=20,sticky="nsew")

weatherLabel = customtkinter.CTkLabel(frame,text=weatherData['status'],font=('Arial BOLD', 15), anchor="center")
weatherLabel.grid(row=2,column=0,columnspan=2,pady=[0,20],sticky="nsew")

tempLabel = customtkinter.CTkLabel(frame, text=f"Temp: {weatherData['temp']}°(celcius) ",font=('Arial', 12),anchor="w")
tempLabel.grid(row=3,column=0,padx=2,pady=0,sticky="w")

humLabel = customtkinter.CTkLabel(frame, text=f"Humidity: {weatherData['humidity']}",font=('Arial', 12),anchor="w")
humLabel.grid(row=4,column=0,padx=2,pady=0,sticky="w")

heatLabel = customtkinter.CTkLabel(frame, text=f"Heat Index: {weatherData['heatIndex']}",font=('Arial', 12),anchor="w")
heatLabel.grid(row=5,column=0,padx=2,pady=0,sticky="w")

placesCombo = customtkinter.CTkComboBox(frame, values=["Iloilo, PH","Manila, PH","Cebu, PH","Bacolod, PH"])
placesCombo.grid(row=4,column=1,padx=2,pady=0,sticky="e")

submitBtn = customtkinter.CTkButton(frame, text="Get Weather", width=50)
submitBtn.grid(row=5,column=1,padx=1,pady=5,ipady=0,sticky="e")

app.resizable(False, False) 
app.mainloop()