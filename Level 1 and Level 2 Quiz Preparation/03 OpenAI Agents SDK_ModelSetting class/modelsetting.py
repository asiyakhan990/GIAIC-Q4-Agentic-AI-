from agents import Agent, Runner, ModelSettings
from dotenv  import load_dotenv

load_dotenv()

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(
        temperature=0.1,
        top_p=0.0,
        frequency_penalty=1.0,
        presence_penalty=2.0
    )
)

result = Runner.run_sync(
    agent,
    "Hello how are you?"
)

print(result.final_output)