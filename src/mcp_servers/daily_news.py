import os
from mcp.server.fastmcp import FastMCP
from newsapi import NewsApiClient
from dotenv import load_dotenv
from typing import Optional
load_dotenv()

# Initialize MCP server
mcp = FastMCP("daily_news", host="127.0.0.1", port=8000)


# Init NewsAPI client
newsapi = NewsApiClient(api_key=os.getenv("NEWSAPI_KEY"))

@mcp.tool()
def get_top_headlines(
    query: str = None,
    country: Optional[str] = "us",
    category: Optional[str] = None,
    sources: Optional[str] = None,
):
    """
    Fetch top headlines from NewsAPI.
    Parameters:
        query (str): Keyword or phrase to search headlines for.
        country (str): 2-letter country code (default 'us').
                       Cannot be used together with `sources`.
        category (str): Category (business, entertainment, health, science, sports, technology).
        sources (str): Comma-separated list of source identifiers.
    Returns:
        List of headline dicts with title, description, url, source, and publishedAt.
    """
    try:
        articles = newsapi.get_top_headlines(
            q=query,
            country=country if not sources else None,  # can't use country + sources together
            category=category,
            sources=sources,
        )

        results = [
            {
                "title": a.get("title"),
                "description": a.get("description"),
                "url": a.get("url"),
                "source": a.get("source", {}).get("name"),
                "publishedAt": a.get("publishedAt"),
            }
            for a in articles.get("articles", [])
        ]
        return results[:10]  # return top 10 only
    except Exception as e:
        return {"error": str(e)}



if __name__ == "__main__":
    print("Starting daily_news MCP server on 127.0.0.1:8000 (Ctrl+C to stop)")
    mcp.run()

