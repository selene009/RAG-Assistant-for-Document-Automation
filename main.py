# main.py

from src.embedder_bge import BGEEmbedder
from src.retriever_faiss import FaissRetriever
from src.router_intent import IntentRouter
from src.function_calling import FunctionCaller

docs = [
    "Financial regulation document…",
    "Insurance report…",
    "Risk assessment guidelines…"
]

# [Originality]
# End-to-end initialization of a modular RAG pipeline,
# reflecting real-world GenAI system composition.
embedder = BGEEmbedder()
retriever = FaissRetriever(embedder)
retriever.build_index(docs)

router = IntentRouter()
fc = FunctionCaller()

query = "Lookup policy details"

# [Originality]
# Intent is detected before retrieval or generation,
# enforcing explicit control over model behavior.
intent = router.detect(query)
result = router.route(intent, retriever, fc, query)

# [Result]
# Demonstrates a complete RAG + function-calling workflow:
# intent detection → routing → retrieval / structured execution.
print("Query:", query)
print("Intent:", intent)
print("Result:", result)
