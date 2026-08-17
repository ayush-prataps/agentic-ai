import os
from pathlib import Path

from dotenv import load_dotenv
import crewai.llms.cache as crewai_cache
from crewai import LLM, Memory


PROJECT_ROOT = Path(__file__).resolve().parents[4]
ENV_FILE = PROJECT_ROOT / ".env"
load_dotenv(ENV_FILE)


# CrewAI + Groq compatibility workaround.
# CrewAI currently injects a cache_breakpoint property
# into messages. Groq rejects this property.
crewai_cache.mark_cache_breakpoint = lambda message: message


# API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError(
        f"GROQ_API_KEY not found in {ENV_FILE}"
    )


llm = LLM(
    model="groq/qwen/qwen3.6-27b",
    temperature=0.2,
)


market_research_memory = Memory(
    llm=llm,
    embedder={
        "provider": "sentence-transformer",
        "config": {
            "model_name": "all-MiniLM-L6-v2",
        },
    },
)

STORAGE_DIR = PROJECT_ROOT / ".crewai"
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

os.environ["CREWAI_STORAGE_DIR"] = str(STORAGE_DIR)