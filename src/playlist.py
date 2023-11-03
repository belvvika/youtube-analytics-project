from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
from src.channel import Channel
from src.video import Video
import datetime

class PlayList(Channel, Video):
    load_dotenv()
    api_key = os.getenv('YOUTUBE_API')
    def __init__(self, video_id, channel_id, playlist_id) -> None:
        self.playlist_id = playlist_id

        super().__init__(video_id, channel_id)

        playlist_videos = self.get_service().playlistItems().list(playlistId=playlist_id, part='contentDetails', maxResults=50).execute()
        '''получение данных по плейлистам канала'''

        self.title = playlist_videos['items'][0]
        self.url = f'https://www.youtube.com/watch?v=WNpfcqhNGhM&list={playlist_videos}'

        video_statistic = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        self.like_count = video_statistic['items'][0]['statistics']['likeCount']

        self.video_list = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
    @classmethod
    def get_service(cls):
        youtube_api_key = cls.api_key
        youtube = build('youtube', 'v3', developerKey=youtube_api_key)
        return youtube

    @property
    def total_duration(self):
        for video in video_statistic['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            return duration

    def show_best_video(self):
        return self.like_count