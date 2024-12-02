# src/factories/board_factory.py

class BoardFactory:
    _boards = {}  # 등록된 게시판 클래스 저장소

    @classmethod
    def register_default_boards(cls):
        """
        기본 게시판 클래스를 등록
        """
        from boards.ce_board import ComputerScienceBoard

        # 기존 컴공 공지만 등록
        cls.register_board("컴공공지", ComputerScienceBoard)

    @classmethod
    def register_board(cls, board_type: str, board_class):
        """
        게시판 클래스를 등록
        :param board_type: 게시판 유형 이름 (예: "컴공공지")
        :param board_class: 게시판 클래스
        """
        if board_type in cls._boards:
            print(f"[WARNING] 이미 등록된 게시판 유형입니다: {board_type}, 기존 클래스를 대체합니다.")
        cls._boards[board_type] = board_class
        print(f"[DEBUG] 등록된 게시판: {board_type} -> {board_class}")

    @classmethod
    def get_board_source(cls, board_type: str):
        """
        요청한 게시판 유형에 따라 적절한 클래스 반환
        :param board_type: 게시판 유형 이름
        :return: 게시판 클래스 인스턴스
        """
        print(f"[DEBUG] 요청된 게시판 유형: {board_type}")
        print(f"[DEBUG] 현재 저장된 게시판 목록: {cls._boards}")
        if board_type in cls._boards:
            board_class = cls._boards[board_type]
            print(f"[DEBUG] 반환된 게시판 클래스: {board_class}")
            instance = board_class()
            print(f"[DEBUG] 생성된 게시판 인스턴스: {instance}")
            return instance
        raise ValueError(f"지원하지 않는 게시판 유형입니다: {board_type}")
