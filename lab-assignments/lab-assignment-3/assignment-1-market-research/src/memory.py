from crewai import Memory
from .config import llm as memory_llm


market_research_memory = Memory(
    llm=memory_llm,
    embedder={
        "provider": "sentence-transformer",
        "config": {
            "model_name": "all-MiniLM-L6-v2",
        },
    },
)