from googleapiclient.discovery import build
import os
from dotenv import load_dotenv


class Video:
    load_dotenv()
    API_KEY = os.getenv('YOUTUBE_API')
    def __init__(self, video_id) -> None:
        self.video_id = video_id
        video_statistic = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        self.title =  video_statistic['items'][0]['snippet']['title']
        self.view_count= video_statistic['items'][0]['statistics']['viewCount']
        self.like_count = video_statistic['items'][0]['statistics']['likeCount']
        self.url = f'https://www.youtube.com/watch?v={video_id}'

    def __str__(self):
        return f'{self.title}'

    @classmethod
    def get_service(cls):
        youtube_api_key = cls.api_key
        youtube = build('youtube', 'v3', developerKey=youtube_api_key)
        return youtube


class PLVideo(Video):
    def __init__(self, video_id, play_list_id):
        super().__init__(video_id)
        self.play_list_id = play_list_id