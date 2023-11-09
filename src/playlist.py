import isodate
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
from src.channel import Channel
from src.video import Video
import datetime
import isodate
class PlayList(Channel, Video):
    load_dotenv()
    api_key = os.getenv('YOUTUBE_API')
    def __init__(self, video_id, channel_id, playlist_id) -> None:
        self.playlist_id = playlist_id

        super().__init__(video_id)
        super().__init__(channel_id)

        playlist_videos = self.get_service().playlistItems().list(playlistId=playlist_id, part='contentDetails', maxResults=50).execute()
        '''получение данных по плейлистам канала'''

        self.video_statistic = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',id=video_id).execute()

        self.title = playlist_videos['items'][0]
        self.url = f'https://www.youtube.com/watch?v=WNpfcqhNGhM&list={playlist_videos}'
    def get_service(cls):
        youtube_api_key = cls.api_key
        youtube = build('youtube', 'v3', developerKey=youtube_api_key)
        return youtube

    @property
    def total_duration(self):
        if self.video_statistic is not None and 'items' in self.video_statistic:
            duration = datetime.timedelta()
            for video in video_statistic['items']:
                iso_8601_duration = video['contentDetails']['duration']
                duration = isodate.parse_duration(iso_8601_duration)
        return duration

    def show_best_video(self):
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        for video_id in video_ids:
            video_statistic = get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
            like_count: int = video_statistic['items'][0]['statistics']['likeCount']
        return like_count