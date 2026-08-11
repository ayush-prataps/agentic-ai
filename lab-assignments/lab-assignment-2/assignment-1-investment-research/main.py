import asyncio

from src.crew import investment_research_crew


def display_report(report):
    print("=" * 60)
    print("FINAL INVESTMENT RESEARCH REPORT")
    print("=" * 60)

    print(f"\nCompany:")
    print(report.company)

    print("\nFinancial Metrics:")
    print(report.financial_metrics.model_dump())

    print("\nGrowth Assessment:")
    print(report.growth_assessment)

    print("\nMarket Outlook:")
    print(report.market_outlook)

    print("\nKey Risks:")
    for risk in report.key_risks:
        print(f"- {risk}")

    print("\nInvestment Rating:")
    print(report.investment_rating)

    print("\nConfidence Score:")
    print(f"{report.confidence_score}%")

    print("\nRecommendation Rationale:")
    print(report.recommendation_rationale)

    print("\n" + "=" * 60)


async def main():
    result = await investment_research_crew.kickoff_async()

    final_report = result.pydantic

    display_report(final_report)

    print("\nMachine-readable JSON:")
    print(final_report.model_dump_json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())