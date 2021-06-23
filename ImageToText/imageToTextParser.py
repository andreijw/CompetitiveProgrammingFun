"""
    Instructions:
    pip install numpy
    pip install opencv-python
    pip install pytesseract (linux 3 apt-get install commands)
    on windows install an executable
    
    Here is the link to their github:
    https://github.com/UB-Mannheim/tesseract/wiki
    
    Class to quickly process a photo with text and transform it
    into a text file in order for us to read input / output
"""

import cv2
import sys
import pytesseract
import numpy as np

def read_image(image_path):
    image = cv2.imread(image_path)
    print("reading the image", image_path)
    return image
    
def gray_scale_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.GaussianBlur(gray_image, (3,3), 0)
    #gray_image = cv2.GaussianBlur(gray_image, (7,7), 0)
    return gray_image

def threshold_image(image):
    #t_image = cv2.adaptiveThreshold(image, 250, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 2)
    (t, t_image) = cv2.threshold(image, 5, 255, cv2.THRESH_BINARY_INV)
    # (t, t_image) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return t_image

def morph_opening(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    o_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=1)
    return o_image
    
def process_image(image):
    # https://tesseract-ocr.github.io/tessdoc/ImproveQuality#page-segmentation-method
    configuration = "--psm 6"
    contents = pytesseract.image_to_string(image, lang='eng', config=configuration)
    return contents
    
def apply_mask(original_image, binary_image):
    #inverted_image = cv2.bitwise_not(binary_image)
    m_image = cv2.bitwise_and(original_image, original_image, mask=binary_image)
    return m_image
    
def find_contours(image):
    new_image = image
    contours, hierarchy = cv2.findContours(new_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  
    print("found the following number of contours", len(contours))
    
    contoured_image = cv2.drawContours(new_image, contours, -1, (0, 255, 0), 3)
    return contoured_image
    
def main():
    # User will input the image path
    if len(sys.argv) < 2:
        print("Please enter an image path")
        return
    
    # read the image into an array of pixels
    image_path = sys.argv[1]
    image = read_image(image_path)
    
    pytesseract.pytesseract.tesseract_cmd = r'D:\\Program Files (x86)\\Tesseract\\tesseract.exe'

    # preprocess the image
    gray_image = gray_scale_image(image)
    t_image = threshold_image(gray_image)  
    c_image = find_contours(t_image)
    o_image = morph_opening(c_image)
    #m_image = apply_mask(gray_image, c_image)
    
    # display the images
    cv2.imshow('Original Image', image)
    cv2.imshow('Gray Image', gray_image)
    cv2.imshow('Binary Image', t_image)
    cv2.imshow('Contoured Image', c_image)
    cv2.imshow('Opened Image', o_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    #transform the image into text  
    imageContents = (process_image(o_image)[:-1]).strip()
    print("Output Text - ", imageContents)
    
if __name__ == "__main__":
    main()