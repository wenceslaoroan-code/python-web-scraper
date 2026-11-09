# Modular Web Data Extraction & Processing Engine

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Security](https://img.shields.io/badge/Security-Input%20Sanitized-orange.svg)

A modular, production-ready Python automation tool designed to securely scrape, parse, clean, and export web data into structured JSON and CSV formats. Built with robust error handling, automated retry logic, logging, and defensive sanitization.

---

## 📌 Features

- **Automated Extraction**: Robust HTML parsing using `BeautifulSoup4`.
- **Defensive Error Handling**: Handles HTTP status codes, network timeouts, and malformed HTML tags gracefully.
- **Data Sanitization**: Cleans and normalizes extracted text before writing to storage.
- **Dual Export Formats**: Exports data to structured `JSON` and `CSV` schema.
- **Logging Subsystem**: Full execution logging for auditing and debugging.
- **Unit Tested**: Includes unit test coverage via Python's standard `unittest` framework.

---

## 🛠️ Architecture Overviewv
