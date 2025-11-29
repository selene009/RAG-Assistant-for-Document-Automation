# function_calling.py
"""
Function-calling simulation for structured lookups.
"""


class FunctionCaller:
    def __init__(self):
        # fake table
        self.table = {"A001": "Policy Details", "A002": "Risk Score"}

    def lookup(self, query):
        # pseudo logic
        key = "A001" if "policy" in query.lower() else "A002"
        return self.table[key]
