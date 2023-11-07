import cv2
import json
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

# video file name 
video_file_name = "CNNs WOLF BLITZER Is STUNNED After IDF Admits To Bombing Civilians In Jabaliya Refugee Camp Rising.mp4" # has to change for different videos

# Specify the output folder for clips
output_folder = 'C:/Users/babut/OneDrive/Desktop/GUI/'

# create a new folder with the same name as the video file
new_folder_name = os.path.splitext(video_file_name)[0]
new_folder_path = os.path.join(output_folder, new_folder_name)
os.makedirs(new_folder_path, exist_ok=True)

# creating video summary

# Load timestamps from the JSON file
final_timestamps_json_file_path = 'C:/Users/babut/OneDrive/Desktop/final_capstone/final_timestamps.json'  # has to change for different videos
with open(final_timestamps_json_file_path, 'r') as final_timestamps_json_file:
    timestamps = json.load(final_timestamps_json_file)

# Load the original video file
video_file_path = "C:/Users/babut/OneDrive/Desktop/final_capstone/CNNs WOLF BLITZER Is STUNNED After IDF Admits To Bombing Civilians In Jabaliya Refugee Camp Rising.mp4"  # has to change for different videos
index = 1

# Process each timestamp in the JSON file
for clip in timestamps:
    start_time = clip['start']
    end_time = clip['end']
    title = clip['gist']

    # Specify the full path for the clip, including the output folder
    clip_filename = os.path.join(new_folder_path, f'{title}.mp4')
    
    # Extract the video clip using ffmpeg_extract_subclip
    ffmpeg_extract_subclip(video_file_path, start_time, end_time, targetname=clip_filename)
    
    index += 1



#=======================================================================================================================





# Creating text summary
auto_summary_json_file_path = "C:/Users/babut/OneDrive/Desktop/final_capstone/6nshi9eo39-5ff2-467b-aca9-822871c7fca5_chapters.json"
# Read data from the JSON file
with open(auto_summary_json_file_path, "r") as auto_summary_json_file:
    data = json.load(auto_summary_json_file)


# Create and save the text file in the output folder
text_summary_output_file_path = os.path.join(new_folder_path, "text_summary.txt")
with open(text_summary_output_file_path, "w") as text_summary_output_file:
    for entry in data:
        summary = entry["summary"]
        # headline = entry["headline"]
        # text_summary_output_file.write(f"Headline: {headline}\n")
        text_summary_output_file.write(f"{summary}\n\n")

print(f"Text file saved to {text_summary_output_file_path}")
