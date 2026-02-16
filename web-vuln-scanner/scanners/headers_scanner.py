
import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security"
]

def scan_headers(url):
    findings = []

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        for header in SECURITY_HEADERS:
            if header not in headers:
                findings.append({
                    "type": f"Missing {header}",
                    "severity": "Low",
                    "url": url
                })
    except:
        pass

    return findings
