from crewai import Agent

from .config import llm
from .tools import async_investigation_tool


incident_analyst = Agent(
    role="Incident Analyst",

    goal=(
        "Analyze incoming incident reports and "
        "classify the incident accurately."
    ),

    backstory=(
        "You are an experienced Site Reliability Engineer "
        "who specializes in incident classification, "
        "severity assessment, and identifying affected systems."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False,
)


system_investigator = Agent(
    role="System Investigator",

    goal=(
        "Investigate incidents by retrieving logs, "
        "system metrics, and service health information."
    ),

    backstory=(
        "You are a senior production systems engineer. "
        "When investigating an incident, use the "
        "Async System Investigation Tool to collect "
        "monitoring information from the affected service."
    ),

    tools=[
        async_investigation_tool
    ],

    llm=llm,
    verbose=True,
    allow_delegation=False,
)


resolution_agent = Agent(
    role="Resolution Agent",

    goal=(
        "Determine the most probable root cause of the incident "
        "and recommend safe and effective corrective actions."
    ),

    backstory=(
        "You are a senior incident commander experienced in "
        "root cause analysis, incident mitigation, and "
        "long-term reliability improvements."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False,
)