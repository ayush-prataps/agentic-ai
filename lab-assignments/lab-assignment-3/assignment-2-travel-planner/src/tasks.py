from crewai import Task

from .agents import (
    destination_research_agent,
    budget_analyst,
    travel_planner,
)


# Task 1 — Destination Research
destination_research_task = Task(
    description="""
Research the following travel destination:

{destination}

Use DestinationInfoTool to obtain:

1. Major attractions
2. Best time to visit
3. Basic travel information

If the tool initially fails, handle the failure appropriately
and retry when possible.

Return a concise destination research summary.
""",

    expected_output="""
A concise destination research summary containing:

- Destination
- Major attractions
- Best time to visit
- Basic travel information
""",

    agent=destination_research_agent,
)


# Task 2 — Budget Analysis
budget_task = Task(
    description="""
Estimate the travel budget for:

Destination: {destination}
Number of travelers: {travelers}
Number of days: {days}

Use CostCalculatorTool.

Calculate:

- Accommodation
- Food
- Transportation
- Activities
- Total estimated cost

Use the destination research provided through task context
when preparing the estimate.
""",

    expected_output="""
A travel budget containing:

- Accommodation cost
- Food cost
- Transportation cost
- Activity cost
- Total estimated cost
""",

    agent=budget_analyst,

    context=[
        destination_research_task,
    ],
)


# Task 3 — Final Itinerary
travel_plan_task = Task(
    description="""
Create a concise travel plan for:

Destination: {destination}
Travelers: {travelers}
Days: {days}

Use:

1. Destination research
2. Budget analysis

Create:

- Trip overview
- Suggested itinerary
- Major attractions
- Budget summary
- Practical travel tips

Keep the itinerary realistic and concise.

Clearly state that the budget is an estimate.
""",

    expected_output="""
A concise final travel plan containing:

- Trip overview
- Day-by-day itinerary
- Major attractions
- Budget summary
- Practical travel tips
""",

    agent=travel_planner,

    context=[
        destination_research_task,
        budget_task,
    ],
)