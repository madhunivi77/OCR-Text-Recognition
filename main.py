#Author      : Madhumitha Sukumar
#Description : This code uses PyTesseract for OCR and OpenCV to annotate an image
#              with recognized text and bounding boxes.
# Import the libraries
import pytesseract
import cv2

# Setting the path for the Tesseract OCR engine
pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"
# Configuration for OCR; here it's set to recognize digits
config= 'digits'

# Read the image using OpenCV
image = cv2.imread("card.jpeg") # default color code bgr

# Convert image to rgb
img_RGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_RGB))

# Getting bounding boxes for each recognized character in the image
boxes = pytesseract.image_to_boxes(img_RGB, config=config) 
ih,iw,ic = image.shape
for box in boxes.splitlines():
    box = box.split(" ")
    # print(box)
    x ,y, w,h = int(box[1]) ,int(box[2]),int(box[3]),int(box[4])
    cv2.rectangle(image, ( x , ih-y ),( w , ih-h ), ( 0 , 255 , 0 ), 1)
    cv2.putText(image,box[0],( x , ih-h ), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),1)

# Performing detailed OCR to get more data such as the position of words
data = pytesseract.image_to_data(img_RGB) 
# Annotating the image with bounding boxes and text based on the detailed OCR data
for id , line in enumerate(data.splitlines()):
    if id != 0:
        line = line.split()
        if len(line) == 12:
            x ,y, w,h = int(line[6]) ,int(line[7]),int(line[8]),int(line[9])
            cv2.rectangle(image, ( x , y ),( w+x , h+y ), ( 0 , 255 , 0 ), 1)
            cv2.putText(image,line[11],( x , y), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),1)

# Displaying the annotated image
cv2.imshow("Input", image)
cv2.waitKey(5000)