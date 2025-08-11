## OpenAI Agents SDK - Teaching Repository

This repository contains a simple Runner project demonstrating the OpenAI Agents SDK with Roman Urdu documentation and runnable examples for classroom teaching.

### Structure

- `Runner/main.py`: Minimal async agent example using Gemini via OpenAI-compatible client
- `Runner/Documentation/`: Roman Urdu docs per topic (Runner, RunConfig, Hooks, Results, etc.)
- `Runner/examples/`: One Python script per documentation topic to test locally

### Prerequisites

- Python 3.10+
- A Gemini API key set as environment variable `GEMINI_API_KEY`

### Setup

```bash
cd Runner
uv sync  # or create venv + pip install
```

Create `Runner/.env` with:

```
GEMINI_API_KEY=your_key_here
```

### Run

- Quick demo: `python Runner/main.py`
- Topic examples: see `Runner/README.md` for the full list

Docs are written in Roman Urdu for easy teaching; READMEs are in English.
