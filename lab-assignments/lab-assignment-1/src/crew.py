from crewai import Crew, Process
from .agents import startup_analyst, startup_consultant
from .tasks import startup_analysis_task, startup_pitch_task


startup_crew = Crew(
    agents=[
        startup_analyst,
        startup_consultant,
    ],
    tasks=[
        startup_analysis_task,
        startup_pitch_task,
    ],
    process=Process.sequential,
    verbose=True,
)
