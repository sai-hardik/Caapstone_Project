from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path, output_audio_path):
    try:
        # Load the video clip
        video_clip = VideoFileClip(video_path)

        # Extract audio
        audio_clip = video_clip.audio

        # Save audio to the specified output path
        audio_clip.write_audiofile(output_audio_path)

        # Close the clips
        audio_clip.close()
        video_clip.close()

        print(f"Audio extracted and saved to {output_audio_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_file_path = "C:/Users/babut/OneDrive/Desktop/final_capstone/CNNs WOLF BLITZER Is STUNNED After IDF Admits To Bombing Civilians In Jabaliya Refugee Camp Rising.mp4"
output_audio_file_path = "C:/Users/babut/OneDrive/Desktop/final_capstone/output.mp3"

extract_audio(video_file_path, output_audio_file_path)
