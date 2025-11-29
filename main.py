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

embedder = BGEEmbedder()
retriever = FaissRetriever(embedder)
retriever.build_index(docs)

router = IntentRouter()
fc = FunctionCaller()

query = "Lookup policy details"
intent = router.detect(query)
result = router.route(intent, retriever, fc, query)

print("Query:", query)
print("Intent:", intent)
print("Result:", result)
