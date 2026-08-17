import os
from pathlib import Path

from dotenv import load_dotenv
import crewai.llms.cache as crewai_cache
from crewai import LLM


PROJECT_ROOT = Path(__file__).resolve().parents[3]

ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE)


# ---------------------------------------------------------
# CrewAI + Groq compatibility workaround
# ---------------------------------------------------------
#
# CrewAI currently injects a `cache_breakpoint` property
# into messages. Groq rejects this property.
#
# This disables CrewAI's internal cache-breakpoint marker.
# It does NOT disable our own application-level caching.
#
crewai_cache.mark_cache_breakpoint = lambda message: message


# ---------------------------------------------------------
# Groq configuration
# ---------------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError(
        f"GROQ_API_KEY not found in {ENV_FILE}"
    )


llm = LLM(
    model="groq/qwen/qwen3.6-27b",
    temperature=0.2,
)