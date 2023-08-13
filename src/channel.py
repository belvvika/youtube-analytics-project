import json
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key = 'AIzaSyCYh8Sykk8-QRgUXGhIIL8nCURX6iQNxFI'

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id


    def get_info(self):
        """Получает и возвращает информацию о канале"""

        service = build('youtube', 'v3', developerKey=self.api_key)
        response = service.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return response

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(self.get_info(), indent=4))