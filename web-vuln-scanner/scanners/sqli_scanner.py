
import requests

SQLI_PAYLOADS = ["' OR '1'='1", "' OR 1=1--"]

ERROR_SIGNATURES = [
    "sql syntax",
    "mysql_fetch",
    "syntax error",
    "unclosed quotation mark"
]

def scan_sqli(url):
    findings = []

    for payload in SQLI_PAYLOADS:
        try:
            response = requests.get(url + payload, timeout=5)
            for error in ERROR_SIGNATURES:
                if error in response.text.lower():
                    findings.append({
                        "type": "SQL Injection",
                        "severity": "High",
                        "url": url
                    })
                    return findings
        except:
            continue

    return findings
