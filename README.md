# PhantomGuard — Benign Secure Backup (Safe, Local-Only)

> **Important — Legal & Ethical Notice**  
> This repository provides a **benign, local-only** tool for securely encrypting and decrypting personal backups.  
> It contains **no networking, no remote control, and no destructive defaults**.  
> Do **not** use this project for unauthorized access, destructive actions, or on systems you do not own.

---

## Overview

PhantomGuard (safe variant) is a small, user-driven utility demonstrating secure, local file backup using symmetric encryption.  
It is intended for **legitimate backups and educational purposes only**.

The repository contains two safe paths:

1. **Educational Analysis** — For documenting malware behavior safely without publishing runnable malicious code.  
2. **Benign Secure Backup** — A safe local utility for encrypting personal files.

---

## Educational Malware Analysis (safe guidance)

This section is for researchers who want to publish observations while avoiding enabling misuse.

### Content to include
- **High-level behavior summary** (what the sample tried to do, e.g., "enumerated files and wrote encrypted copies").  
- **Observed artifacts** (sanitized file names, registry keys, network indicators — remove IPs/domain names).  
- **Static analysis notes** (imports used, notable strings — redact anything enabling reproduction).  
- **Dynamic analysis notes** (processes spawned, file and registry changes, network patterns) — only publish sanitized logs or excerpts.  
- **Detections and mitigations** (YARA/Sigma rules in defensive form, EDR configurations, network alerts to look for).

### Safety rules for publication
- Do **not** include full runnable code from malicious samples.  
- Redact or sanitize IPs, domains, credentials, and any payloads.  
- Prefer pseudo-code for demonstration.  
- Share only in responsible forums and follow local laws and policies.

---

## Benign Secure File Backup — Overview (safe alternative)

If your aim is to demonstrate encryption techniques for legitimate backups, create a small, non-networked utility that:

- Runs **locally only** (no sockets, no remote control).  
- Requires the user to **supply and store their own encryption key**.  
- Adds clear **confirmation prompts** before deleting files.  
- Provides an **undo/restore workflow** using the same key.  
- Includes strong warnings about key loss and irreversible file changes.

The `backup-tool/` folder should contain:

- A minimal CLI that encrypts/decrypts files in a user-specified folder.  
- No automatic deletion of files outside the target folder.  
- Unit tests and example usage demonstrating encryption/decryption on test files only.

### High-level usage (example)

```bash
# Generate a local key
python backup_tool.py generate-key --out my_key.key

# Encrypt a folder
python backup_tool.py encrypt --key my_key.key --input ./test-folder --output ./encrypted-backup

# Decrypt a folder
python backup_tool.py decrypt --key my_key.key --input ./encrypted-backup --output ./restored
