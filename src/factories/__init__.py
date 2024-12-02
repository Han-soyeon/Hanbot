from factories.board_factory import BoardFactory
from factories.report_factory import ReportFactory

# 게시판 클래스 등록
from boards.ce_board import ComputerScienceBoard
BoardFactory.register_board("컴공공지", ComputerScienceBoard)

# 보고서 클래스 등록
from reports.excel_report import ExcelReport
from reports.pdf_report import PDFReport
ReportFactory.register_report("excel", ExcelReport)
ReportFactory.register_report("pdf", PDFReport)
