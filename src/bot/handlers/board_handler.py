from bot.handlers.handler_interface import CommandHandlerInterface
from factories.board_factory import BoardFactory
from telegram import Update
from telegram.ext import ContextTypes

class BoardHandler(CommandHandlerInterface):
    """Board 명령어 핸들러"""

    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            # 명령어 인자에서 게시판 유형과 키워드 추출
            board_type = context.args[0] if len(context.args) > 0 else "컴공공지"
            keyword = context.args[1] if len(context.args) > 1 else None

            print(f"[DEBUG] 요청된 게시판 유형: {board_type}, 키워드: {keyword}")  # 디버깅

            # Factory를 통해 게시판 클래스 가져오기
            board = BoardFactory.get_board_source(board_type)
            print(f"[DEBUG] 반환된 게시판 인스턴스: {board}")  # 디버깅

            # 데이터 가져오기
            posts = board.fetch_posts(keyword=keyword)
            print(f"[DEBUG] 반환된 게시물 데이터: {posts}")  # 디버깅

            # 게시물이 있는 경우 출력, 없는 경우 메시지 출력
            if posts:
                for post in posts:
                    await update.message.reply_text(
                        f"number: {post['number']}\n"
                        f"title: {post['title']}\n"
                        f"author: {post['author']}\n"
                        f"views: {post['views']}\n"
                        f"date: {post['date']}"
                    )
            else:
                await update.message.reply_text("해당 키워드와 일치하는 게시물이 없습니다.")
        except ValueError as e:
            print(f"[ERROR] ValueError: {e}")  # 디버깅
            await update.message.reply_text(str(e))
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}")  # 디버깅
            await update.message.reply_text("알 수 없는 오류가 발생했습니다.")
