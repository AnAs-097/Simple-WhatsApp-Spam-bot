import webbrowser
import pyautogui
import keyboard
import time
webbrowser.open('https://web.whatsapp.com/')
time.sleep(30)
while keyboard.is_pressed('q')==False:
    pyautogui.write("baqwas")
    pyautogui.press("enter")
