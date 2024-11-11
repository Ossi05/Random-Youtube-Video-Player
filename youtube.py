import random
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Create a youtube object
youtube = build('youtube', 'v3', developerKey=API_KEY)

"""
    Returns a random youtube video from a certain channel.
"""
def get_random_video(channel_id: str, max_video_results: int, video_duration: str):
    request = youtube.search().list(
        part = "snippet", 
        channelId = channel_id, 
        type = "video", 
        order = "date", 
        maxResults = max_video_results, 
        videoDuration = video_duration,
        )
    response = request.execute()
    random_video = random.choice(response['items'])
    return f"https://www.youtube.com/watch?v={random_video['id']['videoId']}"
