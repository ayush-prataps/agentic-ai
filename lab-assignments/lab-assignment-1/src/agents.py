from crewai import Agent
from .config import llm


startup_analyst = Agent(
    role="Startup Analyst",
    goal=(
        "Evaluate a hypothetical startup idea for feasibility, "
        "uniqueness, target-market relevance, strengths, "
        "weaknesses, risks, and business potential."
    ),
    backstory=(
        "You are an experienced startup analyst who evaluates "
        "early-stage business ideas from a practical investor "
        "and market perspective. You are analytical, skeptical, "
        "and avoid unsupported claims."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)


startup_consultant = Agent(
    role="Startup Consultant",
    goal=(
        "Use the startup analyst's evaluation to create a "
        "compelling investor elevator pitch and pitch deck outline."
    ),
    backstory=(
        "You are an experienced startup consultant who helps "
        "founders communicate their ideas to investors. You turn "
        "analytical findings into concise, persuasive, and "
        "realistic investor messaging."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)
