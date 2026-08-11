from src.crew import startup_crew


def main():
    print("=" * 60)
    print("CREWAI STARTUP EVALUATION & INVESTOR PITCH")
    print("=" * 60)

    startup_idea = input(
        "\nEnter your startup idea:\n> "
    ).strip()

    if not startup_idea:
        raise ValueError(
            "Startup idea cannot be empty."
        )

    print("\n" + "=" * 60)
    print("STARTING MULTI-AGENT WORKFLOW")
    print("=" * 60)

    result = startup_crew.kickoff(
        inputs={
            "startup_idea": startup_idea
        }
    )

    print("\n" + "=" * 60)
    print("FINAL INVESTOR OUTPUT")
    print("=" * 60)

    print(result)


if __name__ == "__main__":
    main()