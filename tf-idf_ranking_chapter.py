import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Read data from ocr.json
with open('ocr_chapter_timestamp.json', 'r') as file:
    data = json.load(file)

# Read the transcript from transcript.txt
with open('6nq31zxweo-3141-4e05-b08f-faee5e8872f3.txt', 'r') as transcript_file:
    transcript_text = transcript_file.read()

# Tokenize and remove stopwords from the transcript
stop_words = set(stopwords.words('english'))
transcript_words = word_tokenize(transcript_text.lower())
filtered_transcript_words = [word for word in transcript_words if word.isalpha() and word not in stop_words]
transcript_text = ' '.join(filtered_transcript_words)  # Join words back into a single string

# Calculate TF-IDF scores
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([transcript_text])

# Calculate TF-IDF scores for transcript words
transcript_tfidf_scores = dict(zip(tfidf_vectorizer.get_feature_names(), tfidf_matrix.toarray()[0]))

# Calculate ranks for each keyword in each chapter using TF-IDF scores
chapter_ranks = []
for chapter in data:
    chapter_words = chapter['Words']
    chapter_tfidf_sum = 0
    
    for word in chapter_words:
        word_tfidf_score = transcript_tfidf_scores.get(word.lower(), 0)
        chapter_tfidf_sum += word_tfidf_score
    
    chapter_ranks.append({
        'Chapter': chapter['Chapter'],
        'start': chapter['Start Time'],
        'end': chapter['End Time'],
        'Rank': chapter_tfidf_sum
    })

# Sort chapters by rank
sorted_chapter_ranks = sorted(chapter_ranks, key=lambda x: x['Rank'], reverse=True)

# Select top n/2 chapters based on rank
n = len(sorted_chapter_ranks)
top_chapters = sorted_chapter_ranks[:n//2]

# Sort top chapters by chapter number in ascending order
sorted_top_chapters = sorted(top_chapters, key=lambda x: x['Chapter'])

# Output the sorted top chapters as JSON
with open('sorted_top_chapters_tfidf.json', 'w') as outfile:
    json.dump(sorted_top_chapters, outfile, indent=4)

print("Top n/2 chapters based on TF-IDF rank calculated, sorted, and saved to sorted_top_chapters_tfidf.json.")
