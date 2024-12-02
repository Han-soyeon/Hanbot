# src/boards/board_source.py
from abc import ABC, abstractmethod

class BoardSource(ABC):
    @abstractmethod
    def fetch_posts(self):
        """공지사항 데이터를 가져오는 메서드"""
        pass
