import os
from pathlib import Path

from dotenv import load_dotenv
import crewai.llms.cache as crewai_cache
from crewai import LLM


PROJECT_ROOT = Path(__file__).resolve().parents[3]
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE)


# Groq does not support CrewAI's cache_breakpoint field.
crewai_cache.mark_cache_breakpoint = lambda message: message


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError(
        f"GROQ_API_KEY not found in {ENV_FILE}"
    )


llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.2,
)