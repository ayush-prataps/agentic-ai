# Lab Assignment 2 — Advanced CrewAI Workflows

This lab demonstrates advanced CrewAI concepts through two independent multi-agent systems:

1. **Multi-Agent Financial Research & Investment Report Generator**
2. **Multi-Agent IT Incident Response System**

---

## 1. Learning Objectives

This lab demonstrates:

* Multi-agent collaboration
* Sequential CrewAI workflows
* Task-to-task context passing
* Pydantic structured outputs
* Custom CrewAI tools
* Asynchronous operations
* Concurrent data collection
* Application-level caching
* Retry and fallback mechanisms
* Graceful failure handling
* Structured incident and investment reports

The goal is to understand how multiple specialized agents can work together to solve complex real-world problems instead of relying on a single general-purpose agent.



---

# 2. Assignment 1 — Multi-Agent Financial Research & Investment Report Generator

## Problem

Build a multi-agent financial research system that analyzes a publicly traded company and produces a **structured investment research report**.

The system must ensure that each agent produces **validated structured output (Pydantic-based)** instead of unstructured text.

---

## Agents

### Financial Analyst

Analyzes financial performance and key ratios:

* Revenue growth
* Profitability
* Debt-to-equity ratio
* Earnings growth
* Overall financial health
* Financial strengths
* Financial concerns

---

### Market Analyst

Evaluates industry and market conditions:

* Industry outlook
* Competitive position
* Market opportunities
* Market challenges

---

### Risk Analyst

Identifies investment risks:

* Financial risks
* Competitive risks
* Market risks
* Regulatory and geopolitical risks
* Technology risks
* Valuation risks
* Risk mitigation factors

---

### Research Lead

Aggregates structured outputs from all analysts and produces the final investment recommendation.

---

## Architecture

```text
                    Company Data
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
   Financial Analyst  Market Analyst  Risk Analyst
          |              |              |
          +--------------+--------------+
                         |
                         v
                 Research Lead
                         |
                         v
             Investment Report
```

The workflow is sequential, but each agent operates independently with a clearly defined responsibility.

---

## Structured Output (Pydantic Requirement)

Each specialist agent returns structured data defined using Pydantic models.

The final report includes:

* Company
* Financial metrics
* Growth assessment
* Market outlook
* Key risks
* Investment rating
* Confidence score
* Recommendation rationale

This ensures:

* Machine-readable output
* Validation of agent responses
* Reliable downstream consumption

---

## CrewAI Concepts Demonstrated

* `Agent`
* `Task`
* `Crew`
* `Process.sequential`
* Task context passing
* Pydantic structured outputs
* Multi-agent specialization

---

# 3. Assignment 2 — Multi-Agent IT Incident Response System

## Problem

Build a multi-agent IT incident response system that receives an incident report, gathers system information using custom tools, and produces a structured resolution report.

This assignment focuses on:

* Custom tools
* Asynchronous execution
* Caching
* Failure handling policies
* Tool-based agent augmentation

---

## Agents

### Incident Analyst

Classifies the incident:

* Incident type
* Severity
* Affected service
* Symptoms
* Initial assessment

---

### System Investigator

Uses custom tools to retrieve system data:

* Application logs
* System metrics
* Service status

---

### Resolution Agent

Produces final resolution:

* Probable cause
* Supporting evidence
* Immediate actions
* Recommended actions
* Long-term prevention
* Unresolved information
* Resolution confidence

---

## Architecture

```text
                  Incident Report
                        |
                        v
                Incident Analyst
                        |
                        v
              Incident Classification
                        |
                        v
               System Investigator
                        |
                        v
          Async Investigation Tool
                        |
             +----------+----------+
             |          |          |
             v          v          v
           Logs      Metrics     Status
             |          |          |
             +----------+----------+
                        |
                 asyncio.gather()
                        |
                        v
                     Cache
                        |
                        v
              Investigation Result
                        |
                        v
                Resolution Agent
                        |
                        v
           Incident Resolution Report
```

---

# 4. Custom Tools (Required Feature)

The System Investigator uses **at least two custom tools**, including:

### Async System Investigation Tool

Simulates concurrent monitoring operations:

* `fetch_logs()`
* `fetch_metrics()`
* `fetch_service_status()`

Executed using:

```python
asyncio.gather()
```

This enables parallel data collection instead of sequential blocking calls.

---

# 5. Caching Mechanism

The investigation tool implements **TTL-based caching**.

### First request:

```text
[ASYNC] Monitoring sources collected
[CACHE STORE] investigation:payment-service
```

### Repeated request:

```text
[CACHE HIT] investigation:payment-service
```

This improves efficiency by avoiding redundant monitoring calls.

> Note: This is an application-level cache and is separate from CrewAI’s internal caching mechanisms.

---

# 6. Failure Policy (Retry + Fallback)

Each monitoring operation follows a defined failure strategy:

### Flow:

```text
Attempt → Retry → Success
                 ↓
              Failure
                 ↓
              Fallback
```

This ensures:

* Resilience against transient failures
* Graceful degradation instead of system crash
* Reliable tool execution

---

# 7. Asynchronous Execution Design

The system uses asynchronous execution for monitoring operations.

To avoid event-loop conflicts with CrewAI:

* Async logic is executed in a **separate thread**
* `asyncio.run()` is used safely within that thread

### Execution model:

```text
CrewAI Runtime
      |
      v
Custom Tool
      |
      v
Separate Thread
      |
      v
asyncio.gather()
```

This prevents nested event loop errors commonly seen in notebook environments.

---

# 8. Structured Incident Report

The final output is a Pydantic-based structured model:

### IncidentResolutionReport includes:

* Incident ID
* Incident type
* Severity
* Affected service
* Probable cause
* Evidence
* Immediate actions
* Recommended actions
* Long-term prevention
* Resolution confidence
* Unresolved information

This ensures deterministic, machine-readable incident output.

---
