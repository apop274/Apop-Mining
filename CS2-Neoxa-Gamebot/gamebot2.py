import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
import random
import time

#Alex Popov Neoxa cs2 gamebot 3.13.24


# Function to check if the screen matches a reference image
def check_screen(reference_image, monitor):
    screenshot = pyautogui.screenshot(region=monitor)
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, reference_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    return max_val > 0.9  # Adjust threshold as needed


def move():
    #directions = ['W', 'A', 'S', 'D']
    
    
    key = 'W'
    pyautogui.keyDown(key)
    time.sleep(1)
    pyautogui.keyUp(key)
    print("clicked W")
   
    key= 'S'
    pyautogui.keyDown(key)
    time.sleep(1)
    pyautogui.keyUp(key)
    print("clicked S")

    key= 'A' 
    pyautogui.keyDown(key)
    time.sleep(1)
    pyautogui.keyUp(key)
    print("clicked A")


    key='D'   
    pyautogui.keyDown(key)
    time.sleep(1)
    pyautogui.keyUp(key)
    print("clicked D")
    

   


    #choice = random.choice(directions)
   # pyautogui.keyDown(key)
 #   time.sleep(2)
 #   pyautogui.keyUp(key)
    #pyautogui.press(key, duration=0.8)
  #  time.sleep(0.5)





# Function to move randomly using WASD keys
def move_randomly():
    directions = ['W', 'A', 'S', 'D']

    rand = random.randint(1,8)
    key = 'W'

    if rand <=2:
        key = 'A'
    elif rand<=4 and rand>2:
        key='D'
    elif rand>4 and rand<=6:
        key='S'
    else:
        key='W'


    #choice = random.choice(directions)
    pyautogui.keyDown(key)
    time.sleep(2)
    pyautogui.keyUp(key)
    #pyautogui.press(key, duration=0.8)
    time.sleep(0.5)

# Function to simulate shooting
def shoot():
    pyautogui.click()

# Function to swap weapons
def swap_weapon():
    pyautogui.press('3')  # Press 3 to swap to knife
    pyautogui.press('2') # swap back to secondary




def main():
    #cs2 name of title (hover over in taskbar when running)
    cs2_window_title = "Counter-Strike 2"

    # Find the CS2 window
    cs2_window = gw.getWindowsWithTitle(cs2_window_title)
    if not cs2_window:
        print("CS2 window not found. Make sure the game is running.")
        return

    cs2_window = cs2_window[0]
    monitor = (cs2_window.left, cs2_window.top, cs2_window.width, cs2_window.height)

    team_pick_image=cv2.imread('CS2-Team-pick.png') #cs2 team pick screen
   # terrorist_image = cv2.imread('terrorist_screen.png')  # Load reference image for terrorist screen
   # counterterrorist_image = cv2.imread('counterterrorist_screen.png')  # Load reference image for counterterrorist screen
    
    while True:
        if check_screen(team_pick_image, monitor):
            pyautogui.move(100, 0, duration=0.25)  # Move mouse to the left
            move()
        elif check_screen(team_pick_image, monitor):
            pyautogui.move(-100, 0, duration=0.25)  # Move mouse to the right
            move()
        else:
            move()
            move_randomly()

        if random.random() < 0.1:  # 10% chance to shoot
            shoot()
            move()

        if random.random() < 0.15:  # 5% chance to swap weapons
            swap_weapon()
            move()


        time.sleep(1)  # Adjust delay between actions as needed

        print("running...")

        

#you have to correct this part below. look in the previous gpt conversations.

if __name__ == "__main__":
    main()





