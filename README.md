## Yolov5 C++ Detection Standalone example for Windows
#### This is an example code for running yolov5 detection using HailoRT and OpenCV on Windows, without TAPPAS dependencies

**Last HailoRT version checked - 4.16.0**

**Disclaimer:** <br />
This code example is provided by Hailo solely on an “AS IS” basis and “with all faults”. No responsibility or liability is accepted or shall be imposed upon Hailo regarding the accuracy, merchantability, completeness or suitability of the code example. Hailo shall not have any liability or responsibility for errors or omissions in, or any business decisions made by you in reliance on this code example or any part of it. If an error occurs when running this example, please open a ticket in the "Issues" tab.<br />
Please note that this example was tested on specific versions and we can only guarantee the expected results using the exact version mentioned above on the exact environment. The example might work for other versions, other environment or other HEF file, but there is no guarantee that it will.



###### prerequisites: Windows 10, HailoRT, OpenCV, [Curl](https://curl.se/windows/)

Tested on Windows 10 Pro, CMake 3.29, HailoRT 4.16.0, OpenCV 4.2.0
This example exe file reside under the yolov8\build directory (cpp_yolov8_win_standalone_example.exe).
It requires as an input a hef file (yolov8m_pills.hef, which reside under the yolov8\hef directory) and a camera ID, e.g.:
.\cpp_yolov8_win_standalone_example.exe -hef=C:\yolov8\hefs\yolov8m_pills.hef -video=1

