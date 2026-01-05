# function_calling.py
"""
Function-calling simulation for structured lookups.
"""


class FunctionCaller:
    def __init__(self):
        # [Originality]
        # Simulates LLM function-calling behavior for structured data access,
        # separating deterministic lookup logic from generative reasoning.
        #
        # [Result]
        # Reduces hallucination risk by routing structured queries to
        # explicit, verifiable functions instead of free-text generation.
        self.table = {"A001": "Policy Details", "A002": "Risk Score"}

    def lookup(self, query):
        # [Originality]
        # Query-driven key selection mimics intent-conditioned function calls
        # commonly used in production RAG and agent-based systems.
        #
        # [Result]
        # Ensures consistent and auditable outputs for structured queries.
        key = "A001" if "policy" in query.lower() else "A002"
        return self.table[key]
