# src/boards/ce_board.py
from boards.board_source import BoardSource

class ComputerScienceBoard(BoardSource):
    def fetch_posts(self, keyword=None):
        """컴공 공지 데이터를 반환 (키워드 필터링 가능)"""
        data = [
            {
                "number": "948",
                "title": "2025 Pre캡스톤디자인 설명회 자료 및 오픈채팅방 안내 (예비4학년 필수)",
                "author": "컴퓨터공학과",
                "views": "754",
                "date": "2024-11-27"
            },
            {
                "number": "947",
                "title": "2024학년도 푸른등대 삼성기부장학금 신규 장학생 선발",
                "author": "컴퓨터공학과",
                "views": "753",
                "date": "2024-11-12"
            },
            {
                "number": "946",
                "title": "2024학년도 컴퓨터공학과 포트폴리오경진대회 운영 안내",
                "author": "컴퓨터공학과",
                "views": "937",
                "date": "2024-11-12"
            },
            {
                "number": "945",
                "title": "2024학년도 제2학기 중간강의점검 실시 안내",
                "author": "컴퓨터공학과",
                "views": "2,036",
                "date": "2024-10-16"
            },
            {
                "number": "944",
                "title": "2024학년도 2학기 개강후 수강취소(수강철회) 안내",
                "author": "컴퓨터공학과",
                "views": "2,124",
                "date": "2024-10-08"
            },
            {
                "number": "943",
                "title": "2024년도 하반기 연구실 정기 안전교육 실시 안내 (필수)",
                "author": "컴퓨터공학과",
                "views": "3,720",
                "date": "2024-09-27"
            },
        ]

        # 키워드 필터링
        if keyword:
            data = [
                post for post in data 
                if keyword in post["title"] or keyword in post["author"]
            ]

        return data
