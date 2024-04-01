def check_screen(reference_image, monitor):
    screenshot = pyautogui.screenshot(region=monitor)
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, reference_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    return max_val > 0.9  # Adjust threshold as needed





def move3():
    #directions = ['W', 'A', 'S', 'D']
    
    
    key = 'W'
    pyautogui.keyDown(key)
    time.sleep(4)
    pyautogui.keyUp(key)
    print("clicked W")
   
    key= 'S'
    pyautogui.keyDown(key)
    time.sleep(1)
    pyautogui.keyUp(key)
    print("clicked S")

    key= 'A' 
    pyautogui.keyDown(key)
    time.sleep(2)
    pyautogui.keyUp(key)
    print("clicked A")


    key='D'   
    pyautogui.keyDown(key)
    time.sleep(2)
    pyautogui.keyUp(key)
    print("clicked D")



def move_randomly2():
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

    pyautogui.keyDown(key)
    time.sleep(2)
    pyautogui.keyUp(key)
    time.sleep(1)

