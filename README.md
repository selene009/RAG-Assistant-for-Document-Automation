# RAG Document Automation Assistant
A domain-independent Retrieval-Augmented Generation (RAG) pipeline built for long-document automation tasks.  
Originally developed for financial workflows, but the architecture is fully transferable to clinical documentation and guideline retrieval.

## Features
- BGE-based embedding wrapper (pseudo implementation)
- FAISS-like retrieval module
- Intent-based routing (RAG / structured lookup / math operations)
- Function-calling simulation for structured queries
- OCR + ASR multimodal components
- Architecture adaptable to clinical, financial, and compliance-heavy domains
## Project Structure
src/
embedder_bge.py # embedding wrapper
retriever_faiss.py # document retrieval
router_intent.py # intent detection + routing
function_calling.py # structured table lookup
ocr_asr_pipeline.py # OCR + ASR modules
main.py # demo runner
requirements.txt
README.md
## Technical Highlights
- Uses a modular RAG pipeline architecture
- Supports multimodal input routing (OCR/ASR)
- Includes structured lookup via function-calling
- Same workflow patterns used in:
  - Clinical documentation
  - AI scribe automation
  - Financial compliance automation

## Run Demo
python main.py



