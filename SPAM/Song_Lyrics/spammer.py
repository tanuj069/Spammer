from email.quoprimime import body_check
import pyautogui, time
time.sleep(2)
f = open('moneyheist.txt','r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
