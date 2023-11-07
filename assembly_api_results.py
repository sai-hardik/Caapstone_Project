# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:40:49 2023

@author: babut
"""

import requests
import json
import pprint
import sys
import string
#from api_secrets import API_KEY_ASSEMBLYAI
auth_key = '2f7d2ca034c5427e81a225a22e70c0ee'

upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'


headers_auth_only = {"authorization": auth_key}

headers = {
    "authorization": auth_key,
    "content-type":"application/json"
    }

CHUNK_SIZE = 5_242_880

def upload(filename):
    def read_file(filename):
        with open(filename, 'rb') as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint,
                                    headers=headers_auth_only, 
                                    data=read_file(filename))
    pprint.pprint(upload_response.json())
    return upload_response.json()['upload_url'] 


def transcribe(audio_url,auto_chapters=False):
    transcript_request = {
        'audio_url': audio_url,
        'auto_chapters': 'True' if auto_chapters else 'False'
    } 

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    pprint.pprint(transcript_response.json())
    return transcript_response.json()['id']

# def transcribe(audio_url, auto_chapters=False):
#     transcript_request = {
#         'audio_url': audio_url,
#         'auto_chapters': 'True' if auto_chapters else 'False'
#     }

#     transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
#     response_json = transcript_response.json()
#     pprint.pprint(response_json)

#     transcript_id = response_json.get('id', None)
#     if transcript_id:
#         print(f'Transcript ID: {transcript_id}')
#     else:
#         print('Failed to retrieve transcript ID')

#     return transcript_id

        
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    
    if polling_response.json()['status'] == 'completed':
        filename = transcript_id + '.txt'
        with open(filename, 'w') as f:
            f.write(polling_response.json()['text'])
        
        text_filename = transcript_id + '_chapters.json'
        with open(text_filename, 'w') as f:
            chapters = polling_response.json()['chapters']
            for chapter in chapters:
                chapter['start'] /= 1000  # convert milliseconds to seconds
                chapter['end'] /= 1000  # convert milliseconds to seconds
            json.dump(chapters, f, indent=4)
        
        print('Transcript saved')              




if __name__ == "__main__":
    filename = 'output.mp3'
    #audio_url = upload(filename)
    audio_url = 'https://cdn.assemblyai.com/upload/deefca5b-24f2-451b-b41b-ddbb8eab78f0'

    #transcript_id = transcribe(audio_url,auto_chapters=True)
    transcript_id = '6nshi9eo39-5ff2-467b-aca9-822871c7fca5'
    poll(transcript_id)
    
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python new_auto_chapter_summary.py <filename>")
#         sys.exit(1)

#     filename = sys.argv[1]
#     audio_url = upload(filename)
#     transcript_id = transcribe(audio_url, auto_chapters=True)
    
#     if transcript_id:
#         print(f"Polling transcript with ID: {transcript_id}")
#         poll(transcript_id)
#     else:
#         print('Failed to retrieve transcript ID')