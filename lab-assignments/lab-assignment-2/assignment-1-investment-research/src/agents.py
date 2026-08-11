from crewai import Agent

from .config import llm


financial_analyst = Agent(
    role="Senior Financial Analyst",

    goal=(
        "Analyze the company's financial performance using the provided data "
        "and produce a rigorous structured financial assessment."
    ),

    backstory=(
        "You are an experienced equity research analyst specializing in "
        "revenue growth, profitability, leverage, earnings quality, and "
        "financial health."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False,
)


market_analyst = Agent(
    role="Market and Industry Analyst",

    goal=(
        "Evaluate the company's industry conditions, competitive position, "
        "market opportunities, and market challenges."
    ),

    backstory=(
        "You are a strategic market analyst with expertise in industry trends, "
        "competitive dynamics, market opportunities, and long-term outlook."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False,
)


risk_analyst = Agent(
    role="Investment Risk Analyst",

    goal=(
        "Identify and assess the major risks associated with investing "
        "in the company."
    ),

    backstory=(
        "You are a skeptical and detail-oriented risk analyst. "
        "You identify financial, operational, competitive, regulatory, "
        "and macroeconomic risks."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False,
)


research_lead = Agent(
    role="Head of Investment Research",

    goal=(
        "Combine the structured findings from the specialist analysts "
        "into a balanced and validated investment recommendation."
    ),

    backstory=(
        "You lead an institutional investment research team. "
        "You synthesize financial performance, market conditions, and "
        "investment risks into clear, evidence-based recommendations."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False,
)