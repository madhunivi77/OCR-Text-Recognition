# OCR-Text-Recognition

## Description
A Python application that utilizes Optical Character Recognition (OCR) to detect and annotate text in images. It leverages PyTesseract for text detection and OpenCV for drawing bounding boxes and annotations.

## Requirements
Python 3.x
OpenCV (cv2)
PyTesseract
Installation
Python Installation
Ensure Python 3.x is installed on your system. You can download it from the official Python website.

## Dependencies Installation
Install the required Python libraries using pip:

```python
pip install opencv-python
pip install pytesseract
``` 

## Tesseract OCR
Tesseract OCR needs to be installed separately. Installation instructions for various operating systems can be found on the Tesseract GitHub page.

# Configuration
## Setting Tesseract Path
Update the Tesseract command path in the script to match the installation location on your system:

```python
pytesseract.pytesseract.tesseract_cmd = "/path/to/tesseract"
```
Usage
Place the image you want to process in the same directory as the script and name it card.jpeg, or modify the script to point to your specific image file.

Run the script. It will perform OCR on the image and display the results with bounding boxes around detected text.

The annotated image will be displayed for a brief period (5 seconds), highlighting the recognized text areas.




