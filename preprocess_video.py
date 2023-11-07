import cv2

# Open the input video file
input_video_path = "C:/Users/babut/OneDrive/Desktop/final_capstone/CNNs WOLF BLITZER Is STUNNED After IDF Admits To Bombing Civilians In Jabaliya Refugee Camp Rising.mp4"
cap = cv2.VideoCapture(input_video_path)

# Get the video's frame rate and resolution
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create an output video writer
output_video_path = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use different codecs if needed
out = cv2.VideoWriter(output_video_path, fourcc, 1, (frame_width, frame_height))

frame_count = 0  # Initialize frame count

while True:
    ret, frame = cap.read()  # Read a frame from the input video

    if not ret:
        break  # Break the loop if we've reached the end of the video

    frame_count += 1

    # Only write every 25th frame (1 frame per second)
    if frame_count % 25 == 0:
        out.write(frame)

# Release video objects
cap.release()
out.release()

print("Video conversion completed.")
