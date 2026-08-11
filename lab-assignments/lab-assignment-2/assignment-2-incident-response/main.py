import asyncio

from src.crew import incident_response_crew


def display_report(report):
    print("=" * 60)
    print("FINAL INCIDENT RESOLUTION REPORT")
    print("=" * 60)

    print("\nIncident ID:")
    print(report.incident_id)

    print("\nIncident Type:")
    print(report.incident_type)

    print("\nSeverity:")
    print(report.severity)

    print("\nAffected Service:")
    print(report.affected_service)

    print("\nProbable Cause:")
    print(report.probable_cause)

    print("\nEvidence:")
    for item in report.evidence:
        print(f"- {item}")

    print("\nImmediate Actions:")
    for item in report.immediate_actions:
        print(f"- {item}")

    print("\nRecommended Actions:")
    for item in report.recommended_actions:
        print(f"- {item}")

    print("\nLong-Term Prevention:")
    for item in report.long_term_prevention:
        print(f"- {item}")

    print(
        f"\nResolution Confidence: "
        f"{report.resolution_confidence}%"
    )

    print("\nUnresolved Information:")
    for item in report.unresolved_information:
        print(f"- {item}")

    print("\n" + "=" * 60)


async def main():
    result = await incident_response_crew.kickoff_async()

    final_report = result.pydantic

    display_report(final_report)

    print("\nMachine-readable JSON:")
    print(final_report.model_dump_json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())