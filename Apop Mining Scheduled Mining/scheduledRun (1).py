#this program opens lolMiner at the sunny times, for the mining to occur at the sunny times

import subprocess
import schedule
import time
import os

def open_app():
   
   # app_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk'
    app_path = r'C:\Users\Xxapo\OneDrive\Desktop\Nexa coin\lolMiner_v1.77b_Win64\1.77b\mine_nexa'
    subprocess.Popen(['start', 'cmd', '/c', app_path], shell=True)

def close_app():
    
    #app_name = 'chrome.exe'
    #app_name = 'cmd.exe'
    #app_name = 'lolMiner.exe'
    subprocess.Popen(['taskkill', '/f', '/im', 'lolMiner.exe'], shell=True)
    subprocess.Popen(['taskkill', '/f', '/im', 'cmd.exe'], shell=True)
    #os.system(f'taskkill /f /im {app_name}')

#open time
schedule.every().day.at("7:15").do(open_app)

#close time
schedule.every().day.at("16:30").do(close_app)

#for testing
#schedule.every().day.at("16:12").do(open_app)
#schedule.every().day.at("16:14").do(close_app)


while True:
    schedule.run_pending()
    time.sleep(1)
    print('running...')


#to close: click in terminal, presss ctrl+c
