from src.crew import travel_planning_crew


# Current Groq pricing for llama-3.3-70b-versatile:
# $0.59 / 1M input tokens
# $0.79 / 1M output tokens
INPUT_PRICE_PER_MILLION = 0.59
OUTPUT_PRICE_PER_MILLION = 0.79


def calculate_cost(token_usage):
    """
    Estimate execution cost from CrewAI token usage.
    """

    if token_usage is None:
        return None

    prompt_tokens = getattr(
        token_usage,
        "prompt_tokens",
        0,
    )

    completion_tokens = getattr(
        token_usage,
        "completion_tokens",
        0,
    )

    input_cost = (
        prompt_tokens
        / 1_000_000
        * INPUT_PRICE_PER_MILLION
    )

    output_cost = (
        completion_tokens
        / 1_000_000
        * OUTPUT_PRICE_PER_MILLION
    )

    return {
        "input_tokens": prompt_tokens,
        "output_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
        "input_cost_usd": input_cost,
        "output_cost_usd": output_cost,
        "total_cost_usd": input_cost + output_cost,
    }


def print_metrics(result):

    print("\n")
    print("=" * 70)
    print("CREWAI USAGE METRICS")
    print("=" * 70)

    print("\nToken Usage:")
    print(result.token_usage)

    print("\nUsage Metrics:")
    print(result.usage_metrics)

    print("\nTool Failures:")
    print(result.tool_failures)

    cost = calculate_cost(
        result.token_usage
    )

    if cost:

        print("\nCost Analysis:")

        print(
            f"Input Tokens: "
            f"{cost['input_tokens']:,}"
        )

        print(
            f"Output Tokens: "
            f"{cost['output_tokens']:,}"
        )

        print(
            f"Total Tokens: "
            f"{cost['total_tokens']:,}"
        )

        print(
            f"Estimated Input Cost: "
            f"${cost['input_cost_usd']:.6f}"
        )

        print(
            f"Estimated Output Cost: "
            f"${cost['output_cost_usd']:.6f}"
        )

        print(
            f"Estimated Total Cost: "
            f"${cost['total_cost_usd']:.6f}"
        )


def print_task_outputs(result):

    print("\n")
    print("=" * 70)
    print("INDIVIDUAL TASK OUTPUTS")
    print("=" * 70)

    for index, task_output in enumerate(
        result.tasks_output,
        start=1,
    ):

        print("\n" + "-" * 70)
        print(f"TASK {index}")
        print("-" * 70)

        print("\nAgent:")
        print(task_output.agent)

        print("\nOutput:")
        print(task_output.raw)


def main():

    print("=" * 70)
    print("CREWAI AI TRAVEL PLANNING ASSISTANT")
    print("=" * 70)

    destination = input(
        "\nDestination:\n> "
    ).strip()

    travelers = int(
        input(
            "\nNumber of travelers:\n> "
        )
    )

    days = int(
        input(
            "\nNumber of days:\n> "
        )
    )

    print("\n")
    print("=" * 70)
    print("STARTING CREW")
    print("=" * 70)

    result = travel_planning_crew.kickoff(
        inputs={
            "destination": destination,
            "travelers": travelers,
            "days": days,
        }
    )

    # --------------------------------------------------------
    # Individual Task Outputs
    # --------------------------------------------------------

    print_task_outputs(result)

    # --------------------------------------------------------
    # Usage / Cost Analysis
    # --------------------------------------------------------

    print_metrics(result)

    # --------------------------------------------------------
    # Final Crew Output
    # --------------------------------------------------------

    print("\n")
    print("=" * 70)
    print("FINAL TRAVEL PLAN")
    print("=" * 70)

    print(result.raw)


if __name__ == "__main__":
    main()