import isodate
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import datetime
import isodate
class PlayList:
    load_dotenv()
    api_key = os.getenv('YOUTUBE_API')

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id

        self.playlist_info = self.get_service().playlists().list(id=playlist_id, part='contentDetails, snippet', ).execute()

        self.playlist_videos = self.get_service().playlistItems().list(playlistId=playlist_id,part='contentDetails, snippet',maxResults=50).execute()

        self.title = self.playlist_info['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'

        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]

        self.video_statistic = self.get_service().videos().list(part='contentDetails,statistics',id=','.join(self.video_ids)).execute()

    def get_service(cls):
        youtube_api_key = cls.api_key
        youtube = build('youtube', 'v3', developerKey=youtube_api_key)
        return youtube

    @property
    def total_duration(self):
        '''
        возвращает суммарную длительность плейлиста
        '''
            total_duration = datetime.timedelta()
            for video in self.video_statistic['items']:
                iso_8601_duration = video['contentDetails']['duration']
                duration = isodate.parse_duration(iso_8601_duration)
                totla_duration += datetime.timedelta(seconds=duration.total_seconds())
            return total_duration

    def show_best_video(self):
        '''
        возращает ссылку на самое популярное видео из плейлиста
        '''
        max_likes = 0
        max_likes_video_id = ''
        for item in self.video_statistic['items']:
            video_id = item['id']
            like_count = int(item['statistics']['likeCount'])
            if like_count > max_likes:
                max_likes = like_count
                max_likes_video_id = video_id
        return f'https://youtu.be/{max_likes_video_id}'
