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
    gray_image = cv2.GaussianBlur(gray_image, (13,13), 0)
    return gray_image
    
def invert_image(image):
    i_image = cv2.bitwise_not(image)
    return i_image

def threshold_image(image):
    # a global threshold is not good for an image like this
    t_image = cv2.adaptiveThreshold(image, 250, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,9,2)
    return t_image
    
def open_image(image):
    kernel = np.ones((1,1), np.uint8)
    o_image = cv2.dilate(image, kernel, iterations=1)
    return o_image
    
def canny_image(image):
    c_image = cv2.Canny(image, 100, 250)
    return c_image
    
def process_image(image):
    # https://tesseract-ocr.github.io/tessdoc/ImproveQuality#page-segmentation-method
    configuration = "r'--oem 3 --psm 6'"
    contents = pytesseract.image_to_string(image)
    return contents
    
def get_bounding_box(image):
    img = image
    h, w, c = img.shape
    boxes = pytesseract.image_to_boxes(img)
    
    for pixel in boxes.splitlines():
        split_pixel = pixel.split(' ')
        img = cv2.rectangle(image, (int(split_pixel[1]), h - int(split_pixel[2])), (int(split_pixel[3]), h - int(split_pixel[4])), (0, 255, 0), 2)
    
    return img
    
def apply_mask(image):
    m_image = image
    return m_image
    
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
    i_image = invert_image(gray_image)
    t_image = threshold_image(i_image)
    o_image = open_image(t_image)
    c_image = canny_image(o_image)
    
    # display the images
    cv2.imshow('Original Image', image)
    cv2.imshow('Gray Image', gray_image)
    cv2.imshow('Inverted Image', i_image)
    cv2.imshow('Binary Image', t_image)
    cv2.imshow('Opened Image', o_image)
    cv2.imshow('Canny Image', c_image)
    c_image = t_image
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    #transform the image into text    
    imageContents = process_image(c_image)
    print(imageContents)
    
    # get boxes
    # boxed_image = get_bounding_box(c_image)
    # cv2.imshow('boxes', boxed_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()