# src/bot/handlers/handler_interface.py
from abc import ABC, abstractmethod
from telegram import Update
from telegram.ext import ContextTypes

class CommandHandlerInterface(ABC):
    """명령어 핸들러 인터페이스"""
    
    @abstractmethod
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """명령어 처리 로직"""
        pass
