# 🔐 Password Generator

A professional-grade password generator similar to Google's password recommendations, featuring both GUI and CLI interfaces with educational cybersecurity components.

## ✨ Features

### Core Functionality
- **Cryptographically Secure**: Uses Python's `secrets` module for true randomness
- **Customizable Generation**: 
  - Adjustable length (4-64 characters, default: 14)
  - Toggle uppercase letters (A-Z)
  - Toggle lowercase letters (a-z)
  - Toggle digits (0-9)
  - Toggle special symbols (!@#$%^&*()_+-=[]{}|;:,.<>?)
- **Default Settings**: 14 characters with all character types included

### Security Features
- **Password Strength Analysis**:
  - Entropy calculation (bits of randomness)
  - Strength rating (Very Weak to Very Strong)
  - Time-to-crack estimation
- **SHA-256 Hashing**: Secure one-way password hashing
- **Character Type Validation**: Ensures at least one character from each selected type

### User Interfaces
- **GUI Mode** (tkinter):
  - Clean, modern interface
  - One-click password generation
  - Copy to clipboard functionality
  - Real-time strength analysis
  - Visual strength indicators
  - Hash display with educational tooltips
- **CLI Mode**:
  - Interactive menu system
  - Default and custom password generation
  - Password strength analyzer
  - Password hashing tool
  - Educational security information



 🚀 Usage
 Running the Application

```bash
python3 pwgen_web.py
Running on http://127.0.0.1:5000
```
I Used: 

blinker==1.9.0
click==8.3.1
colorama==0.4.6
Flask==3.1.2
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
Werkzeug==3.1.3
