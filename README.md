# PhantomGuard — Secure Local Backup Utility

> **Notice:** This repository provides a **benign, local-only** utility for encrypting and decrypting personal files.  
> It is designed for educational purposes and secure personal backups. The software does **not** include networking, remote control, or any destructive defaults.  
> Unauthorized use on systems you do not own is strictly prohibited.

---

## Overview

PhantomGuard is a lightweight, user-driven utility that demonstrates secure local file backup using symmetric encryption.  
It allows users to safely encrypt directories for personal backups and later decrypt them using the same key.  

The repository provides a **safe alternative** to demonstrate encryption techniques without exposing sensitive or malicious functionality.

---

## Features

- Generate a local symmetric key for file encryption.  
- Encrypt a user-specified folder with individually encrypted files.  
- Decrypt an encrypted folder using the original key.  
- Non-destructive defaults: original files are preserved unless explicitly confirmed for deletion.  
- Fully local operation with no external network communication.

---

## Requirements

- Python 3.8 or newer  
- `cryptography` package

Install dependencies in a virtual environment:

```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows PowerShell
# .\venv\Scripts\Activate.ps1

pip install cryptography
