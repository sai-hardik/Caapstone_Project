# import json

# # Load timestamps from the JSON file
# with open("face_detection_timestamps.json", "r") as file:
#     timestamps = json.load(file)

# # Convert timestamps to seconds for easier calculations
# timestamps_in_seconds = []
# for timestamp in timestamps:
#     hh, mm, ss = map(int, timestamp.split(":"))
#     total_seconds = hh * 3600 + mm * 60 + ss
#     timestamps_in_seconds.append(total_seconds)

# # Initialize variables
# start = timestamps_in_seconds[0]
# end = timestamps_in_seconds[0]
# index = 1

# # Initialize list to store chapters
# chapters = []

# # Process the timestamps
# while index < len(timestamps_in_seconds):
#     if 120 < abs(start - end):
#         while timestamps_in_seconds[index] - end < 15 and abs(start - end) < 240:
#             end = timestamps_in_seconds[index]
#             index += 1
#         # Store the start and end time for the chapter
#         chapters.append(
#             {
#                 "chapter number": len(chapters) + 1,
#                 "start time": start,
#                 "end time": end,
#                 "duration of chapter": end - start,
#             }
#         )
#         # Start and end for the next chapter
#         start = timestamps_in_seconds[index]
#         end = timestamps_in_seconds[index]
#     else:
#         end = timestamps_in_seconds[index]
#         index += 1

# # If there are any remaining timestamps, process them as needed

# # If you want to convert back to hh:mm:ss format, you can do that here

# # Write the output to a JSON file
# with open("output_chapters.json", "w") as outfile:
#     json.dump(chapters, outfile, indent=4)


import json

# Load timestamps from the JSON file
with open("face_detection_timestamps.json", "r") as file:
    timestamps = json.load(file)

# Convert timestamps to seconds for easier calculations
timestamps_in_seconds = []
for timestamp in timestamps:
    hh, mm, ss = map(int, timestamp.split(":"))
    total_seconds = hh * 3600 + mm * 60 + ss
    timestamps_in_seconds.append(total_seconds)

# Initialize variables
start = timestamps_in_seconds[0]
end = timestamps_in_seconds[0]
index = 1

# Initialize list to store chapters
chapters = []

# Process the timestamps
while index < len(timestamps_in_seconds):
    if 120 < abs(start - end):
        while index < len(timestamps_in_seconds) and timestamps_in_seconds[index] - end < 15 and abs(start - end) < 240:
            end = timestamps_in_seconds[index]
            index += 1
        # Store the start and end time for the chapter
        chapters.append(
            {
                "chapter number": len(chapters) + 1,
                "start time": start,
                "end time": end,
                "duration of chapter": end - start,
            }
        )
        # Check if there are more timestamps
        if index < len(timestamps_in_seconds):
            # Start and end for the next chapter
            start = timestamps_in_seconds[index]
            end = timestamps_in_seconds[index]
    else:
        end = timestamps_in_seconds[index]
        index += 1

# If there are any remaining timestamps, process them as needed

# If you want to convert back to hh:mm:ss format, you can do that here

# Write the output to a JSON file
with open("output_chapters.json", "w") as outfile:
    json.dump(chapters, outfile, indent=4)
