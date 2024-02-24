# Yolov8 Capsules and Tablets Detection

## Description
An application using Yolov8 for capsules and tablets detection

## Dataset
* Training dataset: 15,183 images

* Validation dataset: 547 images

* Test dataset: 223 images

## Dataset Reference
```
    https://www.kaggle.com/datasets/perfect9015/pillsdetectiondataset
```
```
    https://universe.roboflow.com/seblful/pills-detection-s9ywn
```
```
    https://universe.roboflow.com/project-qugef/ai-drug-analysis-service
```
```
    https://universe.roboflow.com/project-qugef/pill_remix_medicine_box
```
```
    https://universe.roboflow.com/pills-l7v0j/pills-thesis
```

## Pill Database Reference
```
    https://www.webmd.com/pill-identification/default.htm
```
```
    https://www.drugs.com/imprints.php
```

## Environment Setup
```
    pip install -r requirements.txt
```

## Export to ONNX
```
    python export_yoloV8.py -w training_results/capsules_tablets/weights/best.pt
```

## Detection
```
    python detection.py
```

## Result
![OIP-6-_jpg rf 032ce462539654ebd018c43209707f12](https://github.com/Kaiwei0323/Yolov8-Capsules-Tablets-Detection/assets/91507316/64a6e433-0df6-4910-a270-dd03f37df14b)

