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

### Educational Component
- **Entropy Explanation**: Learn what makes passwords strong
- **Security Best Practices**: Tips for password management
- **Hashing Education**: Understand why hashing matters
- **Common Mistakes**: Avoid weak password patterns
- **Character Pool Analysis**: See how character types affect strength

## 🚀 Usage

### Running the Application

```bash
python3 main.py
```

The application will automatically detect if GUI (tkinter) is available and offer a choice between GUI and CLI modes.

### GUI Mode
1. Click "Generate Password" for instant 14-character password
2. Adjust settings (length, character types) as needed
3. Click "Copy to Clipboard" to copy the password
4. Click "Show Hash" to see the SHA-256 hash
5. View real-time strength analysis

### CLI Mode
Choose from the menu:
1. **Generate Password** - Quick 14-character password with all types
2. **Generate Custom Password** - Customize length and character types
3. **Analyze Password Strength** - Check any password's strength
4. **Hash a Password** - Generate SHA-256 hash
5. **Learn About Password Security** - Educational information
6. **Exit**

## 🧪 Testing



This demonstrates:
- Default password generation (14 chars)
- Longer passwords (20 chars)
- Passwords without symbols
- Weak password analysis
- Multiple password generation

## 📊 Password Strength Ratings

| Entropy (bits) | Rating | Time to Crack |
|---------------|--------|---------------|
| < 28 | Very Weak | Instantly |
| 28-36 | Weak | Seconds |
| 36-60 | Fair | Hours/Days |
| 60-80 | Good | Years |
| 80-100 | Strong | Centuries |
| > 100 | Very Strong | Millions of years |

## 🔒 Security Best Practices

1. **Use Unique Passwords**: Never reuse passwords across accounts
2. **Length Matters**: Longer passwords are exponentially stronger
3. **Mix Character Types**: Use all available character types
4. **Use a Password Manager**: Store passwords securely
5. **Enable 2FA**: Add an extra layer of security
6. **Regular Updates**: Change passwords if breach suspected

## 🎓 Educational Insights

### What is Entropy?
Entropy measures the unpredictability of a password. It's calculated as:
```
Entropy = log2(pool_size^length)
```

### Character Pool Sizes
- Lowercase only: 26 characters
- + Uppercase: 52 characters
- + Digits: 62 characters
- + Symbols: 81 characters

### Why Hashing?
Hashing converts passwords into fixed-length strings using one-way functions. Even if a database is breached, attackers only get hashes, not actual passwords.

## 📋 Requirements

- Python 3.6+
- tkinter (optional, for GUI mode - usually included with Python)
- No external dependencies required!

## 🛠️ Technical Details

- **Random Generation**: Uses `secrets.choice()` for cryptographic security
- **Character Guarantee**: Ensures at least one character from each selected type
- **Shuffle Algorithm**: Fisher-Yates shuffle for uniform distribution
- **Hash Function**: SHA-256 for password hashing
- **Entropy Formula**: log2(pool_size^length)

## 📝 Example Output

```
Generated Password: i45Xq$R#vFi{8%
Entropy: 90.43 bits
Strength: Strong
Time to Crack: Millions of years
SHA-256 Hash: 558af2765b02aa7c8957446c41aec5e6afd4ef1e092ccc4d76bf5a1969ead4cb
```

## 🎯 Use Cases

- Personal password generation
- Developer tools
- Security training and education
- Password policy demonstration
- Cybersecurity awareness programs

## ⚠️ Common Mistakes to Avoid

- Using personal information (names, birthdays)
- Using dictionary words
- Using simple patterns (123456, qwerty)
- Reusing passwords across sites
- Sharing passwords with others
- Writing passwords in plain text

## 🌟 Features Comparison

| Feature | This Generator | Basic Generators |
|---------|---------------|------------------|
| Cryptographic Security | ✅ | ❌ |
| Entropy Calculation | ✅ | ❌ |
| Strength Analysis | ✅ | ❌ |
| Password Hashing | ✅ | ❌ |
| Educational Content | ✅ | ❌ |
| GUI & CLI | ✅ | ❌ |
| Character Guarantee | ✅ | ❌ |

---

**Made with 🔒 for better password security**
