from crewai import Crew, Process

from .agents import (
    incident_analyst,
    system_investigator,
    resolution_agent,
)

from .tasks import (
    incident_analysis_task,
    system_investigation_task,
    incident_resolution_task,
)


incident_response_crew = Crew(
    agents=[
        incident_analyst,
        system_investigator,
        resolution_agent,
    ],

    tasks=[
        incident_analysis_task,
        system_investigation_task,
        incident_resolution_task,
    ],

    process=Process.sequential,
    verbose=True,
)