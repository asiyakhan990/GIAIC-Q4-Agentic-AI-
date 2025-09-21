from agents import Agent, Runner, ModelSettings
from dotenv  import load_dotenv

load_dotenv()

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(
        # temperature=0.1,
        # top_p=0.0,
        # frequency_penalty=1.0,
        # presence_penalty=2.0,
        # truncation="auto"
    ),
    model="gpt-3.5-turbo"
)

# sentence = "how are you" * 17000

result = Runner.run_sync(
    agent,
    "Write a essay on pakistan in 17000 words"
)

print(result.final_output)