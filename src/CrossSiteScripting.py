# Cross-Site Scripting(XSS) 공격
# 악성 스크립트를 게시판 글(Stored XSS), URL파라미터나 폼입력(Reflected XSS), 
# 클라이언트 측 스크립트가 동적으로 페이지 내용 변경 시(DOM-DocumentObjectModel XSS)
# 웹사이트 사용자가 요청하여 웹서버 등에서 응답하면 사용자 PC에서 
# 악성 스크립트가 실행되어 세션 탈취, 웹사이트 변조, 악성 콘텐츠 리다이렉션

# 실제 운영 중인 서버에 테스트 또는 공격을 하는 행위는 법적인 책임이 따르므로 
# 개인용 테스트 서버 구축 또는 bWAPP, DVWA, WebGoat 등과 같은 웹취약점 테스트환경 구축을 통해 테스트
# @SKshieldus, XSS공격유형부터 보안대책까지, 2022.10, https://www.skshieldus.com/blog-security/security-trend-idx-06
# @SKshieldus, https://github.com/EQSTLab/CVE-2024-46538

import re
import html
from typing import List, Dict, Tuple, Optional, Union, Any, Callable

class XSSPrevention:
    def __init__(self):
        self.input_value = None
    
    def validateInput(self, input_value: Any) -> int:
        """입력값 필터링 -> 악성 스크립트("<scripts>") 삽입 방지"""
        # 특정 패턴(알파벳, 숫자, 밑줄 허용)을 정규표현식으로 검증하는 화이트리스트 방식
        # 이메일은 ^[\w\.-]+@[\w\.-]+\.\w+$
        if not re.match("^[a-zA-Z0-9_]+$", input_value):
            raise ValueError("This input value is invalid")
        return input_value

    def escapeHTMLOutput(self, input_value: str) -> str:
        """HTML 출력값에서 특수문자를 HTML 엔티티로 변환하여 인코딩 -> 입력값 무효화"""
        # <, >와 같이 스크립트에 쓰이는 특수문자가 입력되면 스크립트로 동작하여 공격 가능
        stringInput: List = ["<", ">", "'", '"', "(", ")"]
        htmlEntity: List = ["&lt;", "&gt;", "&quot;", "&#x27;", "&#40;", "&#41;"]

        # html.escape() 메서드(Python 내장함수)로 &, <, >, "를 기본적인 HTML 엔티티 처리
        encoded_value = html.escape(input_value)

        # 추가적인 특수문자를 매핑테이블을 통해 의미없는 일반 문자로 치환
        for char, entity in zip(stringInput, htmlEntity):
            encoded_value = encoded_value.replace(char, entity)

        return encoded_value
        
    def escapeJSOutput(self, input_value: str) -> str: 
        """JavaScript 출력값에서 특수문자를 이스케이프 처리하여 인코딩 -> 입력값 무효화"""
        # 자바스크립트에서 사용할 수 없는 특수문자
        stringInput: List = ["\\", "'", '"', "<", ">", "&"]
        javascriptEscape: List = ["\\\\", "\\'", '\\"', "\\x3C", "\\x3E", "\\x26"]

        # 이스케이프 처리
        for char, escape in zip(stringInput, javascriptEscape):
            encoded_value = input_value.replace(char, escape)

        return encoded_value

    def DOMPurify(self):
        """javacript
        element.innerHTML = userInput;
        element.textContext = userInput;

        var clean = DOMPurify.sanitize(userInput);
        element.innerHTML = clean;
        
        Content-Security-Policy: script-src 'self'
        """
        pass
