# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin, urlparse
# import re

# base_url = "https://bmsit.ac.in"
# visited = set()
# non_pdf_links = set()

# def is_internal(url):
#     parsed = urlparse(url)
#     return (parsed.netloc == "" or parsed.netloc == urlparse(base_url).netloc)

# def is_pdf_link(link):
#     return link.lower().endswith(".pdf")

# def extract_links(url):
#     try:
#         response = requests.get(url, timeout=10)
#         if response.status_code != 200:
#             print(f"[!] Skipping {url} (status code: {response.status_code})")
#             return []

#         content_type = response.headers.get("Content-Type", "")
#         if "text/html" not in content_type:
#             return []

#         soup = BeautifulSoup(response.text, 'html.parser')
#         links = set()

#         for tag in soup.find_all('a', href=True):
#             href = tag['href']
#             full_url = urljoin(url, href)
#             if is_internal(full_url):
#                 clean_url = full_url.split('#')[0].split('?')[0].rstrip('/')
#                 if not is_pdf_link(clean_url):
#                     links.add(clean_url)

#         return links
#     except Exception as e:
#         print(f"[!] Error processing {url}: {e}")
#         return []

# def crawl(url):
#     if url in visited:
#         return
#     visited.add(url)

#     print(f"[*] Crawling: {url}")
#     non_pdf_links.add(url)
#     links = extract_links(url)

#     for link in links:
#         if link not in visited and not is_pdf_link(link):
#             crawl(link)

# # Start crawling
# print("[+] Starting crawl...")
# crawl(base_url)

# # Save to llinks.txt
# with open("llinks.txt", "w") as f:
#     for link in sorted(non_pdf_links):
#         f.write(link + "\n")

# print(f"\n[✓] Crawl finished. {len(non_pdf_links)} non-PDF links saved to 'llinks.txt'")




# import os
# import pdfkit
# import re

# # Folder for PDFs
# output_folder = "lpdf"
# os.makedirs(output_folder, exist_ok=True)

# # Sanitize filenames from URL paths
# def sanitize_filename(url):
#     path = url.split("//")[-1]  # remove scheme
#     path = re.sub(r'[^\w\-_.]', '_', path)
#     return path + ".pdf"

# # Read links from file
# with open("llinks.txt", "r") as f:
#     links = [line.strip() for line in f if line.strip()]

# # Convert each to PDF
# for url in links:
#     filename = sanitize_filename(url)
#     filepath = os.path.join(output_folder, filename)

#     if os.path.exists(filepath):
#         print(f"[-] Already exists: {filename}")
#         continue

#     try:
#         print(f"[+] Converting to PDF: {url}")
#         pdfkit.from_url(url, filepath)
#     except Exception as e:
#         print(f"[!] Failed to convert {url}: {e}")

# print(f"\n[✓] All done. PDFs saved to '{output_folder}/'")



from PyPDF2 import PdfMerger
from pathlib import Path

# Folder with individual PDFs
pdf_folder = Path("lpdf")
merged_pdf_path = pdf_folder / "merged_output.pdf"

# Initialize the merger
merger = PdfMerger()

# Loop through all PDFs and add them
for pdf_file in sorted(pdf_folder.glob("*.pdf")):
    if pdf_file.name == "merged_output.pdf":
        continue  # skip already merged file if re-running
    print(f"Adding: {pdf_file.name}")
    merger.append(str(pdf_file))

# Write out the final merged PDF
merger.write(str(merged_pdf_path))
merger.close()

print(f"\n✅ All PDFs merged successfully into: {merged_pdf_path}")
