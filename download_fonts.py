import requests
import re
import os

font_url = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=DM+Sans:wght@400;500;600&family=Great+Vibes&family=Noto+Naskh+Arabic:wght@400;500&display=swap"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

r = requests.get(font_url, headers=headers)
css_content = r.text

urls = re.findall(r'url\((.*?)\)', css_content)
os.makedirs('assets/fonts', exist_ok=True)

for i, u in enumerate(urls):
    clean_u = u.strip("'\"")
    if clean_u.startswith("http"):
        print(f"Downloading font {clean_u}")
        fr = requests.get(clean_u, headers=headers)
        ext = ".woff2" if "woff2" in clean_u else ".woff"
        filename = f"font_{i}{ext}"
        filepath = os.path.join('assets/fonts', filename)
        with open(filepath, 'wb') as f:
            f.write(fr.content)
        
        css_content = css_content.replace(clean_u, f"../fonts/{filename}")

os.makedirs('assets/css', exist_ok=True)
with open('assets/css/fonts.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Done downloading fonts.")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if '<link href="assets/css/fonts.css"' not in html:
    html = html.replace('<link href="assets/css/styles.css" rel="stylesheet"/>', 
                        '<link href="assets/css/fonts.css" rel="stylesheet"/>\n<link href="assets/css/styles.css" rel="stylesheet"/>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Injected fonts.css into index.html")
