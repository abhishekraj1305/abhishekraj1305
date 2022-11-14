import pywhatkit as kit
import cv2

kit.text_to_handwritting["Hope you are doing well", "handwritting.png"]
img = cv2.imread("handwritting.png")
cv2.imshow("text to Handwritting", img)
cv2.waitkey(0)
cv2.destroyAllwindows()
# view rawText to handwritting.py hosted with * by