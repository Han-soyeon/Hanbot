import os
import sys
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

# src 디렉토리를 모듈 경로로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
src_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if src_root not in sys.path:
    sys.path.insert(0, src_root)

# 디버깅용 경로 출력
print("Updated sys.path:", sys.path)

# 핸들러 임포트
from src.bot.handlers.start_handler import StartHandler
from src.bot.handlers.board_handler import BoardHandler
from src.bot.handlers.report_handler import ReportHandler

class TelegramBotHandler:
    def __init__(self, token):
        """Telegram Bot 초기화"""
        self.app = Application.builder().token(token).build()
        self.setup_handlers()

    def setup_handlers(self):
        """핸들러를 Application에 추가"""
        self.app.add_handler(CommandHandler("start", StartHandler().handle))
        self.app.add_handler(CommandHandler("board", BoardHandler().handle))
        self.app.add_handler(CommandHandler("report", ReportHandler().handle))

    def run(self):
        """봇 실행"""
        self.app.run_polling()


if __name__ == "__main__":
    # 환경 변수 로드
    load_dotenv()
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    if not TOKEN:
        print("텔레그램 봇 토큰이 설정되지 않았습니다. .env 파일을 확인하세요.")
    else:
        bot = TelegramBotHandler(TOKEN)
        bot.run()
