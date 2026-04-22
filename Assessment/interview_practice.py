# Interview Practice — Foundations + Real World
# These mirror the style of prompt you'd get in a coding foundations interview.
# Work through one problem at a time. Talk through your thinking out loud.
# ─────────────────────────────────────────────────────────────────────────────


# ── PROBLEM 1 ─────────────────────────────────────────────────────────────────
# Most Frequent Item
#
# Given a list of strings, return the one that appears most often.
# If there's a tie, return any one of them.
#
# Example:
#   most_frequent(["apple", "banana", "apple", "cherry", "banana", "apple"])
#   → "apple"

def most_frequent(items):
    
    pass


# ── PROBLEM 2 ─────────────────────────────────────────────────────────────────
# Name Formatter
#
# Given a list of names in "First Last" format, return them reformatted as
# "Last, First" and sorted alphabetically by last name.
#
# Example:
#   format_names(["John Smith", "Ada Lovelace", "Grace Hopper"])
#   → ["Hopper, Grace", "Lovelace, Ada", "Smith, John"]

def format_names(names):
    pass


# ── PROBLEM 3 ─────────────────────────────────────────────────────────────────
# Total Spend Per User
#
# You're given a list of transaction dicts, each with a "user" and "amount".
# Return a dict mapping each user to their total spend,
# sorted by total (highest first).
#
# Example:
#   transactions = [
#       {"user": "alice", "amount": 50},
#       {"user": "bob",   "amount": 30},
#       {"user": "alice", "amount": 20},
#   ]
#   total_spend(transactions) → {"alice": 70, "bob": 30}

def total_spend(transactions):
    pass


# ── PROBLEM 4 ─────────────────────────────────────────────────────────────────
# Parse Server Logs
#
# You're given a list of log lines, each in this format:
#   "YYYY-MM-DD username ACTION"
#
# Return a dict mapping each username to the list of actions they performed,
# in the order they appear in the log.
#
# Example:
#   logs = [
#       "2024-01-10 alice LOGIN",
#       "2024-01-10 bob LOGIN",
#       "2024-01-11 alice UPLOAD",
#       "2024-01-11 alice LOGOUT",
#   ]
#   parse_logs(logs) → {
#       "alice": ["LOGIN", "UPLOAD", "LOGOUT"],
#       "bob":   ["LOGIN"]
#   }

def parse_logs(logs):
    pass


# ── PROBLEM 5 ─────────────────────────────────────────────────────────────────
# Shopping Cart
#
# Implement a ShoppingCart class that supports:
#   add_item(name, price)    — add an item with its price
#   remove_item(name)        — remove an item by name (do nothing if not found)
#   get_total()              — return the sum of all item prices
#   get_items()              — return the list of item names currently in the cart
#
# Example:
#   cart = ShoppingCart()
#   cart.add_item("shirt", 29.99)
#   cart.add_item("jeans", 59.99)
#   cart.remove_item("shirt")
#   cart.get_total()   → 59.99
#   cart.get_items()   → ["jeans"]

class ShoppingCart:
    def __init__(self):
        pass

    def add_item(self, name, price):
        pass

    def remove_item(self, name):
        pass

    def get_total(self):
        pass

    def get_items(self):
        pass


# ── PROBLEM 6 ─────────────────────────────────────────────────────────────────
# Top Earners by Department
#
# Given a list of employee dicts (each with "name", "department", "salary"),
# return a dict mapping each department to the name of its highest-paid employee.
#
# Example:
#   employees = [
#       {"name": "Alice", "department": "Engineering", "salary": 95000},
#       {"name": "Bob",   "department": "Engineering", "salary": 88000},
#       {"name": "Carol", "department": "Marketing",   "salary": 72000},
#       {"name": "Dave",  "department": "Marketing",   "salary": 75000},
#   ]
#   top_earners(employees) → {"Engineering": "Alice", "Marketing": "Dave"}

def top_earners(employees):
    pass


# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Problem 1
    print("── Problem 1 ──")
    print(most_frequent(["apple", "banana", "apple", "cherry", "banana", "apple"]))
    # Expected: "apple"

    # Problem 2
    print("\n── Problem 2 ──")
    print(format_names(["John Smith", "Ada Lovelace", "Grace Hopper"]))
    # Expected: ["Hopper, Grace", "Lovelace, Ada", "Smith, John"]

    # Problem 3
    print("\n── Problem 3 ──")
    txns = [
        {"user": "alice", "amount": 50},
        {"user": "bob",   "amount": 30},
        {"user": "alice", "amount": 20},
        {"user": "bob",   "amount": 90},
    ]
    print(total_spend(txns))
    # Expected: {"bob": 120, "alice": 70}

    # Problem 4
    print("\n── Problem 4 ──")
    logs = [
        "2024-01-10 alice LOGIN",
        "2024-01-10 bob LOGIN",
        "2024-01-11 alice UPLOAD",
        "2024-01-11 alice LOGOUT",
    ]
    print(parse_logs(logs))
    # Expected: {"alice": ["LOGIN", "UPLOAD", "LOGOUT"], "bob": ["LOGIN"]}

    # Problem 5
    print("\n── Problem 5 ──")
    cart = ShoppingCart()
    cart.add_item("shirt", 29.99)
    cart.add_item("jeans", 59.99)
    cart.add_item("hat", 15.00)
    cart.remove_item("shirt")
    print(cart.get_total())   # 74.99
    print(cart.get_items())   # ["jeans", "hat"]

    # Problem 6
    print("\n── Problem 6 ──")
    employees = [
        {"name": "Alice", "department": "Engineering", "salary": 95000},
        {"name": "Bob",   "department": "Engineering", "salary": 88000},
        {"name": "Carol", "department": "Marketing",   "salary": 72000},
        {"name": "Dave",  "department": "Marketing",   "salary": 75000},
    ]
    print(top_earners(employees))
    # Expected: {"Engineering": "Alice", "Marketing": "Dave"}
