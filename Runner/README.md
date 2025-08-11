## OpenAI Agents SDK Runner - Teaching Setup (English)

This folder contains a minimal teaching setup for the OpenAI Agents SDK (Python), configured to run with Google's Gemini models via an OpenAI-compatible endpoint. It includes Roman Urdu docs and runnable examples for each topic.

### Requirements

- Python 3.10+
- `uv` or `pip`
- An environment variable `GEMINI_API_KEY`

### Install

Using uv (recommended):

```bash
cd Runner
uv sync
```

Using pip:

```bash
cd Runner
python -m venv .venv
.venv\Scripts\activate  # on Windows
pip install -r requirements.txt  # fallback if you add a requirements.txt
pip install -e .
```

### Configure environment

Create a `.env` in `Runner/`:

```
GEMINI_API_KEY=your_key_here
```

Tracing is disabled in examples using `set_tracing_disabled(True)`.

### Run the basic demo

```bash
python Runner/main.py
```

### Run per-topic examples

- Async run: `python Runner/examples/01-Run.py`
- Sync run: `python Runner/examples/02-Run_sync.py`
- Streamed run: `python Runner/examples/03-Run_streamed.py`
- RunConfig: `python Runner/examples/04-RunConfig.py`
- RunHooks: `python Runner/examples/05-RunHooks.py`
- RunResult: `python Runner/examples/06-RunResult.py`
- RunResultStreaming: `python Runner/examples/07-RunResultStreaming.py`
- RunContextWrapper: `python Runner/examples/08-RunContextWrapper.py`
- RunErrorDetails (exceptions): `python Runner/examples/09-RunErrorDetails.py`

Refer to Roman Urdu docs in `Runner/Documentation/` for teaching notes and links.
