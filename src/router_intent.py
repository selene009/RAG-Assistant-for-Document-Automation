# router_intent.py
"""
Intent-based routing for RAG.
"""

class IntentRouter:
    def detect(self, query):
        if "sum" in query.lower():
            return "math"
        if "table" in query.lower():
            return "structured_lookup"
        return "rag"

    def route(self, intent, retriever, fc, query):
        if intent == "structured_lookup":
            return fc.lookup(query)
        elif intent == "math":
            return f"Result: {eval('2+3')}"
        else:
            return retriever.search(query)
