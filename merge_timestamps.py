import json

# Load the contents of the two JSON files
with open('sorted_top_chapters.json', 'r') as f:
    output_chapters = json.load(f)

with open('6nshi9eo39-5ff2-467b-aca9-822871c7fca5_chapters.json', 'r') as f:
    new_auto_summary = json.load(f)

# Create a list to store the new timestamps
new_timestamps = []

# Loop through the timestamps in output_chapters
for timestamp in output_chapters:
    new_timestamps.append({
        'start': timestamp['start'],
        'end': timestamp['end'],
        'gist': ''
    })

    # Check if there are any overlapping timestamps in new_auto_summary
    for new_timestamp in new_auto_summary:
        if new_timestamp['start'] >= timestamp['start'] and new_timestamp['start'] <= timestamp['end']:
            # If there is an overlap, add the gist from new_auto_summary to the new timestamp
            if new_timestamp['gist'] not in [t['gist'] for t in new_timestamps]:
                new_timestamps[-1]['gist'] = new_timestamp['gist']

# # Check for any timestamps in new_auto_summary that are not overlapping with output_chapters
# for new_timestamp in new_auto_summary:
#     overlap = False
#     for timestamp in output_chapters:
#         if new_timestamp['start'] >= timestamp['start'] and new_timestamp['start'] <= timestamp['end']:
#             overlap = True
#             break
#     if not overlap:
#         new_timestamps.append({
#             'start': int( new_timestamp['start']),
#             'end': int(new_timestamp['end']),
#             'gist': new_timestamp['gist']
#         })

# Write the new timestamps to a JSON file
with open('final_timestamps.json', 'w') as f:
    json.dump(new_timestamps, f,indent=None)




# Read data from timestamps.json file
with open('final_timestamps.json', 'r') as infile:
    data = json.load(infile)

# Function to add clip number if "gist" is empty
def add_clip_numbers(data):
    clip_number = 1
    for item in data:
        if item["gist"] == "":
            item["gist"] = f"Clip {clip_number}"
            clip_number += 1
    return data

# Add clip numbers to the JSON data
modified_data = add_clip_numbers(data)

# Write modified data back to timestamps.json file
with open('final_timestamps.json', 'w') as outfile:
    json.dump(modified_data, outfile, indent=4)

print("Modified JSON data written back to timestamps.json")













# # Load data from final_timestamps.json
# with open('final_timestamps.json', 'r') as infile:
#     data = json.load(infile)

# # Remove items where "gist" is empty
# data = [item for item in data if item["gist"] != ""]

# # Sort data by "start" key
# sorted_data = sorted(data, key=lambda x: x["start"])

# # Write sorted and filtered data to a new JSON file
# with open('final_output.json', 'w') as outfile:
#     json.dump(sorted_data, outfile, indent=4)

# print("Data written to final_output.json.")


