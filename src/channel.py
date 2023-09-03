import json
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key = 'AIzaSyCYh8Sykk8-QRgUXGhIIL8nCURX6iQNxFI'

    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.__channel_id = channel_id
        youtube_channels_list = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics')
        self.__info_to_print = youtube_channels_list.execute()
        self.title = self.__info_to_print['items'][0]['snippet']['title']
        self.description = self.__info_to_print['items'][0]['snippet']['description']
        self.url = self.__info_to_print['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriberCount = self.__info_to_print['items'][0]['statistics']['subscriberCount']
        self.video_count = self.__info_to_print['items'][0]['statistics']['videoCount']
        self.viewCount = self.__info_to_print['items'][0]['statistics']['viewCount']

    def get_info(self):
        """Получает и возвращает информацию о канале"""

        service = build('youtube', 'v3', developerKey=self.api_key)
        response = service.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return response


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(self.get_info(), indent=4))


    @classmethod
    def get_service(cls):
        youtube_api_key = cls.api_key
        youtube = build('youtube', 'v3', developerKey=youtube_api_key)
        return youtube

    def to_json(self, filename):
        channel = {
            'channel_id': self.__channel_id,
            'title': self.title,
            'description' : self.description,
            'url' : self.url,
            'subscriberCount' : self.subscriberCount,
            'videoCount' : self.video_count,
            'viewCount': self.viewCount
        }
        with open(filename, 'w', encoding='UTF-8') as f:
            json.dump(channel, f, ensure_ascii=False)

    @property
    def channel_id(self):
        return self.channel_id