# 💍 Multi-Wedding-Agents

A multi-agent wedding planning assistant built with **LangChain**. A main "Wedding Planner" agent takes your requirements and preferences, then delegates research tasks to two specialized sub-agents that search the web for relevant information (venues, vendors, ideas, etc.) — combining everything into tailored wedding planning recommendations.

## How it works

1. You're prompted in the terminal to describe your wedding requirements and preferences (budget, style, location, guest count, theme, etc.).
2. Your input is injected into the system prompt of a **main orchestrator agent** (`MainWeddingPlannerAgent`), which is told it has two expert sub-agents at its disposal.
3. The main agent has two tools available — `delegate_to_subagent1` and `delegate_to_subagent2` — each of which hands a query off to its own independent LangChain agent (`SubAgent1`, `SubAgent2`).
4. Each sub-agent is equipped with a `search_web` tool (backed by **Tavily**) and researches the web on the main agent's behalf, returning results back up the chain.
5. The main agent synthesizes everything into a final set of wedding planning recommendations, printed to the console.

This is a hierarchical / supervisor-style multi-agent architecture: one orchestrator agent reasons about what to look up and delegates the actual web research to subordinate agents rather than doing it all itself.

## Tech stack

| Layer | Technology |
|---|---|
| Agent framework | [LangChain](https://www.langchain.com/) (`create_agent`, multi-agent delegation via tool calling) |
| LLM inference | [Groq](https://groq.com/) (`openai/gpt-oss-20b`) via `langchain.chat_models.init_chat_model` |
| Web search tool | [Tavily](https://tavily.com/) search API |
| Config / secrets | `python-dotenv` |
| Language | Python 3.12+ |
| Dependency management | [uv](https://github.com/astral-sh/uv) |

## Project structure

```
multi-wedding-agents/
├── main.py         # Entry point — collects user input, runs the main orchestrator agent
├── agents.py        # Defines SubAgent1 & SubAgent2, and the delegate_to_subagentX tools
├── models.py        # Shared Groq chat model instance used by all agents
├── prompt.py        # System prompt (with requirements templating) and user prompt
├── tools.py         # Tavily-backed search_web tool used by the sub-agents
├── pyproject.toml   # Project metadata and dependencies
└── .env.example     # Required environment variables
```

## Getting started

### Prerequisites

- Python 3.12+
- A [Groq API key](https://console.groq.com/keys)
- A [Tavily API key](https://tavily.com/)

### Installation

```bash
git clone https://github.com/baakasta/multi-wedding-agents.git
cd multi-wedding-agents

# using uv (recommended, since the repo ships a uv.lock)
uv sync

# or with pip
pip install -e .
```

### Configuration

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### Usage

```bash
uv run main.py
# or: python main.py
```

You'll be prompted in the terminal:

```
Please enter your requirements and preferences for your wedding:
```

Type in details like budget, location, guest count, style/theme, etc. The main agent will delegate research to its sub-agents and print out tailored wedding planning recommendations.

