from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city=city_name.get()

    api_key = "ebbb5b9cdf79b3255099787c94ea055c"  # Replace with your actual API key
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
    
    w_label1.config(text=data["weather"][0]["main"])

    wb_label1.config(text=data["weather"][0]["description"]) 

    Temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)))
    
    pre_label1.config(text=str(data["main"]["pressure"]))


win = Tk()
win.title("Weather App")
win.geometry("570x570")

canvas = Canvas(win, width=570, height=570)
canvas.pack(fill=BOTH, expand=True)

bg_image = PhotoImage(file="backgrouud.png")  # Replace with your image file
canvas.create_image(0, 0, anchor=NW, image=bg_image)

# Add a label for the app title
name_label = Label(win, text="Weather App", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50,width=520 )

city_name=StringVar()


# Define the list of locations
list_name = [
    "Punjab",
    "Sindh",
    "Khyber Pakhtunkhwa",
    "Balochistan",
    "Islamabad",
    "Gilgit-Baltistan",
    "Azad Jammu and Kashmir"
]

# Create a combobox with the list of locations
com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 20,"bold"),textvariable=city_name)
com.place(x=25, y=120, height=50, width=520)

w_label = Label(win, text="Weather Climate", font=("Times New Roman", 20))
w_label.place(x=25, y=260, height=50, width=250)

w_label1 = Label(win, text="", font=("Times New Roman", 20))
w_label1.place(x=300, y=260, height=50, width=250)

wb_label = Label(win, text="Weather Description", font=("Times New Roman", 20))
wb_label.place(x=25, y=330, height=50, width=250)

wb_label1 = Label(win, text="", font=("Times New Roman", 20))
wb_label1.place(x=300, y=330, height=50, width=250)

Temp_label = Label(win, text="Temperature", font=("Times New Roman", 20))
Temp_label.place(x=25, y=400, height=50, width=250)

Temp_label1 = Label(win, text="", font=("Times New Roman", 20))
Temp_label1.place(x=300, y=400, height=50, width=250)

pre_label = Label(win, text="pressure", font=("Times New Roman", 20))
pre_label.place(x=25, y=470, height=50, width=250)

pre_label1 = Label(win, text="", font=("Times New Roman", 20))
pre_label1.place(x=300, y=470, height=50, width=250)

Done_Button = Button(win,text="Done",font=("Times New Roman", 20,"bold"),command=data_get)
Done_Button.place(x=235, y=190, height=50, width=100)



win.mainloop()
