import os
from ultralytics import YOLO
import cv2
import math
import csv
from copy import copy
import easyocr

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
reader = easyocr.Reader(['en'], gpu=True)

def check_valid(input):
    return all(char.isdigit() or char.isalpha() for char in input)


def read_pill_imprint(imprint_crop):
    detections = reader.readtext(imprint_crop)
    text = ""  # Initialize text with an empty string
    detected_score = 0  # Initialize score before the loop
    for detection in detections:
        bbox, detected_text, detected_score = detection
        text = detected_text.upper().replace(' ', '')  # Use replace instead of remove

    if check_valid(text):
        return text, detected_score
    return 0, 0




def findMatchingPill(csvFile, pillType, imprint):
    with open(csvFile, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            csv_pillName, csv_pillType, csv_Color, csv_Shape, csv_ImprintA, csv_ImprintB = row
            if csv_pillType == pillType and (csv_ImprintA == imprint or csv_ImprintB == imprint):
                return csv_pillName
    return "Unknown"


def convertToGrayScale(img):
    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform histogram equalization
    gray_img = cv2.equalizeHist(gray_img)

    # Apply Gaussian blur
    gray_img = cv2.GaussianBlur(gray_img, (7, 7), 0)

    # Apply adaptive thresholding
    _, binary_img = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Convert binary image to 3 channels (grayscale to BGR)
    gray_img_bgr = cv2.cvtColor(binary_img, cv2.COLOR_GRAY2BGR)

    return gray_img_bgr


def pillPredict(cap):
    ret, frame = cap.read()
    if ret:
        pillResults = pillModel(frame, stream=True)
        # imprint_detections = []
        for result in pillResults:
            boxes = result.boxes
            for box in boxes:
                confidence = math.ceil((box.conf[0] * 100)) / 100
                if confidence >= 0.77:
                    # bounding box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values


                    # put box in cam
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)

                    print("Confidence --->", confidence)

                    # class name
                    cls = int(box.cls[0])
                    print("Class name -->", pillClassNames[cls])

                    # store box info
                    # imprint_detections.append([cls, x1, y1, x2, y2])
                    imprint_crop = copy(frame[y1:y2, x1:x2])
                    imprint_crop_thresh = convertToGrayScale(imprint_crop)
                    text, score = read_pill_imprint(imprint_crop)

                    # cv2.imshow("text", imprint_crop_thresh)

                    # Display confidence and class name on the bounding box
                    # label = f"{pillClassNames[int(box.cls[0])]} {confidence:.2f}%"
                    if score >= 0.4:
                        drugType = pillClassNames[cls]
                        imprint = text
                        output = findMatchingPill("pill_database.csv", drugType, imprint)
                        label = f"{pillClassNames[int(box.cls[0])]}: {output} ({imprint})"
                    else:
                        label = f"{pillClassNames[int(box.cls[0])]}"

                    # object details
                    org = [x1, y1]
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 1
                    color = (255, 0, 0)
                    thickness = 2

                    cv2.putText(frame, label, org, font, fontScale, color, thickness)



        cv2.imshow('Webcam', frame)




# load models
pillModel = YOLO("training_results/capsules_tablets_m2/weights/best.pt")

# object classes
pillClassNames = ["Capsule", "Tablet"]


if __name__ == '__main__':
    video_name = input('Enter 0 for Webcam | Enter 1 for Video Source: ')
    if video_name == '0':
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print('Webcam is disabled')

        while cap.isOpened():
            pillPredict(cap)
            # mnistPredict(cap)
            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    else:
        cap = cv2.VideoCapture('pills.mp4')
        if not cap.isOpened():
            print('Cannot open file')

        while cap.isOpened():
            pillPredict(cap)
            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
