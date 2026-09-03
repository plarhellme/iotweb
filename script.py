import glob
import re
import os

files = glob.glob(r"D:\work\iotweb\*.html")

pages = [
    ("index.html", "Go to Home Page"),
    ("page1.html", "Go to Page 1"),
    ("page2.html", "Go to Page 2"),
    ("page3.html", "Go to Page 3"),
    ("page4.html", "Go to Page 4"),
    ("page5.html", "Go to Page 5"),
    ("page6.html", "Go to Page 6"),
    ("page7.html", "Go to Page 7"),
    ("page8.html", "Go to Page 8"),
    ("page9.html", "Go to Page 9"),
    ("page10.html", "Go to Page 10"),
    ("page11.html", "Go to Page 11"),
    ("page12.html", "Go to Page 12"),
    ("page13.html", "Go to Page 13"),
    ("page14.html", "Go to Page 14"),
    ("quiz1.html", "Go to Quiz 1"),
]

for file_path in files:
    filename = os.path.basename(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Build the nav block for this page
    nav_links = []
    for page_href, page_text in pages:
        if page_href != filename:
            nav_links.append(f'      <a href="{page_href}">{page_text}</a>')
    
    nav_html = '    <div class="page-nav">\n' + '\n'.join(nav_links) + '\n    </div>'
    
    # 2. Replace existing page-nav or insert after <body>
    if 'class="page-nav"' in content:
        content = re.sub(r'<div class="page-nav">.*?</div>', nav_html, content, flags=re.DOTALL)
    else:
        # insert right after <body>
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + nav_html, content, count=1, flags=re.IGNORECASE)
        
    # 3. Add style.css if it doesn't exist
    if 'href="style.css"' not in content:
        content = re.sub(r'(</head>)', r'  <link rel="stylesheet" href="style.css" />\n  \1', content, flags=re.IGNORECASE)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done updating nav for all pages")
