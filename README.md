## Yolov8 Capsules and Tablets C++ Detection for Windows

## Description
An application for running Yolov8 detection using HailoRT and OpenCV on Windows, without TAPPAS dependencies

## Hardware Requirements
* Hailo-8 AI Accelerator

## Software Requirements
* Windows 10
* Visual Studio 2022
* MinGW Compiler v11.0.0
* CMake 3.29.0
* OpenCV 4.9.0
* HailoRT 4.16.0

## Pill Detection
* Structure: Yolov8m
* Classes: Capsule, Tablet

## Feature recognition
### Shape
* Structure: ResNet-32
* Classes: Circle, Oval, Oblong

### Color
* Structure: ResNet-32
* Classes: White, Yellow, Pink, Orange, Blue, Brown, Green

## Imprint Recognition
### Image Processing
* Imprint extraction: MSWT
* Imprint Repairion: LBP

### Imprint Detection

### Imprint Correction
* Structure: RNN

## Reference
```
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9883737/
```
```
  https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/iet-ipr.2014.1007
```
