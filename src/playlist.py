from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

class PlayList():
    load_dotenv()
    api_key = os.getenv('YOUTUBE_API')
    def __init__(self, playlist) -> None:
        self.playlist = playlist
        playlists = self.get_service().playlists().list(channelId=channel_id, part='contentDetails,snippet', maxResults=50).execute()
        self.title = playlists['items'][0]
        self.url = f'https://www.youtube.com/watch?v=WNpfcqhNGhM&list={playlist}'
        self.duration = playlists['items']['contentDetails']['duration']
        video_statistic = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        self.like_count = video_statistic['items'][0]['statistics']['likeCount']

    @classmethod
    def get_service(cls):
        youtube_api_key = cls.api_key
        youtube = build('youtube', 'v3', developerKey=youtube_api_key)
        return youtube

    @property
    def total_duration(self):
        self.duration

    def show_best_video(self):
        pass