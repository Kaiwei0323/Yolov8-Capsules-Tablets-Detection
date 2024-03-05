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

## Mdoel
```
  yolov8m_pill_detector_v2.hef
  Accuracy: 95.2%
```

## Build
```
  cmake.exe -S . -B build -DOpenCV_DIR="C:/opencv/build/x64/vc16/lib"
  cmake.exe --build build
```

## Delete Build
```
  rm -r build
```

## Detection
```
  .\build\debug\yolov8_pill_detector.exe -hef=".\hefs\yolov8m_pill_detector_v2.hef" -video=0
```
