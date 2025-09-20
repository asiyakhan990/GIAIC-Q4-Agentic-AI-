import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(True)

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

# config = RunConfig(
#     model=model,
#     model_provider=client,
#     tracing_disabled=True
# )

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=model
)

result = Runner.run_sync(
    agent,
    "What is python in 2 lines"
)

print(result.final_output)