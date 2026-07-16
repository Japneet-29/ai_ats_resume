from backend.core.embedder import get_embedder
from backend.services.jd_matcher import calculate_semantic_similarity

embedder = get_embedder()

resume = """
Python developer with FastAPI, React, SQL, Docker and AWS.
"""

jd = """
Looking for a backend engineer with Python, FastAPI and Docker experience.
"""

score = calculate_semantic_similarity(
    resume,
    jd
)

print(score)