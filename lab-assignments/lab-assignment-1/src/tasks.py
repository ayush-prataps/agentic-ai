from crewai import Task
from .agents import startup_analyst, startup_consultant


startup_analysis_task = Task(
    description="""
Evaluate the following hypothetical startup idea:

{startup_idea}

Analyze the idea from both a startup and investor perspective.

Your analysis must cover:

1. Problem being solved
2. Proposed solution
3. Target customers
4. Market need
5. Feasibility
6. Uniqueness and differentiation
7. Key strengths
8. Key weaknesses
9. Major risks
10. Potential business model
11. Overall startup assessment

Be analytical and realistic.

Do not blindly praise the startup idea.
Identify weaknesses, risks, assumptions, and potential
failure points.

The report will be passed to another agent, so make the
analysis clear and actionable.
""",

    expected_output="""
A clear startup analyst report containing:

- Problem
- Proposed solution
- Target customers
- Market need
- Feasibility assessment
- Uniqueness and differentiation
- Strengths
- Weaknesses
- Major risks
- Potential business model
- Overall assessment
""",

    agent=startup_analyst,
)


startup_pitch_task = Task(
    description="""
Create investor-facing material for the following startup idea:

{startup_idea}

You must use the Startup Analyst's report provided as
context for this task.

Produce TWO outputs:

1. ELEVATOR PITCH

Create a concise investor-oriented elevator pitch explaining:

- The problem
- The solution
- Target customers
- Main value proposition
- Differentiation
- Business potential

2. PITCH DECK OUTLINE

Create an 8-10 slide pitch deck outline.

For every slide provide:

- Slide number
- Slide title
- Key points that should be presented

The pitch must be grounded in the Startup Analyst's findings.

Do not invent unsupported statistics, revenue numbers,
market sizes, customer counts, funding amounts, or
other quantitative claims.

If the analyst identified important weaknesses or risks,
reflect them appropriately in the pitch.
""",

    expected_output="""
An investor-ready response containing:

ELEVATOR PITCH
A concise investor elevator pitch.

PITCH DECK OUTLINE
An 8-10 slide pitch deck outline with slide titles
and key talking points.
""",

    agent=startup_consultant,

    context=[startup_analysis_task],
)
