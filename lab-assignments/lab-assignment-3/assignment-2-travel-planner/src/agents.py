from crewai import Agent

from .config import llm
from .tools import (
    DestinationInfoTool,
    CostCalculatorTool,
)


destination_info_tool = DestinationInfoTool()
cost_calculator_tool = CostCalculatorTool()


destination_research_agent = Agent(
    role="Travel Researcher",

    goal=(
        "Research the specified travel destination using "
        "DestinationInfoTool and provide useful destination "
        "information for the travel planner."
    ),

    backstory=(
        "You are an experienced travel researcher who "
        "collects practical destination information including "
        "attractions, timing, and travel considerations."
    ),

    tools=[
        destination_info_tool,
    ],

    llm=llm,
    verbose=True,
    allow_delegation=False,
    # Allows the agent to retry after a tool failure.
    max_iter=5,
)


budget_analyst = Agent(
    role="Travel Budget Analyst",

    goal=(
        "Estimate a realistic travel budget using the "
        "CostCalculatorTool and the destination research."
    ),

    backstory=(
        "You are a travel budget analyst who specializes in "
        "estimating accommodation, food, transportation, "
        "and activity costs."
    ),

    tools=[
        cost_calculator_tool,
    ],

    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=5,
)


travel_planner = Agent(
    role="Itinerary Planner",

    goal=(
        "Create a concise and practical final travel itinerary "
        "using the destination research and budget analysis."
    ),

    backstory=(
        "You are an experienced travel planner who combines "
        "destination information and budget constraints into "
        "a practical itinerary."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False,
)