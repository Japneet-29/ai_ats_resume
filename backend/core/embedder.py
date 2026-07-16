import requests
import numpy as np

from backend.core.config import JINA_API_KEY

MODEL = "jina-embeddings-v3"


class JinaEmbedder:
    def __init__(self):
        self.url = "https://api.jina.ai/v1/embeddings"
        self.headers = {
            "Authorization": f"Bearer {JINA_API_KEY}",
            "Content-Type": "application/json",
        }

    def encode(self, texts):
        if isinstance(texts, str):
            texts = [texts]

        payload = {
            "model": MODEL,
            "input": texts,
        }

        response = requests.post(
            self.url,
            headers=self.headers,
            json=payload,
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()["data"]

        embeddings = [item["embedding"] for item in data]

        if len(embeddings) == 1:
            return np.array(embeddings[0])

        return np.array(embeddings)


_embedder = None


def get_embedder():
    global _embedder

    if _embedder is None:
        print("Initializing Jina Embedder...")
        _embedder = JinaEmbedder()

    return _embedder