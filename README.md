# SimpleCropper

Welcome to the SimpleCropper App project! This repository contains a simple application that utilizes the OpenCV library and Haar cascades to crop faces of people from images. Originally developed as a part of my university project, I've revisited and refined the implementation to showcase how facial detection and cropping can be achieved using readily available tools.

Features
* Detects faces in images using Haar cascade classifiers.
* Crops the detected faces, saving them as separate images.
* Provides a straightforward interface for selecting input and output images.
* Works with video input.

Usage
```bash
git clone https://github.com/supersokol/SimpleCropper.git
cd facecrop-app
pip install -r requirements.txt
FINALCROPPER.py [-h] [-i INPUT_PATH] [-o OUTPUT_PATH] [-v VIDEO_INPUT] [-s SKIPRATE] [-c CASCADE_PATH] [-l LOG_PATH]

options:
  -h, --help            show this help message and exit
  -i INPUT_PATH, --input_path INPUT_PATH
                        Path to a image, directory containig images or video. (str, default: None)
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        output path, str, defaults to "output" directory
  -v VIDEO_INPUT, --video_input VIDEO_INPUT
                        Video input (bool, default is False).
  -s SKIPRATE, --skiprate SKIPRATE
                        optional skiprate (int, for video only, default is 28).
  -c CASCADE_PATH, --cascade_path CASCADE_PATH
                        haar cascade filename path.
  -l LOG_PATH, --log_path LOG_PATH
                        optional log filename.
```
Tested on `Python 3.7.9`.

View Results: After processing, check the output directory for cropped face images.


License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code for educational and personal purposes.

Acknowledgments
I would like to acknowledge the power of the OpenCV library and the effectiveness of Haar cascade classifiers in facial detection. Their impact on computer vision and image processing is truly remarkable.