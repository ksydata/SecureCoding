# Cross-Site Scripting(XSS) 공격
# 악성 스크립트를 게시판 글(Stored XSS), URL파라미터나 폼입력(Reflected XSS), 
# 클라이언트 측 스크립트가 동적으로 페이지 내용 변경 시(DOM XSS)
# 세션 탈취, 웹사이트 변조, 악성 컨텐츠 리다이렉션

import re
import html

class CrossSiteScriptingPrevention:
    def __init__(self):
        pass
    
    def validateInput(self):
        """입력값 검증(필터링)"""
        pass

    def escapeHTMLOutput(self):
        """HTML 출력값에서 특수문자를 HTML 엔티티로 변환하여 인코딩
        """
        pass        

    def escapeJSOutput(self): 
        """JavaScript 출력값에서 특수문자를 이스케이프 처리하여 인코딩"""
        pass