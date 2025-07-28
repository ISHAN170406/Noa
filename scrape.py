import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import sys

base_url = "https://bmsit.ac.in"
visited = set()
unique_links = set()

def is_internal(url):
    parsed = urlparse(url)
    return (parsed.netloc == "" or parsed.netloc == urlparse(base_url).netloc)

def extract_links(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"[!] Skipping {url} (status code: {response.status_code})")
            return []

        # Only parse HTML content
        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            print(f"[!] Skipping {url} (non-HTML content: {content_type})")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()

        for tag in soup.find_all('a', href=True):
            href = tag['href']
            full_url = urljoin(url, href)

            if is_internal(full_url):
                clean_url = re.sub(r'#.*$', '', full_url)  # Remove fragment
                clean_url = re.sub(r'\?.*$', '', clean_url)  # Remove query
                links.add(clean_url.rstrip('/'))

        return links
    except requests.exceptions.Timeout:
        print(f"[!] Timeout while accessing: {url}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Request error for {url}: {e}")
    except Exception as e:
        print(f"[!] General error for {url}: {e}")

    return []

def crawl(url, depth=0):
    if url in visited:
        return
    visited.add(url)

    indent = '  ' * depth
    print(f"{indent}[*] Crawling: {url}")
    links = extract_links(url)

    for link in links:
        if link not in visited:
            unique_links.add(link)
            crawl(link, depth + 1)

# Start crawling
print("[+] Starting crawl from:", base_url)
crawl(base_url)

# Output all unique links
print("\n[+] Crawl complete. Total unique links found:", len(unique_links))
for link in sorted(unique_links):
    print(link)

# Optional: Save to file
with open("bmsit_links.txt", "w") as f:
    for link in sorted(unique_links):
        f.write(link + "\n")
