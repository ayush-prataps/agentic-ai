from crewai import Task
from .agents import (
    research_agent,
    market_analyst,
    report_writer,
)


# Task 1 — Technology Research
research_task = Task(
    description="""
Research the following technology/product:

{technology}

Collect and summarize important information.

Your research should cover:

1. What the technology/product is
2. How it works at a high level
3. Main capabilities
4. Major applications
5. Key benefits
6. Important limitations
7. Current relevance
8. Important findings that a market analyst should know

Use reliable general knowledge available to you.

Do not invent statistics or unsupported quantitative claims.

The research findings should be detailed enough to be
useful to downstream tasks and suitable for storage in
CrewAI Memory.
""",

    expected_output="""
A concise but informative technology research summary
covering:

- Overview
- High-level working
- Capabilities
- Applications
- Benefits
- Limitations
- Current relevance
- Important research findings
""",

    agent=research_agent,
)


# Task 2 — Market Analysis
market_analysis_task = Task(
    description="""
Analyze the market for:

{technology}

Use the Research Agent's output provided through task
context.

Also use relevant information available in CrewAI Memory.

Analyze:

1. Current market trends
2. Market opportunities
3. Major competitors or competing technologies
4. Adoption drivers
5. Market challenges
6. Risks
7. Future market potential

Do not simply repeat the research findings.

Build meaningful market analysis from them.

Do not invent unsupported statistics, market sizes,
revenue figures, or customer numbers.
""",

    expected_output="""
A concise market analysis containing:

- Market trends
- Opportunities
- Competitors or competing technologies
- Adoption drivers
- Market challenges
- Risks
- Future potential
""",

    agent=market_analyst
)


# Task 3 — Final Report
report_writing_task = Task(
    description="""
Create a concise market research report for:

{technology}

Use:

1. The Technology Researcher's findings
2. The Market Analyst's analysis
3. Relevant information available in CrewAI Memory

The report should contain:

1. Executive Summary
2. Technology/Product Overview
3. Key Capabilities and Applications
4. Market Trends
5. Opportunities
6. Competitive Landscape
7. Challenges and Risks
8. Future Outlook
9. Conclusion

The report should be factual, concise, and well structured.

Do not invent unsupported statistics, market sizes,
revenue numbers, customer counts, or other quantitative claims.
""",

    expected_output="""
A concise market research report containing:

- Executive Summary
- Technology/Product Overview
- Capabilities and Applications
- Market Trends
- Opportunities
- Competitive Landscape
- Challenges and Risks
- Future Outlook
- Conclusion
""",

    agent=report_writer
)