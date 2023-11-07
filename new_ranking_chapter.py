# # -*- coding: utf-8 -*-
# """
# Created on Tue Oct 31 23:00:49 2023

# @author: babut
# """




# import json
# from collections import Counter
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# # Read data from ocr.json
# with open('ocr_chapter_timestamp.json', 'r') as file:
#     data = json.load(file)

# # Read the transcript from transcript.txt
# with open('6nr9eox5kf-4108-4f51-a126-19a919f0d030.txt', 'r') as transcript_file:
#     transcript_text = transcript_file.read()

# # Tokenize and remove stopwords from the transcript
# stop_words = set(stopwords.words('english'))
# transcript_words = word_tokenize(transcript_text.lower())
# filtered_transcript_words = [word for word in transcript_words if word.isalpha() and word not in stop_words]

# # Calculate word frequencies
# word_frequencies = Counter(filtered_transcript_words)

# # Calculate ranks for each keyword in each chapter
# chapter_ranks = []
# for chapter in data:
#     chapter_words = chapter['Words']
#     total_words_in_chapter = len(chapter_words)
#     chapter_rank = 0
    
#     for word in chapter_words:
#         word_frequency = word_frequencies.get(word.lower(), 0)
#         word_rank = word_frequency / total_words_in_chapter
#         chapter_rank += word_rank
    
#     chapter_ranks.append({
#         'Chapter': chapter['Chapter'],
#         'Start Time': chapter['Start Time'],
#         'End Time': chapter['End Time'],
#         'Rank': chapter_rank
#     })

# # Sort chapters by rank
# sorted_chapter_ranks = sorted(chapter_ranks, key=lambda x: x['Rank'], reverse=True)

# # Output the sorted chapter ranks as JSON
# with open('new_sorted_chapter_ranks.json', 'w') as outfile:
#     json.dump(sorted_chapter_ranks, outfile, indent=4)

# print("Chapter ranks, Start Time, End Time calculated, sorted, and saved to new_sorted_chapter_ranks.json.")

import json
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Read data from ocr.json
with open('ocr_chapter_timestamp.json', 'r') as file:
    data = json.load(file)

# Read the transcript from transcript.txt
with open('6nshi9eo39-5ff2-467b-aca9-822871c7fca5.txt', 'r') as transcript_file:
    transcript_text = transcript_file.read()

# Tokenize and remove stopwords from the transcript
stop_words = set(stopwords.words('english'))
transcript_words = word_tokenize(transcript_text.lower())
filtered_transcript_words = [word for word in transcript_words if word.isalpha() and word not in stop_words]

# Calculate word frequencies
word_frequencies = Counter(filtered_transcript_words)

# Calculate ranks for each keyword in each chapter
chapter_ranks = []
for chapter in data:
    chapter_words = chapter['Words']
    total_words_in_chapter = len(chapter_words)
    chapter_rank = 0
    
    for word in chapter_words:
        word_frequency = word_frequencies.get(word.lower(), 0)
        word_rank = word_frequency / total_words_in_chapter
        chapter_rank += word_rank
    
    chapter_ranks.append({
        'Chapter': chapter['Chapter'],
        'start': chapter['Start Time'],
        'end': chapter['End Time'],
        'Rank': chapter_rank
    })

# Sort chapters by rank
sorted_chapter_ranks = sorted(chapter_ranks, key=lambda x: x['Rank'], reverse=True)

# Select top n/2 chapters based on rank
n = len(sorted_chapter_ranks)
top_chapters = sorted_chapter_ranks[:n//2]

# Sort top chapters by chapter number in ascending order
sorted_top_chapters = sorted(top_chapters, key=lambda x: x['Chapter'])

# Output the sorted top chapters as JSON
with open('sorted_top_chapters.json', 'w') as outfile:
    json.dump(sorted_top_chapters, outfile, indent=4)

print("Top n/2 chapters based on rank calculated, sorted, and saved to new_sorted_top_chapters.json.")



