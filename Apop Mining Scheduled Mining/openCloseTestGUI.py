import tkinter as tk
from tkinter import *
import subprocess
import os
import time
import schedule

def open_app():
    #path to application
    app_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk'
    subprocess.Popen([app_path], shell=True)


def close_app():
    #app_name = example.exe
    app_name = 'chrome.exe'
    os.system(f'taskkill /f /im {app_name}')

def start_func():

    running = True

     #open time
    schedule.every().day.at("15:28").do(open_app)

     #close time
    schedule.every().day.at("15:29").do(close_app)

    try:
        while running:
         schedule.run_pending()
         time.sleep(1)
    except KeyboardInterrupt:
     # put cursor in the terminal then press ctrl+c to end program
     print("Program has stopped running.")

frame = tk.Tk()
frame.title("Scheduled program opener/closer")
frame.geometry("450x500")
rgb_value = "#9E71E5"


button = tk.Button(frame, text="start", width=15, height = 6, command = start_func, bg = rgb_value)

labelText = "Click the button to run the bot!"

start_label = tk.Label(frame, text = labelText)


start_label.pack(pady = 75)
button.pack(pady = 50)


frame.mainloop()