import time
import random
import pyautogui
import cv2
import numpy as np

# Constants for screen capture and comparison


x1= 100
y1= 900
x2= 1850
y2= 150

SCREENSHOT_REGION = (x1, y1, x2, y2)  
# Define the region for the screenshot





T_ERROR = 0.8  # Adjust the error threshold based on your screenshot matching needs

# Function to move randomly
def move_randomly():
    keys = ['w', 'a', 's', 'd']
    key = random.choice(keys)
    pyautogui.keyDown(key)
    time.sleep(random.uniform(0.5, 1))  # Adjust the delay based on your needs
    pyautogui.keyUp(key)

# Function to shoot occasionally
def shoot_randomly():
    if random.random() < 0.1:  # Adjust the probability based on your needs
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.5, 1))
        pyautogui.mouseUp()

# Function to swap weapons in random patterns
def swap_weapons():
    keys = ['1', '2', '3', '4']  # Assuming 1, 2, 3, 4 are the keys for weapons
    key = random.choice(keys)
    pyautogui.press(key)
    time.sleep(random.uniform(0.5, 1))

# Function to check if it's time to choose a side (Terrorist or Counter-Terrorist)
def is_choose_side_screen():
    screenshot = pyautogui.screenshot(region=SCREENSHOT_REGION)
    screenshot_np = np.array(screenshot)
    template = cv2.imread("choose_side_template.png")  # Replace with your template image

    # Convert the images to grayscale
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Match the template
    res = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    if np.max(res) > T_ERROR:
        return True
    return False

# Function to choose a side by moving the mouse left or right
def choose_side():
    if random.choice([True, False]):  # Randomly choose left or right
        pyautogui.move(-50, 0, duration=0.5)
    else:
        pyautogui.move(50, 0, duration=0.5)

# Main loop
def main():
    while True:

        move_randomly()
        move_randomly()
        shoot_randomly()
        swap_weapons()

        if is_choose_side_screen():
            choose_side()

        time.sleep(random.uniform(1, 5))

if __name__ == "__main__":
    main()
