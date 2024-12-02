# src/bot/handlers/start_handler.py
from bot.handlers.handler_interface import CommandHandlerInterface
from telegram import Update
from telegram.ext import ContextTypes

class StartHandler(CommandHandlerInterface):
    """Start 명령어 핸들러"""
    
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "안녕하세요! 공지사항 알림 봇입니다.\n명령어 예시:\n"
            "/board 컴공공지\n/report excel 컴공공지\n/report pdf 컴공공지"
        )
