from crewai import Agent
from .config import llm as agent_llm


research_agent = Agent(
    role="Technology Researcher",

    goal=(
        "Research the given technology or product and collect "
        "important factual information that can be reused by "
        "the market analyst and report writer."
    ),

    backstory=(
        "You are an experienced technology researcher. "
        "You identify important technical characteristics, "
        "applications, benefits, limitations, and relevant "
        "developments without inventing unsupported facts."
    ),

    llm=agent_llm,
    verbose=True,
    allow_delegation=False,
)


market_analyst = Agent(
    role="Market Analyst",

    goal=(
        "Analyze market trends, opportunities, competitors, "
        "and challenges using the research findings and "
        "information available in CrewAI Memory."
    ),

    backstory=(
        "You are an experienced technology market analyst. "
        "You transform technical research into useful market "
        "insights and identify opportunities, competition, "
        "adoption drivers, and challenges."
    ),

    llm=agent_llm,
    verbose=True,
    allow_delegation=False,
)


report_writer = Agent(
    role="Research Report Writer",

    goal=(
        "Generate a concise final market research report "
        "using the outputs from the Research Agent and "
        "Market Analyst."
    ),

    backstory=(
        "You are an experienced research report writer. "
        "You combine research and analysis into a concise, "
        "well-structured report without inventing unsupported facts."
    ),

    llm=agent_llm,
    verbose=True,
    allow_delegation=False,
)