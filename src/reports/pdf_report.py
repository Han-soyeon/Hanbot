import os
from fpdf import FPDF
from reports.report_interface import ReportInterface


class PDFReport(ReportInterface):
    def generate(self, data, file_path: str):
        """
        데이터를 PDF 파일로 저장
        :param data: 보고서에 들어갈 데이터 (리스트 형식)
        :param file_path: 저장할 파일 경로
        """
        self._validate_data(data)

        # 파일 경로가 없으면 디렉터리 생성
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        pdf = FPDF()
        pdf.add_page()

        # 폰트 설정
        try:
            font_path = self._get_font_path()
            pdf.add_font("NanumGothic", '', font_path, uni=True)
        except FileNotFoundError as e:
            print(f"[ERROR] {e}")
            return

        pdf.set_font("NanumGothic", size=12)

        # 제목
        pdf.cell(200, 10, txt="공지사항 보고서", ln=True, align='C')

        # 데이터 추가
        for idx, item in enumerate(data, start=1):
            pdf.cell(0, 10, txt=f"{idx}. 제목: {item['title']}", ln=True)
            pdf.cell(0, 10, txt=f"   작성자: {item['author']}", ln=True)
            pdf.cell(0, 10, txt=f"   조회수: {item['views']}", ln=True)
            pdf.cell(0, 10, txt=f"   날짜: {item['date']}", ln=True)
            pdf.cell(0, 10, txt="", ln=True)

        pdf.output(file_path, 'F')
        print(f"PDF 보고서가 {file_path}에 저장되었습니다.")

    def _validate_data(self, data):
        """데이터 유효성 검사"""
        if not data:
            raise ValueError("보고서에 데이터가 없습니다.")

    def _get_font_path(self):
        """폰트 파일 경로 반환"""
        font_dir = os.path.join(os.path.dirname(__file__), "../fonts")
        font_path = os.path.join(font_dir, "NanumGothic.ttf")
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"폰트 파일을 찾을 수 없습니다: {font_path}")
        return font_path
