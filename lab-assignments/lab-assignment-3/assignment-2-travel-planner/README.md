# CrewAI AI Travel Planning Assistant

An AI-powered travel planning system built with **CrewAI**. It uses three specialized agents and custom tools to gather destination information, calculate realistic travel budgets, and generate a day-by-day travel itinerary.

## Agents

* **Travel Researcher** — researches destination attractions, best times to visit, and general travel information using custom `DestinationInfoTool`.
* **Travel Budget Analyst** — calculates estimated costs for accommodation, food, transportation, and activities using custom `CostCalculatorTool`.
* **Itinerary Planner** — synthesizes destination research and budget breakdown into a structured, day-by-day itinerary.

## Custom Tools

* **`DestinationInfoTool`** — fetches destination data and demonstrates agent self-healing via tool retry.
* **`CostCalculatorTool`** — calculates structured budget estimates based on destination, duration, and traveler count.

## Key CrewAI Concepts Demonstrated

* Custom CrewAI **Tools** using `BaseTool` and `pydantic` schemas
* Agent error recovery & retry handling via `max_iter`
* Sequential multi-agent execution pipeline
* Token usage tracking and execution cost estimation

## Tech Stack

* Python
* CrewAI & CrewAI Tools
* Groq LLM (`groq/qwen/qwen3.6-27b`)
* Pydantic

## Run

```bash
python main.py
```

Enter travel details when prompted:

```text
Destination: Goa
Number of travelers: 2
Number of days: 4
```

The system then executes:

```text
Destination Research → Budget Analysis → Itinerary Planning → Metrics & Final Output
```
