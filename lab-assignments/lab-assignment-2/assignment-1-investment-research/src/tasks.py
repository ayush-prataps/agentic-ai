from crewai import Task

from .agents import (
    financial_analyst,
    market_analyst,
    risk_analyst,
    research_lead,
)

from .models import (
    FinancialAnalysis,
    MarketAnalysis,
    RiskAnalysis,
    InvestmentReport,
)


COMPANY_DATA = """
Company: NVIDIA Corporation

Hypothetical financial and business snapshot for educational analysis:

Financial Performance:
- Revenue growth: 38%
- Net profit margin: 52%
- Debt-to-equity ratio: 0.42
- Earnings growth: 45%

Business Context:
- Industry: Semiconductors and Artificial Intelligence Infrastructure
- Strong demand for AI accelerators and data center computing
- Strong ecosystem and software advantages through CUDA
- High dependence on continued AI infrastructure spending
- Increasing competition from AMD, Intel, custom silicon, and cloud providers
- Export restrictions and geopolitical tensions may affect international growth
- Valuation may be sensitive to expectations of future AI growth
"""


financial_analysis_task = Task(
    description=f"""
Analyze the following company financial data.

{COMPANY_DATA}

Evaluate:

1. Revenue growth
2. Profitability
3. Leverage
4. Earnings growth
5. Overall financial health
6. Major financial strengths
7. Major financial concerns

Return only information that can fit the FinancialAnalysis schema.
""",

    expected_output=(
        "A validated FinancialAnalysis object containing structured "
        "financial metrics, growth assessment, strengths, and concerns."
    ),

    agent=financial_analyst,
    output_pydantic=FinancialAnalysis,
)


market_analysis_task = Task(
    description=f"""
Analyze the market and industry conditions for the following company.

{COMPANY_DATA}

Evaluate:

1. Industry outlook
2. Competitive position
3. Market opportunities
4. Market challenges

Do not focus primarily on company financial ratios.
Focus on the external market and competitive environment.

Return the result according to the MarketAnalysis schema.
""",

    expected_output=(
        "A validated MarketAnalysis object containing industry, market "
        "outlook, competitive position, opportunities, and challenges."
    ),

    agent=market_analyst,
    output_pydantic=MarketAnalysis,
)


risk_analysis_task = Task(
    description=f"""
Analyze the major investment risks for the following company.

{COMPANY_DATA}

Identify risks across:

1. Financial risks
2. Competitive risks
3. Market risks
4. Regulatory and geopolitical risks
5. Technology risks
6. Valuation risks

Also identify factors that could mitigate those risks.

Return the result according to the RiskAnalysis schema.
""",

    expected_output=(
        "A validated RiskAnalysis object containing overall risk level, "
        "key risks, and risk mitigation factors."
    ),

    agent=risk_analyst,
    output_pydantic=RiskAnalysis,
)


investment_report_task = Task(
    description="""
You are the Head of Investment Research.

You will receive structured outputs from:

1. Financial Analyst
2. Market Analyst
3. Risk Analyst

Use those structured findings to produce the final investment report.

You must:

- Preserve the financial metrics from the Financial Analyst
- Use the Market Analyst's market outlook
- Use the Risk Analyst's key risks
- Form a balanced growth assessment
- Assign an investment rating
- Assign a confidence score between 0 and 100
- Provide a clear recommendation rationale

The final output MUST conform exactly to the InvestmentReport schema.

Do not invent unsupported facts.
Do not return markdown outside the structured schema.
""",

    expected_output=(
        "A validated InvestmentReport containing the final investment "
        "recommendation and all required structured fields."
    ),

    agent=research_lead,

    context=[
        financial_analysis_task,
        market_analysis_task,
        risk_analysis_task,
    ],

    output_pydantic=InvestmentReport,
)