from praisonaiagents import Agent, MCP
from dotenv import load_dotenv
load_dotenv()


single_tool_agent = Agent(
    instructions="You are a helpful assistant. Only call the tool if the user asks for it.",
    llm="gpt-4o-mini",
    tools=MCP("npx @openbnb/mcp-server-airbnb --ignore-robots-txt")
)

print("🔧 Agent initialized. You can now chat with it (type 'exit' to quit).")
print("--------------------------------------------------------------")

# Interactive loop
while True:
    try:
        user_input = input("🧑 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting chat.")
            break
        response = single_tool_agent.start(user_input)
        print(f"🤖 Agent: {response}\n")
    except KeyboardInterrupt:
        print("\n👋 Interrupted. Exiting chat.")
        break
    except Exception as e:
        print(f"⚠️ Error: {e}")