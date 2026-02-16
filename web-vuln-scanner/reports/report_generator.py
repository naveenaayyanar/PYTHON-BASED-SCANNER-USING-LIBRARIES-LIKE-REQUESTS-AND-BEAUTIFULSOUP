
def generate_report(filename, findings):
    with open(filename, "w") as f:
        f.write("<html><head><title>Scan Report</title></head><body>")
        f.write("<h1>Web Vulnerability Scan Report</h1>")

        if not findings:
            f.write("<p>No vulnerabilities detected.</p>")
        else:
            for finding in findings:
                f.write(f"<h3>{finding['type']}</h3>")
                f.write(f"<p>Severity: {finding['severity']}</p>")
                f.write(f"<p>URL: {finding['url']}</p><hr>")

        f.write("</body></html>")
