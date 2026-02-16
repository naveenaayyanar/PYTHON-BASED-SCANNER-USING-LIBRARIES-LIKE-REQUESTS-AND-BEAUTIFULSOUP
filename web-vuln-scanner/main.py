
import argparse
from core.crawler import crawl
from scanners.sqli_scanner import scan_sqli
from scanners.xss_scanner import scan_xss
from scanners.headers_scanner import scan_headers
from reports.report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="Advanced Web Vulnerability Scanner")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--depth", type=int, default=2, help="Crawling depth")
    parser.add_argument("--output", default="report.html", help="Output report file")

    args = parser.parse_args()

    print(f"[+] Crawling {args.url}")
    urls = crawl(args.url, args.depth)

    findings = []

    for url in urls:
        findings.extend(scan_sqli(url))
        findings.extend(scan_xss(url))
        findings.extend(scan_headers(url))

    generate_report(args.output, findings)
    print(f"[+] Scan complete. Report saved to {args.output}")

if __name__ == "__main__":
    main()
