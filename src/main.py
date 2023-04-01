from PIL import Image
import pytesseract

from utils.arguments import parse_arguments


def run(filename):
    # Read image from which text needs to be extracted
    image = Image.open(filename)

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print(text)


if __name__ == "__main__":
    filename = parse_arguments()
    run(filename)
