from crewai import Crew, Process

from .agents import (
    destination_research_agent,
    budget_analyst,
    travel_planner,
)

from .tasks import (
    destination_research_task,
    budget_task,
    travel_plan_task,
)


travel_planning_crew = Crew(
    agents=[
        destination_research_agent,
        budget_analyst,
        travel_planner,
    ],

    tasks=[
        destination_research_task,
        budget_task,
        travel_plan_task,
    ],

    process=Process.sequential,
    verbose=True,
)