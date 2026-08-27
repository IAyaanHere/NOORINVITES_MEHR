import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

BASE_URL = "https://naqshdigital.in/mehr/"
DIR_PATH = "."

# Session to reuse connections
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
})

def sanitize_filename(url_path):
    path = urlparse(url_path).path
    filename = os.path.basename(path)
    return filename

def get_folder_for_url(url, tag_name):
    # Determine folder based on file extension and tag type
    path = urlparse(url).path
    ext = os.path.splitext(path)[1].lower()
    
    if ext == '.css': return 'assets/css'
    if ext == '.js': return 'assets/js'
    if ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico']: return 'assets/images'
    if ext in ['.mp4', '.webm', '.ogg']: return 'media'
    if ext in ['.mp3', '.wav']: return 'media'
    if ext in ['.woff', '.woff2', '.ttf', '.eot']: return 'assets/fonts'
    
    if tag_name == 'script': return 'assets/js'
    if tag_name == 'link': return 'assets/css'
    if tag_name == 'img': return 'assets/images'
    
    return 'assets/misc'

def download_file(url, folder):
    if url.startswith("data:"): return url
    if url.startswith("#"): return url
    
    full_url = urljoin(BASE_URL, url)
    parsed = urlparse(full_url)
    
    # We only download if we can get a filename
    filename = sanitize_filename(full_url)
    if not filename:
        return url
        
    local_path = os.path.join(DIR_PATH, folder, filename)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    relative_path = f"{folder}/{filename}"
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        return relative_path
        
    try:
        print(f"Downloading {full_url} to {local_path}")
        r = session.get(full_url, stream=True, timeout=15)
        r.raise_for_status()
        with open(local_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                
        # If it's a CSS file, we need to process it to find fonts/images
        if local_path.endswith('.css'):
            process_css_file(local_path, full_url)
            
        return relative_path
    except Exception as e:
        print(f"Failed to download {full_url}: {e}")
        return url

def process_css_file(filepath, css_url):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Find url(...)
    urls = re.findall(r'url\((.*?)\)', content)
    for u in urls:
        clean_u = u.strip("'\"")
        if clean_u.startswith("data:"): continue
        
        # Determine URL
        resource_url = urljoin(css_url, clean_u)
        
        # Decide folder
        folder = 'assets/fonts' if any(ext in clean_u for ext in ['.woff', '.ttf', '.eot']) else 'assets/images'
        
        rel_path = download_file(resource_url, folder)
        
        # Replace in CSS
        # Since CSS is in assets/css, and rel_path is from root (e.g., assets/fonts/font.woff2)
        # the relative path from CSS should be ../fonts/font.woff2
        if rel_path != resource_url and rel_path.startswith("assets/"):
            new_path = rel_path.replace("assets/", "../", 1)
            if new_path.startswith("../media/"): 
                new_path = "../../" + rel_path # if it was in media, etc. (just being safe)
            content = content.replace(u, f"'{new_path}'")
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("Fetching index.html...")
    r = session.get(BASE_URL)
    r.encoding = 'utf-8'
    html_content = r.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Process links (CSS, favicons)
    for tag in soup.find_all('link'):
        href = tag.get('href')
        if href:
            folder = get_folder_for_url(href, 'link')
            new_href = download_file(href, folder)
            tag['href'] = new_href
            
    # Process scripts
    for tag in soup.find_all('script'):
        src = tag.get('src')
        if src:
            folder = get_folder_for_url(src, 'script')
            new_src = download_file(src, folder)
            tag['src'] = new_src
            
    # Process images
    for tag in soup.find_all('img'):
        src = tag.get('src')
        if src:
            folder = get_folder_for_url(src, 'img')
            new_src = download_file(src, folder)
            tag['src'] = new_src
            
    # Process audio/video
    for tag_name in ['audio', 'video', 'source']:
        for tag in soup.find_all(tag_name):
            src = tag.get('src')
            if src:
                folder = 'media'
                new_src = download_file(src, folder)
                tag['src'] = new_src

    # Save index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Saved index.html")
    
    # Also download Google Fonts if present
    google_fonts_links = [tag for tag in soup.find_all('link') if 'fonts.googleapis.com' in tag.get('href', '')]
    if google_fonts_links:
        print("Found Google Fonts")
        font_css_content = ""
        for tag in google_fonts_links:
            href = tag.get('href')
            print(f"Downloading Google Font CSS: {href}")
            res = session.get(href)
            if res.status_code == 200:
                font_css_content += res.text + "\n"
            # Remove from original HTML
            tag.decompose()
            
        # Parse font_css_content and download woff2 files
        urls = re.findall(r'url\((.*?)\)', font_css_content)
        for u in urls:
            clean_u = u.strip("'\"")
            if clean_u.startswith("http"):
                rel_path = download_file(clean_u, 'assets/fonts')
                new_path = rel_path.replace("assets/", "../", 1)
                font_css_content = font_css_content.replace(clean_u, new_path)
                
        # Save fonts.css
        os.makedirs('assets/css', exist_ok=True)
        with open('assets/css/fonts.css', 'w', encoding='utf-8') as f:
            f.write(font_css_content)
            
        # Add local fonts.css to HTML
        new_link = soup.new_tag('link', rel='stylesheet', href='assets/css/fonts.css')
        if soup.head:
            soup.head.append(new_link)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
    print("Done!")

if __name__ == "__main__":
    main()
