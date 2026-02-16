
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl(base_url, max_depth):
    visited = set()
    queue = [(base_url, 0)]

    while queue:
        url, depth = queue.pop(0)
        if depth > max_depth or url in visited:
            continue

        visited.add(url)

        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")

            for link in soup.find_all("a", href=True):
                full_url = urljoin(base_url, link["href"])
                if urlparse(full_url).netloc == urlparse(base_url).netloc:
                    queue.append((full_url, depth + 1))
        except:
            continue

    return list(visited)
