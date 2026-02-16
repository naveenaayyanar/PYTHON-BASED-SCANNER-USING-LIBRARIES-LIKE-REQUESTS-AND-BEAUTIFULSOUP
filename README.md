# 🔎 Advanced Web Vulnerability Scanner

A modular Python-based web application security scanner designed to identify common vulnerabilities such as:

* SQL Injection (SQLi)
* Cross-Site Scripting (XSS)
* Missing HTTP Security Headers

Built as part of a Cybersecurity Internship Task.

---

## 🚀 Features

* 🔍 Depth-based web crawler
* 💉 SQL Injection detection (error-based)
* 🧨 Reflected XSS detection
* 🛡 HTTP Security Header analysis
* 📊 HTML report generation
* 🧩 Modular architecture
* ⚙ CLI-based interface
* 🔒 Designed for authorized testing environments

---

## 🏗 Project Architecture

```
web-vuln-scanner/
│
├── main.py
├── core/
│   └── crawler.py
├── scanners/
│   ├── sqli_scanner.py
│   ├── xss_scanner.py
│   └── headers_scanner.py
├── reports/
│   └── report_generator.py
├── requirements.txt
└── README.md
```

Inspired by the modular design of tools like:

* OWASP ZAP
* Burp Suite

---

## 🛠 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/web-vuln-scanner.git
cd web-vuln-scanner
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies:

* Python 3.8+
* Requests
* Beautiful Soup

---

## ▶ Usage

Basic scan:

```bash
python main.py --url http://localhost --depth 2 --output report.html
```

Example (testing local lab):

```bash
python main.py --url http://localhost/dvwa --depth 2 --output report.html
```

---

## 📊 Sample Output

After execution:

```
[+] Crawling http://localhost
[+] Scan complete. Report saved to report.html
```

Open `report.html` in your browser to view findings.

---

## 🛡 Vulnerabilities Detected

### 1️⃣ SQL Injection

* Error-based detection
* Common database error signature matching

### 2️⃣ Reflected XSS

* Payload reflection detection in HTTP responses

### 3️⃣ Missing Security Headers

* Content-Security-Policy
* X-Frame-Options
* X-Content-Type-Options
* Strict-Transport-Security

Aligned with guidance from:
OWASP

---

## ⚠ Ethical Disclaimer

This tool is intended strictly for:

* Educational purposes
* Authorized penetration testing
* Local lab environments

Do NOT scan websites without explicit permission.

Unauthorized scanning is illegal and unethical.

---

## 📚 Learning Objectives

This project demonstrates:

* Web crawling logic
* Vulnerability pattern detection
* HTTP request manipulation
* Security misconfiguration analysis
* Structured report generation
* Modular Python development

---

## 🎯 Future Improvements

* Multi-threaded scanning
* Form-based injection testing
* Authentication support
* JSON report export
* Rate limiting
* Logging system
* Severity scoring system

---

## 👨‍💻 Author
Naveena.A
