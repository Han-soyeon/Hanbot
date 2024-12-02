# src/bot/handlers/report_handler.py
# 확장성 추가 파일
from bot.handlers.handler_interface import CommandHandlerInterface
from factories.report_factory import ReportFactory
from factories.board_factory import BoardFactory
from telegram import Update
from telegram.ext import ContextTypes
import os

class ReportHandler(CommandHandlerInterface):
    """Report 명령어 핸들러"""

    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            # 명령어 형식 검증
            if len(context.args) < 2:
                await update.message.reply_text(
                    "명령어 형식이 잘못되었습니다. 예시: /report excel 컴공공지"
                )
                return

            # 보고서 및 게시판 유형 파라미터
            report_type = context.args[0].lower()
            board_type = context.args[1]
            keyword = context.args[2] if len(context.args) > 2 else None

            # 게시판 데이터 가져오기
            board = BoardFactory.get_board_source(board_type)
            posts = board.fetch_posts(keyword=keyword)

            if posts:
                # 보고서 생성기 가져오기
                report = ReportFactory.get_report_generator(report_type)
                # 파일 확장자 결정
                file_extension = report_type if report_type != "excel" else "xlsx"
                file_path = os.path.join("reports", f"{board_type}_report.{file_extension}")
                
                # 보고서 생성
                report.generate(posts, file_path)

                # 응답 메시지에서 경로를 제외하고 파일 이름만 출력하도록 변경
                file_name = f"{board_type}_report.{file_extension}"
                await update.message.reply_text(
                    f"{report_type.upper()} 보고서가 생성되었습니다: {file_name}"
                )
            else:
                await update.message.reply_text("보고서를 생성할 데이터가 없습니다.")
        except ValueError as e:
            await update.message.reply_text(str(e))
        except FileNotFoundError as e:
            await update.message.reply_text(f"파일 생성 중 오류가 발생했습니다: {str(e)}")
        except Exception as e:
            await update.message.reply_text("알 수 없는 오류가 발생했습니다. 관리자에게 문의하세요.")
            print(f"Unexpected error: {e}")
