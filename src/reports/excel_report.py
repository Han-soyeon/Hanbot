import os
import pandas as pd
from reports.report_interface import ReportInterface


class ExcelReport(ReportInterface):
    def generate(self, data, file_path: str):
        """
        데이터를 Excel 파일로 저장
        :param data: 보고서에 들어갈 데이터 (리스트 형식)
        :param file_path: 저장할 파일 경로
        """
        self._validate_data(data)

        # 파일 경로가 없으면 디렉터리 생성
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 데이터프레임 변환 및 저장
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False)
        print(f"Excel 보고서가 {file_path}에 저장되었습니다.")

    def _validate_data(self, data):
        """데이터 유효성 검사"""
        if not data:
            raise ValueError("보고서에 데이터가 없습니다.")
