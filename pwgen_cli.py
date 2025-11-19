# pwgen_cli.py
import argparse
from password_utils import generate_new_passwords
from colorama import init as colorama_init, Fore, Style
import sys
import tkinter as tk
from tkinter import ttk

colorama_init(autoreset=True)

def pretty_print_passwords(passwords):
    # color each suggestion differently
    colors = [Fore.GREEN, Fore.CYAN, Fore.MAGENTA]
    for idx, pwd in enumerate(passwords, 1):
        color = colors[(idx-1) % len(colors)]
        print(f"{color}Suggestion {idx}: {Style.BRIGHT}{pwd}")

def interactive_loop(default_length=12, default_strength="strong"):
    while True:
        ans = input("Do you want a password suggestion? (yes/no): ").strip().lower()
        if ans in ("y", "yes"):
            # ask options
            try:
                length_input = input(f"Length (press Enter for {default_length}): ").strip()
                length = int(length_input) if length_input else default_length
            except ValueError:
                print("Invalid length. Using default.")
                length = default_length

            strength = input(f"Strength [weak/medium/strong] (Enter for {default_strength}): ").strip().lower()
            if strength not in ("weak", "medium", "strong", ""):
                print("Invalid strength. Using default.")
                strength = default_strength
            elif strength == "":
                strength = default_strength

            pwlist = generate_new_passwords(3, length=length, strength=strength)
            pretty_print_passwords(pwlist)

        elif ans in ("n", "no"):
            print("Alright — no password generated. Bye!")
            break
        else:
            print("Please answer 'yes' or 'no'.")

def main():
    parser = argparse.ArgumentParser(description="Simple secure password generator")
    parser.add_argument("--length", "-l", type=int, default=12, help="Password length (int)")
    parser.add_argument("--strength", "-s", choices=["weak","medium","strong"], default="strong", help="Password strength")
    parser.add_argument("--three", action="store_true", help="Generate three suggestions (default interactive does 3)")
    parser.add_argument("--no-color", action="store_true", help="Disable colored output")
    parser.add_argument("--once", action="store_true", help="Generate once and exit (non-interactive)")

    args = parser.parse_args()

    if args.once:
        n = 3 if args.three else 1
        passwords = generate_new_passwords(n, length=args.length, strength=args.strength)
        if args.no_color:
            for i, p in enumerate(passwords, 1):
                print(f"Suggestion {i}: {p}")
        else:
            pretty_print_passwords(passwords)
        sys.exit(0)

    # otherwise run interactive loop (colors optional)
    if args.no_color:
        # monkey-patch pretty_print_passwords to plain
        def plain_print(ps):
            for i,p in enumerate(ps,1):
                print(f"Suggestion {i}: {p}")
        global pretty_print_passwords  # override for session
        pretty_print_passwords = plain_print

    interactive_loop(default_length=args.length, default_strength=args.strength)

if __name__ == "__main__":
    main()

def generate():
    try:
        length = int(length_var.get())
        if length < 1:
            raise ValueError
    except ValueError:
        show_message("Length must be a positive integer")
        return

    strength = strength_var.get()
    pwlist = generate_new_passwords(3, length=length, strength=strength)
    for i, pw in enumerate(pwlist):
        outputs[i].delete(0, tk.END)
        outputs[i].insert(0, pw)

def copy_to_clip(idx):
    root.clipboard_clear()
    root.clipboard_append(outputs[idx].get())
    show_message("Copied to clipboard")

def show_message(msg):
    status_var.set(msg)
    root.after(3000, lambda: status_var.set(""))

root = tk.Tk()
root.title("FinSec Password Generator")

frame = ttk.Frame(root, padding=16)
frame.grid(row=0, column=0)

ttk.Label(frame, text="Length:").grid(row=0, column=0, sticky="w")
length_var = tk.StringVar(value="12")
ttk.Entry(frame, textvariable=length_var, width=6).grid(row=0, column=1, sticky="w", padx=6)

ttk.Label(frame, text="Strength:").grid(row=0, column=2, sticky="w", padx=(10,0))
strength_var = tk.StringVar(value="strong")
ttk.Combobox(frame, textvariable=strength_var, values=["weak","medium","strong"], width=8).grid(row=0, column=3, sticky="w")

ttk.Button(frame, text="Generate 3", command=generate).grid(row=0, column=4, padx=(10,0))

outputs = []
for i in range(3):
    ent = ttk.Entry(frame, width=40)
    ent.grid(row=1+i, column=0, columnspan=4, pady=6, sticky="w")
    outputs.append(ent)
    ttk.Button(frame, text="Copy", command=lambda idx=i: copy_to_clip(idx)).grid(row=1+i, column=4, padx=(6,0))

status_var = tk.StringVar(value="")
ttk.Label(frame, textvariable=status_var, foreground="blue").grid(row=4, column=0, columnspan=5, pady=(8,0))

root.mainloop()