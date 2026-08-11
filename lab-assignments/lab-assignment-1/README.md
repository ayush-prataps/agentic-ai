# Lab Assignment 1 — Startup Evaluation & Investor Pitch

## Problem Statement

Build a two-agent AI system using CrewAI to evaluate a hypothetical
startup idea and generate a corresponding elevator pitch and pitch
deck outline.

The system simulates two roles in a startup ecosystem:

1. Startup Analyst
2. Startup Consultant

---

## System Architecture

```text
                    Startup Idea
                         |
                         v
                 +---------------+
                 | Startup       |
                 | Analyst       |
                 +---------------+
                         |
                         | Startup Analysis
                         v
                 +---------------+
                 | Analyst       |
                 | Report        |
                 +---------------+
                         |
                         | Task Context
                         v
                 +---------------+
                 | Startup       |
                 | Consultant    |
                 +---------------+
                    /          \
                   /            \
                  v              v
        Elevator Pitch      Pitch Deck Outline
```

## Technical Notes

This project uses Groq as the LLM provider through CrewAI/LiteLLM.

CrewAI currently injects an internal `cache_breakpoint` message
property that is rejected by Groq. A small compatibility patch is
therefore applied during startup to disable this internal marker.

This workaround does not affect the multi-agent workflow or task
context mechanism.