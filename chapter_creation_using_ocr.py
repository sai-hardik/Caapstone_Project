import cv2
import pytesseract
import json
import re  # Import the re module for regular expressions

# Set the Tesseract executable path (update it with your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load video and extract every 5th frame
cap = cv2.VideoCapture("C:/Users/babut/OneDrive/Desktop/final_capstone/output_video.mp4")
frames = []
timestamps = []
count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if count % 5 == 0:
        frames.append(frame)
        timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC))
    count += 1

# Load chapter data from the JSON file
with open("output_chapters.json", "r") as chapters_file:
    chapters = json.load(chapters_file)

# Extract text from frames using OCR
text_frames = []
for i, frame in enumerate(frames):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    if text:
        text_frames.append((text, i, timestamps[i]))

# Function to find the chapter for a given timestamp
def find_chapter(timestamp):
    for chapter in chapters:
        start_time = chapter["start time"]
        end_time = chapter["end time"]
        if start_time <= timestamp <= end_time:
            return chapter
    return None

# Function to remove special characters using regular expressions
def remove_special_characters(text):
    # Define a regular expression pattern to match non-alphanumeric characters
    pattern = re.compile(r'[^a-zA-Z0-9\s]+')
    # Use the pattern to replace non-alphanumeric characters with whitespace
    clean_text = re.sub(pattern, ' ', text)
    return clean_text

# Extract OCR words for each chapter, remove special characters, and use a set to avoid duplicates
chapter_ocr_data = {}
for text_frame in text_frames:
    text, frame_number, timestamp = text_frame
    chapter = find_chapter(timestamp / 1000)  # Convert timestamp to seconds
    if chapter:
        chapter_num = chapter["chapter number"]
        if chapter_num not in chapter_ocr_data:
            chapter_ocr_data[chapter_num] = {
                "start_time": chapter["start time"],
                "end_time": chapter["end time"],
                "words": set()  # Use a set to avoid duplicates
            }
        cleaned_text = remove_special_characters(text)
        chapter_ocr_data[chapter_num]["words"].update(cleaned_text.split())  # Add cleaned words to the set

# Prepare the data for JSON
json_data = []
for chapter_num, data in chapter_ocr_data.items():
    chapter_info = {
        "Chapter": chapter_num,
        "Start Time": data["start_time"],
        "End Time": data["end_time"],
        "Words": list(data["words"])  # Convert set to a list for JSON serialization
    }
    json_data.append(chapter_info)

# Write the data to a JSON file
with open("ocr_chapter_timestamp.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)

print("OCR words data has been written to ocr_words.json")
