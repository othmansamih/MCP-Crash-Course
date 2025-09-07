## MCP Crash Course

A minimal, working example of building and using MCP (Model Context Protocol) tools with agents. It includes:

- **MCP servers**: `daily_news` (NewsAPI) and `wikipedia_summary`
- **Agents**: single-tool agents (OpenAI and Ollama) and a multi-tool agent orchestrating both tools

### Project layout

```
src/
  mcp_servers/
    daily_news.py
    wikipedia_summary.py
  single_tool_agent_mcp_openai.py
  single_tool_agent_mcp_ollama.py
  multi_tools_agent_mcp_ollama.py
requirements.txt
```

### Requirements

- Python 3.10+
- Windows PowerShell (project examples use Windows paths)
- Optional LLM backends:
  - OpenAI (for `gpt-4o-mini` via `OPENAI_API_KEY`)
  - Ollama (for `ollama/llama3.2`; install from `https://ollama.com`)

Python deps (installed via `requirements.txt`):
- `mcp`, `mcp[cli]`
- `praisonaiagents`, `praisonaiagents[llm]`
- `newsapi-python`, `wikipedia`

### Environment variables

Create a `.env` file in the project root:

```
NEWSAPI_KEY=your_newsapi_key_here
OPENAI_API_KEY=your_openai_key_here            # required for the OpenAI agent
```

Get a NewsAPI key at `https://newsapi.org`. If you only use the Ollama agent, `OPENAI_API_KEY` is not required.

### Setup (Windows)

```
git clone https://github.com/othmansamih/MCP-Crash-Course
```

```
python -m venv .venv
.venv\Scripts\activate
```

```
pip install -r requirements.txt
```

If using Ollama:

1) Install from `https://ollama.com`
2) Pull the model: `ollama pull llama3.2`

### Run MCP servers directly (optional)

You can run the servers manually if you want to test them in isolation:

```
python src/mcp_servers/daily_news.py       # serves on 127.0.0.1:8000
python src/mcp_servers/wikipedia_summary.py# serves on 127.0.0.1:8001
```

If you use Claude Desktop, a sample config is shown in `claude_desktop_config.json` to auto-launch these servers with Claude Desktop

### Run the agents

Each script launches an interactive REPL. Type your prompt and press Enter. Type `exit` to quit.

- OpenAI + Airbnb MCP tool (via npx):

```
python src/single_tool_agent_mcp_openai.py
```

- Ollama + Daily News MCP tool:

```
python src/single_tool_agent_mcp_ollama.py
```

- Multi-tool agent (Ollama) using both `daily_news` and `wikipedia_summary`:

```
python src/multi_tools_agent_mcp_ollama.py
```

### What each server does

- `daily_news` (`127.0.0.1:8000`): exposes `get_top_headlines(query, country, category, sources)` using NewsAPI.
- `wikipedia_summary` (`127.0.0.1:8001`): exposes a Wikipedia summary tool.

The agents only call these tools when your instruction implies a need, e.g., “Fetch today’s top tech headlines in the US” or “Summarize Alan Turing from Wikipedia.”

### Example prompts

- "Show top technology headlines in the US."
- "Give me sports news in the UK."
- "Summarize 'Large language model' from Wikipedia."
- "Find news about NVIDIA earnings."


### Notes

- Agents use `praisonaiagents` to wire LLMs to MCP tools.
- The MCP servers are implemented with `FastMCP` from the `mcp` package.
