
import pyautogui
import time


def move2():
    #directions = ['W', 'A', 'S', 'D']
    
    
    key = 'W'
    pyautogui.keyDown(key)
    time.sleep(4)
    pyautogui.keyUp(key)
    print("clicked W")
   
    key='D'   
    pyautogui.keyDown(key)
    time.sleep(3)
    pyautogui.keyUp(key)
    print("clicked D")


    key= 'S'
    pyautogui.keyDown(key)
    time.sleep(1)
    pyautogui.keyUp(key)
    print("clicked S")

    ey = 'W'
    pyautogui.keyDown(key)
    time.sleep(4)
    pyautogui.keyUp(key)
    print("clicked W")

    key= 'A' 
    pyautogui.keyDown(key)
    time.sleep(1)
    pyautogui.keyUp(key)
    print("clicked A")

    ey = 'W'
    pyautogui.keyDown(key)
    time.sleep(4)
    pyautogui.keyUp(key)
    print("clicked W")
