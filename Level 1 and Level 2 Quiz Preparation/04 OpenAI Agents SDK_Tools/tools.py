from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Assistant",
    instructions="You are helpful assistant"
)

result = Runner.run_sync(
    agent,
    "Hello"
)

print(result.final_output)