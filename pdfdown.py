import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

base_url = "https://bmsit.ac.in"
visited = set()
pdf_links = set()
pdf_folder = "pdf"

os.makedirs(pdf_folder, exist_ok=True)

def is_internal(url):
    parsed = urlparse(url)
    return (parsed.netloc == "" or parsed.netloc == urlparse(base_url).netloc)

def is_pdf_link(link):
    return link.lower().endswith(".pdf")

def extract_links(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"[!] Skipping {url} (status code: {response.status_code})")
            return []

        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()

        for tag in soup.find_all('a', href=True):
            href = tag['href']
            full_url = urljoin(url, href)
            if is_internal(full_url):
                clean_url = full_url.split('#')[0].split('?')[0]
                links.add(clean_url.rstrip('/'))

        return links
    except Exception as e:
        print(f"[!] Error processing {url}: {e}")
        return []

def crawl_for_pdfs(url):
    if url in visited:
        return
    visited.add(url)

    print(f"[*] Crawling: {url}")
    links = extract_links(url)

    for link in links:
        if is_pdf_link(link):
            pdf_links.add(link)
        elif link not in visited:
            crawl_for_pdfs(link)

def download_pdfs():
    for pdf_url in pdf_links:
        try:
            filename = os.path.basename(urlparse(pdf_url).path)
            filepath = os.path.join(pdf_folder, filename)

            if os.path.exists(filepath):
                print(f"[-] Already downloaded: {filename}")
                continue

            print(f"[+] Downloading: {pdf_url}")
            response = requests.get(pdf_url, timeout=10)
            with open(filepath, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            print(f"[!] Failed to download {pdf_url}: {e}")

# Start crawling and downloading PDFs
crawl_for_pdfs(base_url)
print(f"\n[✓] Found {len(pdf_links)} PDF file(s). Starting download...\n")
download_pdfs()
print("\n[✓] All PDFs downloaded to 'pdf/' folder.")
