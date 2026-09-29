"""


ATM Banking System

A professional, menu-driven ATM simulation using only Python built-ins.
Data is persisted to a JSON file so accounts survive restarts.

Author  : Neeraj Dusa (College Project)
Python  : 3.8+
Run     : python atm_banking_system.py
"""

import json
import os
import hashlib
import datetime
import random

# ──────────────────────────────────────────────
# CONSTANTS
# ──────────────────────────────────────────────

DATA_FILE = "bank_data.json"
MAX_PIN_ATTEMPTS = 3
MIN_PIN_LENGTH = 4
MIN_BALANCE = 500.0

# ══════════════════════════════════════════════
# DATA LAYER
# ══════════════════════════════════════════════

def hash_pin(pin: str) -> str:
    """Return SHA-256 hash of a PIN string."""
    return hashlib.sha256(pin.encode()).hexdigest()

def load_data() -> dict:
    """Load account data from file."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def save_data(accounts: dict) -> None:
    """Save account data to file."""
    with open(DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

# ══════════════════════════════════════════════
# DISPLAY
# ══════════════════════════════════════════════

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def divider(char="─", width=50):
    print(char * width)

def print_header(title):
    divider("═")
    print(f"{'ATM BANKING SYSTEM':^50}")
    print(f"{title:^50}")
    divider("═")

def print_menu(options):
    divider()
    for i, opt in enumerate(options, 1):
        print(f"[{i}] {opt}")
    divider()

# ══════════════════════════════════════════════
# INPUT VALIDATION
# ══════════════════════════════════════════════

def get_valid_amount(prompt):
    while True:
        try:
            amt = float(input(prompt))
            if amt > 0:
                return round(amt, 2)
            print("Enter positive amount.")
        except:
            print("Invalid input.")

def get_valid_pin(prompt="Enter PIN: "):
    while True:
        pin = input(prompt)
        if pin.isdigit() and len(pin) >= MIN_PIN_LENGTH:
            return pin
        print("Invalid PIN.")

def generate_account_number(accounts):
    while True:
        acc = str(random.randint(1000000000, 9999999999))
        if acc not in accounts:
            return acc

# ══════════════════════════════════════════════
# CORE FUNCTIONS
# ══════════════════════════════════════════════

def _make_txn(desc, amt, bal):
    return {
        "datetime": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
        "description": desc,
        "amount": amt,
        "balance": bal
    }

def create_account(accounts):
    print_header("CREATE ACCOUNT")

    name = input("Name: ")
    pin = get_valid_pin("Set PIN: ")
    confirm = get_valid_pin("Confirm PIN: ")

    if pin != confirm:
        print("PIN mismatch.")
        return

    deposit = get_valid_amount("Initial Deposit: ")
    if deposit < MIN_BALANCE:
        print("Minimum balance required.")
        return

    acc_no = generate_account_number(accounts)

    accounts[acc_no] = {
        "name": name,
        "pin_hash": hash_pin(pin),
        "balance": deposit,
        "locked": False,
        "transactions": [_make_txn("Account opened", deposit, deposit)]
    }

    save_data(accounts)
    print("Account Created. Account No:", acc_no)
    input("Press Enter...")

def login(accounts):
    print_header("LOGIN")

    acc_no = input("Account Number: ")

    if acc_no not in accounts:
        print("Not found.")
        return None, None

    acc = accounts[acc_no]

    if acc["locked"]:
        print("Account locked.")
        return None, None

    for i in range(MAX_PIN_ATTEMPTS):
        pin = get_valid_pin()
        if hash_pin(pin) == acc["pin_hash"]:
            print("Login success!")
            input("Press Enter...")
            return acc_no, acc
        else:
            print("Wrong PIN.")

    acc["locked"] = True
    save_data(accounts)
    print("Account locked.")
    return None, None

def check_balance(acc):
    print_header("BALANCE")
    print("Balance:", acc["balance"])
    input("Press Enter...")

def deposit(accounts, acc_no, acc):
    amt = get_valid_amount("Deposit: ")
    acc["balance"] += amt
    acc["transactions"].append(_make_txn("Deposit", amt, acc["balance"]))
    save_data(accounts)
    print("Deposited.")
    input("Press Enter...")

def withdraw(accounts, acc_no, acc):
    amt = get_valid_amount("Withdraw: ")

    if acc["balance"] - amt < MIN_BALANCE:
        print("Insufficient balance.")
    else:
        acc["balance"] -= amt
        acc["transactions"].append(_make_txn("Withdraw", -amt, acc["balance"]))
        save_data(accounts)
        print("Withdrawn.")

    input("Press Enter...")

def show_transactions(acc):
    print_header("TRANSACTIONS")
    for t in acc["transactions"][-10:][::-1]:
        print(t)
    input("Press Enter...")

def change_pin(accounts, acc_no, acc):
    old = get_valid_pin("Old PIN: ")
    if hash_pin(old) != acc["pin_hash"]:
        print("Wrong PIN.")
        return

    new = get_valid_pin("New PIN: ")
    acc["pin_hash"] = hash_pin(new)
    save_data(accounts)
    print("PIN changed.")
    input("Press Enter...")

# ══════════════════════════════════════════════
# MENUS
# ══════════════════════════════════════════════

def banking_menu(accounts, acc_no, acc):
    while True:
        clear_screen()
        print_header(f"Welcome {acc['name']}")
        print_menu([
            "Check Balance",
            "Deposit",
            "Withdraw",
            "Transactions",
            "Change PIN",
            "Logout"
        ])

        ch = input("Choice: ")

        if ch == "1":
            check_balance(acc)
        elif ch == "2":
            deposit(accounts, acc_no, acc)
        elif ch == "3":
            withdraw(accounts, acc_no, acc)
        elif ch == "4":
            show_transactions(acc)
        elif ch == "5":
            change_pin(accounts, acc_no, acc)
        elif ch == "6":
            break

def main_menu():
    accounts = load_data()

    while True:
        clear_screen()
        print_header("WELCOME")
        print_menu([
            "Login",
            "Create Account",
            "Exit"
        ])

        ch = input("Choice: ")

        if ch == "1":
            acc_no, acc = login(accounts)
            if acc_no:
                banking_menu(accounts, acc_no, acc)

        elif ch == "2":
            create_account(accounts)

        elif ch == "3":
            save_data(accounts)
            print("Goodbye!")
            break

# ENTRY POINT
if __name__ == "__main__":
    main_menu()
