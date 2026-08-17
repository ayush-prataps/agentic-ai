from src.config import market_research_memory
from src.agents import (
    research_agent,
    market_analyst,
    report_writer,
)
from src.tasks import (
    research_task,
    market_analysis_task,
    report_writing_task,
)


def main():

    print("=" * 70)
    print("CREWAI MULTI-AGENT MARKET RESEARCH SYSTEM")
    print("=" * 70)

    technology = input(
        "\nEnter a technology/product to research:\n> "
    ).strip()

    if not technology:
        raise ValueError(
            "Technology/product cannot be empty."
        )

    print("\n" + "=" * 70)
    print("STEP 1 — RESEARCH AGENT")
    print("=" * 70)

    research_task.description = research_task.description.format(
    technology=technology
)

    research_result = research_agent.execute_task(
        task=research_task
    )

    research_findings = str(research_result)

    print("\nResearch completed.")


    print("\n" + "=" * 70)
    print("STEP 2 — STORE RESEARCH IN MEMORY")
    print("=" * 70)

    market_research_memory.remember(
        f"""
Technology/Product: {technology}

Research Findings:
{research_findings}
""",
        scope="/market-research",
        categories=["technology", "market-research"],
        importance=0.8,
    )

    print("Research findings stored in CrewAI Memory.")


    print("\n" + "=" * 70)
    print("STEP 3 — RECALL MEMORY")
    print("=" * 70)

    memories = market_research_memory.recall(
        f"Important research findings about {technology}",
        limit=5,
        depth="shallow",
    )

    memory_context = "\n\n".join(
        memory.record.content
        for memory in memories
    )

    if not memory_context:
        memory_context = "No relevant memories were retrieved."

    print("Memory retrieved successfully.")

    print("\nRetrieved Memory:")
    print(memory_context)


    print("\n" + "=" * 70)
    print("STEP 4 — MARKET ANALYST")
    print("=" * 70)

    market_analysis_task.description = market_analysis_task.description.format(
        technology=technology,
        research_findings=research_findings,
        memory_context=memory_context,
    )

    market_result = market_analyst.execute_task(
        task=market_analysis_task
    )

    market_analysis = str(market_result)

    print("\nMarket analysis completed.")


    print("\n" + "=" * 70)
    print("STEP 5 — REPORT WRITER")
    print("=" * 70)

    report_writing_task.description = report_writing_task.description.format(
        technology=technology,
        research_findings=research_findings,
        market_analysis=market_analysis,
    )

    report_result = report_writer.execute_task(
        task=report_writing_task
    )

    print("\n" + "=" * 70)
    print("FINAL MARKET RESEARCH REPORT")
    print("=" * 70)

    print(report_result)


if __name__ == "__main__":
    main()