# import json

# # Load the sorted_top_chapters.json file
# with open('sorted_top_chapters.json', 'r') as f:
#     sorted_chapters = json.load(f)

# # Load the new_auto_summary.json file
# with open('auto_summary.json', 'r') as f:
#     auto_summary = json.load(f)

# # Create a new list to store the timestamps and gist
# new_list = []

# # Create a set to store the used clip numbers
# used_clips = set()

# # Loop through each chapter in sorted_chapters
# for chapter in sorted_chapters:
#     # Get the start and end timestamps
#     start = chapter['start']
#     end = chapter['end']
#     # Check if there are overlapping timestamps in auto_summary
#     for summary in auto_summary:
#         if start <= summary['end'] and end >= summary['start']:
#             # If there is an overlap, add the gist to the new list
#             new_list.append({
#                 'start': start,
#                 'end': end,
#                 'gist': summary['gist']
#             })
#             break
#     else:
#         # If there is no overlap, add clip1, clip2, clip3, etc. as the gist to the new list
#         clip_num = len(new_list) + 1
#         while f'clip{clip_num}' in used_clips:
#             clip_num += 1
#         used_clips.add(f'clip{clip_num}')
#         new_list.append({
#             'start': start,
#             'end': end,
#             'gist': f'clip{clip_num}'
#         })

# # Write the new list to a JSON file
# with open('new_file.json', 'w') as f:
#     json.dump(new_list, f)











import json

# Load the sorted_top_chapters.json file
with open('sorted_top_chapters.json', 'r') as f:
    sorted_chapters = json.load(f)

# Load the new_auto_summary.json file
with open('6nsj0yoa5h-d26a-4ca2-9903-124832515fd1_chapters.json', 'r') as f:
    auto_summary = json.load(f)

# Create a new list to store the timestamps and gist
new_list = []

# Create a set to store the used clip names
used_clips = set()

# Loop through each chapter in sorted_chapters
for chapter in sorted_chapters:
    # Get the start and end timestamps
    start = chapter['start']
    end = chapter['end']
    # Check if there are overlapping timestamps in auto_summary
    for summary in auto_summary:
        if start <= summary['end'] and end >= summary['start']:
            # If there is an overlap, add the gist to the new list
            new_list.append({
                'start': start,
                'end': end,
                'gist': summary['gist']
            })
            break
    else:
        # If there is no overlap, add a unique clip name as the gist to the new list
        clip_num = len(new_list) + 1
        while f'clip{clip_num}' in used_clips:
            clip_num += 1
        used_clips.add(f'clip{clip_num}')
        new_list.append({
            'start': start,
            'end': end,
            'gist': f'clip{clip_num}'
        })

# Check if there are any duplicate gists and replace them with unique clip names
gist_counts = {}
for chapter in new_list:
    gist = chapter['gist']
    if gist in gist_counts:
        clip_num = gist_counts[gist] + 1
        while f'clip{clip_num}' in used_clips:
            clip_num += 1
        used_clips.add(f'clip{clip_num}')
        chapter['gist'] = f'clip{clip_num}'
    else:
        gist_counts[gist] = 1

# Write the new list to a JSON file
with open('final_timestamps.json', 'w') as f:
    json.dump(new_list, f, indent=4)



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import json
# from datetime import datetime, timedelta

# # Load the existing output file and extract the gists that have already been used and the start and end timestamps
# with open('new_file_V2.json', 'r') as f:
#     output = json.load(f)
#     used_gists = set(summary['gist'] for summary in output)
#     # start_time = datetime.fromisoformat(str(output[-1]['start']))
#     # end_time = datetime.fromisoformat(str(output[-1]['end']))
#     start_time = output['start']
#     end_time = output['end']

# # Load the auto_summary.json file and extract the gists that meet the criteria of end - start > 180, have not been used before, and whose start timestamps are not in between the start and end timestamps of the output file
# with open('auto_summary.json', 'r') as f:
#     summaries = json.load(f)
#     new_summaries = []
#     for summary in summaries:
#         start = datetime.fromisoformat(str(summary['start']))
#         end = datetime.fromisoformat(str(summary['end']))
#         if (end - start) > timedelta(seconds=120) and summary['gist'] not in used_gists and start < start_time or start > end_time:
#             new_summaries.append(summary)
#             used_gists.add(summary['gist'])

# # Append the new gists to the existing output file and save it
# with open('new_file_V2.json', 'w') as f:
#     output.extend(new_summaries)
#     json.dump(output, f)