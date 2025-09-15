from agents import Agent, Runner
# , set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()
# set_tracing_disabled(True)

agent = Agent(
    name="Assistant",
    instructions="you are helpful assistant",
)

result = Runner.run_sync(
    agent,
    "Hello"
)

print(result.final_output)