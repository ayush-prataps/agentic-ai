from typing import List, Literal

from pydantic import BaseModel, Field


class FinancialMetrics(BaseModel):
    revenue_growth_percent: float = Field(
        description="Year-over-year revenue growth percentage"
    )

    profit_margin_percent: float = Field(
        description="Net profit margin percentage"
    )

    debt_to_equity: float = Field(
        description="Debt-to-equity ratio"
    )

    earnings_growth_percent: float = Field(
        description="Year-over-year earnings growth percentage"
    )

    financial_health: Literal[
        "Strong",
        "Moderate",
        "Weak",
    ]


class FinancialAnalysis(BaseModel):
    company: str
    financial_metrics: FinancialMetrics
    growth_assessment: str
    strengths: List[str]
    concerns: List[str]


class MarketAnalysis(BaseModel):
    company: str
    industry: str

    market_outlook: Literal[
        "Positive",
        "Neutral",
        "Negative",
    ]

    competitive_position: str
    market_opportunities: List[str]
    market_challenges: List[str]


class RiskAnalysis(BaseModel):
    company: str

    overall_risk_level: Literal[
        "Low",
        "Medium",
        "High",
    ]

    key_risks: List[str]
    risk_mitigation_factors: List[str]


class InvestmentReport(BaseModel):
    company: str

    financial_metrics: FinancialMetrics

    growth_assessment: str

    market_outlook: Literal[
        "Positive",
        "Neutral",
        "Negative",
    ]

    key_risks: List[str]

    investment_rating: Literal[
        "Strong Buy",
        "Buy",
        "Hold",
        "Sell",
        "Strong Sell",
    ]

    confidence_score: float = Field(
        ge=0,
        le=100,
        description="Confidence score between 0 and 100",
    )

    recommendation_rationale: str