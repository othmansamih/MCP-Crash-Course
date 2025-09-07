# wikipedia_summary.py
import asyncio
from mcp.server.fastmcp import FastMCP
import wikipedia

# Initialize MCP server
mcp = FastMCP("wikipedia_summary", host="127.0.0.1", port=8001)

@mcp.tool()
def get_wikipedia_summary(query: str, sentences: int = 3, lang: str = "en"):
    """
    Fetch a summary of a topic from Wikipedia.

    Parameters:
        query (str): The topic or article title to search for on Wikipedia.
        sentences (int): Number of sentences to return in the summary (default: 3).
        lang (str): Language code for Wikipedia (default: 'en').

    Returns:
        dict: {
            "title": str,
            "summary": str,
            "url": str
        }
    """
    try:
        wikipedia.set_lang(lang)
        summary = wikipedia.summary(query, sentences=sentences)
        page = wikipedia.page(query)
        return {
            "title": page.title,
            "summary": summary,
            "url": page.url,
        }
    except wikipedia.DisambiguationError as e:
        return {
            "error": "DisambiguationError",
            "message": f"Your query '{query}' may refer to multiple topics.",
            "options": e.options[:10],  # show a few options
        }
    except wikipedia.PageError:
        return {"error": "PageError", "message": f"No page found for '{query}'."}
    except Exception as e:
        return {"error": "Exception", "message": str(e)}

if __name__ == "__main__":
    print("Starting wikipedia_summary MCP server on 127.0.0.1:8001 (Ctrl+C to stop)")
    mcp.run()
