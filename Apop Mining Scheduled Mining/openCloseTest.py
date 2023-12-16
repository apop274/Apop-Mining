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

def clicked_button():
    
    schedule.every().day.at("00:03").do(open_app)

    schedule.every().day.at("00:04").do(close_app)

    while True:
        schedule.run_pending()
        time.sleep(0)




frame = tk.Tk()
frame.title("start")
frame.geometry("450x500")
rgb_value = "#9E71E5"
#frame.configure(bg ="blue")


button = tk.Button(frame, text="start", width=15, height = 6, command = clicked_button, bg = rgb_value)

labelText = "Click the button to run the bot!"

start_label = tk.Label(frame, text = labelText)



start_label.pack(pady = 75)
button.pack(pady = 50)




frame.mainloop()