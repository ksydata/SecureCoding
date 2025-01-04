import sys
sys.path.append("C:/SecureCoding/src")
from CrossSiteScripting import XSSPrevention

xssprev_object = XSSPrevention()
html_input = "<script>alert('XSS');</script>"

escaped_html = xssprev_object.escapeHTMLOutput(input_value = html_input)
print(f"Escaped HTML Output: {escaped_html}")
# Escaped HTML Output: &lt;script&gt;alert$#40;&#x27;XSS&#x27;&#41;;&lt;/script&gt;
