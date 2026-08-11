from crewai import Task

from .agents import (
    incident_analyst,
    system_investigator,
    resolution_agent,
)

from .models import (
    IncidentClassification,
    InvestigationResult,
    IncidentResolutionReport,
)


INCIDENT_REPORT = """
Incident ID: INC-2026-001

Service: payment-service

Severity reported by monitoring: HIGH

Description:

Users are reporting failed payment transactions.

The API error rate increased rapidly during the last
15 minutes.

Average API response time has increased from
300 milliseconds to nearly 5 seconds.

The payment service is still partially operational,
but many transactions are failing.
"""


incident_analysis_task = Task(
    description=f"""
Analyze the following incident report:

{INCIDENT_REPORT}

Determine:

1. Incident type
2. Severity
3. Affected service
4. Observable symptoms
5. Initial technical assessment

Return the result according to the
IncidentClassification schema.
""",

    expected_output=(
        "A validated IncidentClassification object."
    ),

    agent=incident_analyst,
    output_pydantic=IncidentClassification,
)


system_investigation_task = Task(
    description="""
Investigate the incident identified by the Incident Analyst.

Use the Async System Investigation Tool to investigate
the affected service.

The tool concurrently collects:

- Application logs
- System metrics
- Service status

Analyze the collected information.

If any information source is unavailable, explicitly
mention it instead of inventing information.

Return the result according to the InvestigationResult schema.
""",

    expected_output=(
        "A validated InvestigationResult containing "
        "the affected service, logs, metrics, service "
        "status, investigation summary, and information quality."
    ),

    agent=system_investigator,

    context=[
        incident_analysis_task,
    ],

    output_pydantic=InvestigationResult,
)


incident_resolution_task = Task(
    description="""
Use the structured incident classification and structured
system investigation results to determine the most likely
root cause.

Produce:

1. Probable root cause
2. Supporting evidence
3. Immediate corrective actions
4. Recommended resolution
5. Long-term prevention measures
6. Any unresolved or missing information
7. Confidence level between 0 and 100

Do not claim certainty when the evidence is incomplete.

Return the result according to the
IncidentResolutionReport schema.
""",

    expected_output=(
        "A validated IncidentResolutionReport."
    ),

    agent=resolution_agent,

    context=[
        incident_analysis_task,
        system_investigation_task,
    ],

    output_pydantic=IncidentResolutionReport,
)