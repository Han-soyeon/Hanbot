# src/reports/report_interface.py
from abc import ABC, abstractmethod

class ReportInterface(ABC):
    @abstractmethod
    def generate(self, data, file_path: str):
        """데이터를 기반으로 보고서를 생성"""
        pass
