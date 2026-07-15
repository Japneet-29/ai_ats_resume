from sentence_transformers import SentenceTransformer
from backend.core.config import SENTENCE_TRANSFORMER_MODEL

_embedder = None

def get_embedder():
    global _embedder

    if _embedder is None:
        print("Loading SentenceTransformer...")
        _embedder = SentenceTransformer(SENTENCE_TRANSFORMER_MODEL)
        print("SentenceTransformer loaded!")

    return _embedder