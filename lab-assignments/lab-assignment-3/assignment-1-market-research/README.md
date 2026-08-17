# CrewAI Market Research System

A multi-agent market research system built with **CrewAI**. It uses three specialized agents to research a technology/product, analyze its market, and generate a concise final report.

## Agents

* **Technology Researcher** — researches the technology, applications, benefits, and limitations.
* **Market Analyst** — analyzes trends, opportunities, competitors, risks, and future potential.
* **Report Writer** — combines the research and market analysis into the final report.

## Key CrewAI Concepts Demonstrated

* CrewAI **Memory** using `remember()` and `recall()`
* Local `all-MiniLM-L6-v2` embeddings
* Sequential multi-agent workflow
* Task output passing between agents
* Final aggregated report generation

## Tech Stack

* Python
* CrewAI
* Groq LLM
* Llama 3.3 70B
* Sentence Transformers
* `all-MiniLM-L6-v2`

## Run

```bash
python main.py
```

Enter a technology/product when prompted, for example:

```text
Foldable iPhone
```

The system then executes:

```text
Research → Memory → Recall → Market Analysis → Final Report
```
