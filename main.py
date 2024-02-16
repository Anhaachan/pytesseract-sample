import cv2
import pytesseract
import os

input_image_path = './images/test.jpg'

image = cv2.imread(input_image_path)

my_config = r'--psm 6 --oem 3'

print(pytesseract.image_to_string(image, lang="eng", config="my_config"))
