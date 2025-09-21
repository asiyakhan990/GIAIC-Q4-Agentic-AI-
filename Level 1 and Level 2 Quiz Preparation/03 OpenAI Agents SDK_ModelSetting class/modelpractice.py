from agents import Agent, Runner, ModelSettings
from openai.types import Reasoning
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
        # truncation="auto",
        # max_tokens=25,
        # reasoning=Reasoning(
        #     # effort=["medium"]
        #     summary=["concise"]
        # )
        # metadata={
        #     "live": "session-4"
        # }
        # store=True,
        include_usage=False
    ),
    # model="gpt-3.5-turbo"
    model="gpt-5",
    
)

# sentence = "how are you" * 17000

result = Runner.run_sync(
    agent,
    # "Write a essay on pakistan in 17000 words"
    "What is Python"
)

print(result.final_output)