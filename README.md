# img-to-questions
python tool to convert an image to a list of questions


## Usage
1. Install tesseract, instructions [here](https://tesseract-ocr.github.io/tessdoc/Installation.html)
    ```bash
    sudo apt install tesseract-ocr
    sudo apt install libtesseract-dev
    ```
2. Install app requirements
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application
    ```bash
    cd src
    python3 main.py -f ./test_data/test.png
    ```
