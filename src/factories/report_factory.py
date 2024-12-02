from reports.excel_report import ExcelReport
from reports.pdf_report import PDFReport

class ReportFactory:
    _reports = {}  # 등록된 보고서 클래스 저장소

    @classmethod
    def register_report(cls, report_type: str, report_class):
        """
        보고서 클래스를 등록
        :param report_type: 보고서 유형 이름 (예: "excel", "pdf")
        :param report_class: 보고서 클래스
        """
        cls._reports[report_type] = report_class

    @classmethod
    def get_report_generator(cls, report_type: str):
        """
        보고서 형식에 따라 적절한 보고서 생성 클래스 반환
        :param report_type: 보고서 유형 이름
        :return: 보고서 생성 클래스 인스턴스
        """
        report_type = report_type.lower()
        if report_type in cls._reports:
            return cls._reports[report_type]()
        raise ValueError(f"지원하지 않는 보고서 형식입니다: {report_type}")


# 보고서 클래스를 등록
ReportFactory.register_report("excel", ExcelReport)
ReportFactory.register_report("pdf", PDFReport)
