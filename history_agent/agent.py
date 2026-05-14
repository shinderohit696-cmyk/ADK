from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent", # name of the agent
    model="gemini-2.5-flash-lite", # LLM provider
    description="Greeting agent", # description provided to agent
    instruction="""
    You are a helpful assistant that provide the Information on Indian history only. 
    provide indian history related answers only .
    if someone asks other than any history question then politely refuse.
    """,
)