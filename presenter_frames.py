import cv2
import json

# Loading the cascades
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


# Defining a function that will do the detections
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in faces:
        roi_gray = gray[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for ex, ey, ew, eh in eyes:
            pass  # You can add code here if you want to do something with the eyes
        return (x, y, w, h)  # Return face coordinates if detected
    return None


# Open the video file
video_capture = cv2.VideoCapture("CNNs WOLF BLITZER Is STUNNED After IDF Admits To Bombing Civilians In Jabaliya Refugee Camp Rising.mp4")
frame_rate = int(video_capture.get(cv2.CAP_PROP_FPS))
total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

face_detected_timestamps = []

# Process the frames
for i in range(total_frames):
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if i % (frame_rate * 3) == 0:  # Detect every 3 seconds
        face_coordinates = detect(gray, frame)
        if face_coordinates is not None:
            seconds = i // frame_rate
            minutes = seconds // 60
            hours = minutes // 60
            face_detected_timestamps.append(
                f"{hours:02}:{minutes % 60:02}:{seconds % 60:02}"
            )

# Save the face detection timestamps to a JSON file
with open("face_detection_timestamps.json", "w") as f:
    json.dump(face_detected_timestamps, f)

# Release the video capture object
video_capture.release()
