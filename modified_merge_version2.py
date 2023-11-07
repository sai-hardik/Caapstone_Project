import json
from datetime import datetime

# Read the sorted_top_chapters.json and auto_summary.json files
with open('sorted_top_chapters.json', 'r') as f:
    sorted_top_chapters = json.load(f)

with open('6nzgofzpt4-a3b0-4479-84c5-b8301053f860_chapters.json', 'r') as f:
    auto_summary = json.load(f)

# Loop through the timestamps in the sorted_top_chapters.json file
output = []
gist_count = {}
for chapter in sorted_top_chapters:
    start = datetime.fromtimestamp(chapter['start'])
    end = datetime.fromtimestamp(chapter['end'])
    overlap = False

    # Check if the timestamps overlap with any of the timestamps in the auto_summary.json file
    for summary in auto_summary:
        summary_start = datetime.fromtimestamp(summary['start'])
        summary_end = datetime.fromtimestamp(summary['end'])
        if start <= summary_end and end >= summary_start:
            overlap = True
            gist = summary['gist']
            if gist in gist_count:
                gist_count[gist] += 1
                gist += f'_{gist_count[gist]}'
            else:
                gist_count[gist] = 1
            output.append({
                'start': chapter['start'],
                'end': chapter['end'],
                'gist': gist
            })
            break

    # If the timestamps do not overlap, adding clip1, clip2, etc. in place of the gist
    if not overlap:
        output.append({
            'start': chapter['start'],
            'end': chapter['end'],
            'gist': 'clip'
        })

# Write the output JSON file
with open('final_timestamps.json', 'w') as f:
    json.dump(output, f, indent=4)