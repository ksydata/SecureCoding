import sys
sys.path.append("C:/SecureCoding/src")
from CrossSiteScripting import XSSPrevention

xssprev_object = XSSPrevention()
# 악성 스크립트 입력 예시
html_input = "<script>alert('XSS');</script>"
js_input = "var name = 'Melissa'; alert(name);"

# <script> alert('XSS'); </script>가 안전하게 HTML 엔티티로 변환
escaped_html = xssprev_object.escapeHTMLOutput(input_value = html_input)
print(f"Escaped HTML Output: {escaped_html}")
    # Escaped HTML Output: &lt;script&gt;alert&#40;&#x27;XSS&#x27;&#41;;&lt;/script&gt;

escaped_js = xssprev_object.escapeJSOutput(input_value = js_input)
print(f"Escaped JavaScript Output: {escaped_js}")
    # Escaped JavaScript Output: var name = \'Melissa\'; alert(name);
