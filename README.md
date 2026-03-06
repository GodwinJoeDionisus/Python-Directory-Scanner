# Directory Scanner

A Python-based tool that discovers hidden directories and admin panels on a target website.

---

## Project Overview

Directory enumeration is an important technique in penetration testing and bug bounty hunting. Many websites contain hidden directories that are not directly accessible through the main interface.

This tool attempts to discover those hidden paths using a wordlist.

---

## Features

- Directory enumeration
- Wordlist-based scanning
- Detects accessible hidden paths
- Useful for bug bounty reconnaissance

---

## Technologies Used

- Python
- Requests

---

## Installation

Install dependencies:

```
pip install requests
```

---

## Usage

Run the scanner:

```
python directory_scanner.py
```

Enter the target website URL.

Example:

```
http://testphp.vulnweb.com
```

---

## Project Structure

```
DirectoryScanner/
│
├── directory_scanner.py
├── directories.txt
└── README.md
```

---

## Disclaimer

This project is for educational purposes only. Only scan websites you own or have permission to test.

---

## Author

Godwin Joe Dionisus  
Cybersecurity | Networking | Ethical Hacking
