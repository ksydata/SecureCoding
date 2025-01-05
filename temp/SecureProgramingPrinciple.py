# @홍재희, 보안 프로그래밍의 이해, 모던코딩가이드, 2024.11.

class SecurePrograming:
    def __init__(self):
        pass
    
    def performAction(self, user):
        """최소 접근권한(읽기)의 원칙"""
        if user.has_permission("read_data"):
            pass
        elif user.has_permission("write_data"):
            pass
        else: 
            raise PermissionError

    def defenseInDepth(self):
        """여러 겹의 보안 계층(호스트 수준, 애플리케이션 수준, DB 수준 등) 구축하여 심층 방어
        Pseudo code
        if level is Network:
            네트워크 레벨에서는 HTTPS를 사용
            app.run(ssl_context = "adhoc")
        then level is Application:
            애플리케이션 레벨에서는 입력 검증
            def validation_input(data) 
        then level is Database:
            파라미터화된 쿼리를 사용
            def get_user(username):
                cursor.execute(
                    "SELECT * FROM users WHERE username = ?",
                    (username,)
                )
        """
        pass

    def secureByDefault(self):
        """웹 프레임워크에서 Cross-Site Request Forgery 보호 기본적인 설정으로 활성화
        @CSRF Protection, https://flask-wtf.readthedocs.io/en/0.15.x/csrf/"""
        from flask import Flask
        from flask_wtf.csrf import CSRFProtect
        app = Flask(__name__)
        csrf = CSRFProtect()
        csrf.init_app(app)

    def properErrorHandling(self, result):
        """디버그 정보나 스택 트레이스와 같은 상세정보는 로그에만 기록하고 사용자에게 일반적인 메시지 반환"""
        import logging
        # from logging.handlers import RotatingFileHandler
        try:
            return result
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return "An error occurred. Please try again later."
        