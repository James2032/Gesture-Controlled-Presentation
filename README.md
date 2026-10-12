# Gesture-Controlled-Presentation
HCI project for controlling presentations using hand gestures through a webcam.

Technologies Used:

Python 3.12
OpenCV - Accesse the webcam and process video.
MediaPipe - Detect and track hand movements.
GitHub - Store and manages the project code.

Current Progress (Milestone 1)
Set up the Python development environment.
Installed OpenCV and MediaPipe.
Created webcam_test.py to test webcam access.
Created hand_tracking.py to detect and track hands.
Successfully tested real time hand tracking using Mediapipe.

How to run:
Install Python 3.12.
Install the required libraries:
python -m pip install opencv-python mediapipe
Download the MediaPipe hand-tracking model:
curl -L -o hand_landmarker.task "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
Run the hand-tracking program:
python hand_tracking.py
The webcam should open and display green tracking points on your hands. Press Q if you want to close the program.

Next Steps:
Recognize specific hand gestures.
Use gestures to move between presentation slides.
Improve gesture accuracy and prevent accidental commands.
Conduct usability testing.


