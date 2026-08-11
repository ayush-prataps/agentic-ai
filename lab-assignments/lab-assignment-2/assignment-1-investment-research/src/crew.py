from crewai import Crew, Process

from .agents import (
    financial_analyst,
    market_analyst,
    risk_analyst,
    research_lead,
)

from .tasks import (
    financial_analysis_task,
    market_analysis_task,
    risk_analysis_task,
    investment_report_task,
)


investment_research_crew = Crew(
    agents=[
        financial_analyst,
        market_analyst,
        risk_analyst,
        research_lead,
    ],

    tasks=[
        financial_analysis_task,
        market_analysis_task,
        risk_analysis_task,
        investment_report_task,
    ],

    process=Process.sequential,
    verbose=True,
)