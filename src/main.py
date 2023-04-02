from PIL import Image
import pytesseract
import cv2
from utils.arguments import parse_arguments
import numpy as np


def run(filename, factor):
    # Read image from which text needs to be extracted
    image = Image.open(filename)

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print(text)


def remove_vertical_lines(img):
    kernel_vertical = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 50))
    vertical_lines = 255 - cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel_vertical)
    return cv2.add(vertical_lines, img)


def remove_horizontal_lines(img):
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 1))
    horizontal_lines = 255 - cv2.morphologyEx(img, cv2.MORPH_CLOSE, horizontal_kernel)
    return cv2.add(horizontal_lines, img)


def remove_grid(img):
    img = remove_horizontal_lines(img)
    # img = remove_vertical_lines(img)
    return img


# For images too small, we can enlarge using openCV
def run2(filename, factor=1):
    # Read image from which text needs to be extracted
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, None, fx=factor, fy=factor)

    #img = cv2.medianBlur(img, 5)
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 3)

    # Remove vertical and horizontal lines
    img = remove_grid(img)

    cv2.imshow('image', img)
    cv2.waitKey()

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(img, lang='spa',
                                       config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789áéíóúÁÉÍÓÚüÜ? ')

    # Print the extracted text
    print(text)


if __name__ == "__main__":
    filename, scale = parse_arguments()
    run2(filename, scale)
