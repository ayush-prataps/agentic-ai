from crewai import Crew, Process
from .agents import (
    research_agent,
    market_analyst,
    report_writer,
)
from .tasks import (
    research_task,
    market_analysis_task,
    report_writing_task,
)


market_research_crew = Crew(
    agents=[
        research_agent,
        market_analyst,
        report_writer,
    ],

    tasks=[
        research_task,
        market_analysis_task,
        report_writing_task,
    ],

    process=Process.sequential,
    verbose=True,
)