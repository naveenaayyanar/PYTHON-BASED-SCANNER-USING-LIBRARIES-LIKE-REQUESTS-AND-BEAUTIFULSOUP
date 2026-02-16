
import requests

def scan_xss(url):
    findings = []
    test_payload = "<script>XSS_TEST</script>"

    try:
        response = requests.get(url, params={"q": test_payload}, timeout=5)
        if test_payload in response.text:
            findings.append({
                "type": "Reflected XSS",
                "severity": "Medium",
                "url": url
            })
    except:
        pass

    return findings
