from cgitb import text
from re import template
import cv2
import numpy as np      # To convert python image object into numpy array for template matching method of OpenCV 
import pyautogui
import time

template1 = cv2.imread('templates/template1.png', 0)
template2 = cv2.imread('templates/template2.png', 0)
template3 = cv2.imread('templates/template3.png', 0)
template4 = cv2.imread('templates/template4.png', 0)
# '0' indicates grayscale format

# Setting threshold for confidence in template matching
threshold = 0.7

# Alert box for stopping criteria
pyautogui.alert(text = 'Keep the mouse pointer on the top-left corner of the screen to stop the program', title = 'Stopping Criteria')

flag = 0

def check(template):
    res = cv2.matchTemplate(im1, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    # Checking if template is matched
    if loc[0].size != 0:
        # Clicking on first match
        pyautogui.click(list(zip(*loc[::-1]))[0])
        global flag
        flag = 1

# Continuous loop to check for YouTube ad
while True:
    time.sleep(1)
    im1 = pyautogui.screenshot()
    im1 = np.asarray(im1.convert(mode = 'L'))
    check(template1)
    if flag == 1:
        continue
    check(template2)
    if flag == 1:
        continue
    check(template3)
    if flag == 1:
        continue
    check(template4)
    if flag == 1:
        continue

    # Stopping criteria
    if pyautogui.position == (0, 0):
        # Alert box with message that program is closed
        pyautogui.alert(text = 'Ad Skipper is closed', title = 'Ad Skipper Closed')
        break