import os
import sys
import urllib.request

url = sys.argv[1]

if not url.endswith('/download'):
    url += '/download'

with urllib.request.urlopen(url) as response:
    md = response.read().decode(response.headers.get_content_charset())

with open("document.md", "w", encoding='utf-8') as f:
    f.write(md)

os.system('pandoc document.md --template pandoc-template.tex --pdf-engine=pdflatex --highlight=espresso -o document.pdf')

