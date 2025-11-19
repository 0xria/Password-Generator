
import secrets
import string

def choose_from(seq):
    return secrets.choice(seq)

"""
strength: 'weak', 'medium', 'strong'
length : int( recommended >= 12 for strong)
Returns a string of randomly generate password
"""

def generate_password(length=12, strength="strong"):
    if length < 1:
        raise ValueError("Length must be >= 1")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    signs = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"

    if strength == "weak":
        pool = lower + digits 
        pw = [] #atleast one letter and digit if possible
        pw.append(choose_from(lower))
        pw.append(choose_from(digits))
        for _ in range(max(0, length - 2)):
            pw.append(choose_from(pool))

    elif strength == "medium":
        pool = lower + upper + digits #atleat one lower, upper and digit
        pw = []
        pw.append(choose_from(lower))
        pw.append(choose_from(upper))
        pw.append(choose_from(digits))
        for _ in range(max(0, length - 3)):
            pw.append(choose_from(pool))

    else: #strong which is the default
        pool = lower + upper + digits + signs #atleast one lower, uopper, digit and sign
        pw = []
        pw.append(choose_from(lower))
        pw.append(choose_from(upper))
        pw.append(choose_from(digits))
        pw.append(choose_from(signs))
        for _ in range(max(0, length - 4)):
            pw.append(choose_from(pool))

    #randomly and securely shuffle
    for i in range(len(pw)-1, 0, -1):
        j = secrets.randbelow(i+1)
        pw[1], pw[j] = pw[j], pw[i]

    return ''.join(pw)

def generate_new_passwords(n=3, length=12, strength="strong"):
    return [generate_password(length=length, strength=strength) for _ in range(n)]
