

# pip install youtube_dl



# from pytube import YouTube

# # URL of the YouTube video you want to download
# video_url = 'https://www.youtube.com/watch?v=VRB3ISdaFis'

# # Create a YouTube object
# yt = YouTube(video_url)

# # Get streams with resolution closest to 360p
# streams_360p = yt.streams.filter(res="360p")

# # Choose the first stream in the list (you can customize this)
# video_stream = streams_360p[0]

# # Download the video to the current directory
# video_stream.download()

# print("Video downloaded successfully!")
# from pytube import YouTube

# # URL of the YouTube video you want to download
# video_url = 'https://www.youtube.com/watch?v=VRB3ISdaFis'

# # Provide your YouTube credentials (email and password)
# username = 'newscapstoneproject@gmail.com'
# password = 'Capstone@project'

# # Create a YouTube object with authentication
# yt = YouTube(video_url, on_progress_callback=None, on_complete_callback=None, proxies=None, logging=True, allow_dash=True, age_restricted=True, api_key=None, client_id=None, client_secret=None, http_client=None, credentials=(username, password))

# # Get streams with resolution closest to 360p
# streams_360p = yt.streams.filter(res="360p")

# # Choose the first stream in the list (you can customize this)
# video_stream = streams_360p[0]

# # Download the video to the current directory
# video_stream.download()

# print("Video downloaded successfully!")



# from pytube import YouTube

# # URL of the YouTube video you want to download
# video_url = 'https://www.youtube.com/watch?v=VRB3ISdaFis'

# # Provide your YouTube credentials (email and password)
# username = 'newscapstoneproject@gmail.com'
# password = 'Capstone@project'

# # Create a YouTube object with age-restricted video URL
# yt = YouTube(video_url)

# # Login to YouTube using your credentials
# yt.login(username, password)

# # Get streams with resolution closest to 360p
# streams_360p = yt.streams.filter(res="360p")

# # Choose the first stream in the list (you can customize this)
# video_stream = streams_360p[0]

# # Download the video to the current directory
# video_stream.download()

# print("Video downloaded successfully!")


from pytube import YouTube

# URL of the YouTube video you want to download
video_url = 'https://www.youtube.com/watch?v=8r4MOyaLXnM'

# Create a YouTube object
yt = YouTube(video_url,
        use_oauth=True,
        allow_oauth_cache=True
)

# Get streams with resolution closest to 360p
streams_360p = yt.streams.filter(res="360p")

# Choose the first stream in the list (you can customize this)
video_stream = streams_360p[0]

# Download the video to the current directory
video_stream.download()

print("Video downloaded successfully!")