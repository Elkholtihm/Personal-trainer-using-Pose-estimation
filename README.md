# Personal Trainer using Pose Estimation
This project aims to demonstrate the use of pose estimation for personal training using Mediapipe. The goal is to count specific movements during a workout based on pose landmarks and angles.

## Project Structure
The project consists of the following files:

* test.py: A script to test pose estimation using Mediapipe.
* PoseDetectionModule.py: A custom module using Mediapipe for drawing pose landmarks and calculating angles between three given landmarks.
* PersonalTrainer.py: A script for counting movements during training based on pose landmarks and angles.

## Using the Project
To utilize this project, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Elkholtihm/Personal-trainer-using-Pose-estimation.git
    ```
2. Ensure you have all the necessary dependencies installed. You can install them using pip:
    ```bash
    pip install -r requirements.txt
    ```
5. Once you've set the model path, you can execute the `app1.py` file to run the website:
    ```bash
    python PersonalTrainer.py
    ```
   
## Pose Detection Module
The PoseDetectionModule.py file contains the PoseDetector class, which includes methods to:

1. Find and draw pose landmarks
2. Calculate angles between three given landmarks

## Personal Trainer Script
The PersonalTrainer.py script uses the PoseDetector module to count movements during a workout. The script performs the following steps:

1. Capture video from a webcam or a video file.
2. Detect pose landmarks.
3. Calculate angles between specific landmarks.
4. Count movements based on the calculated angles.
5. Display the video with landmarks, angles, and movement count.

## Connect with me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hamza-kholti-075288209/)

## Acknowledgments
[![Mediapipe Documentation](https://img.shields.io/badge/Mediapipe-Documentation-0A66C2?style=for-the-badge&logo=mediapipe&logoColor=white)](https://ai.google.dev/edge/mediapipe/solutions/guide) 
[![OpenCV Documentation](https://img.shields.io/badge/OpenCV-Documentation-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
