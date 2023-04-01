from PIL import Image
import pytesseract
import cv2
from utils.arguments import parse_arguments


def run(filename):
    # Read image from which text needs to be extracted
    image = Image.open(filename)

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print(text)


# For images too small, we can enlarge using openCV
def run2(filename, factor=1):
    # Read image from which text needs to be extracted
    image = cv2.imread(filename)
    image = cv2.resize(image, None, fx=factor, fy=factor)

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print(text)


if __name__ == "__main__":
    filename, scale = parse_arguments()
    run2(filename, scale)
