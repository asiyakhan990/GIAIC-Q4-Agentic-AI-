import datetime
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, function_tool
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(True)
gemini_ai_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_ai_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

@function_tool()
def get_time() -> str:
    """Get the current time"""

    print("get_time tool invoked")
    return f"Current time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"

@function_tool
def add_numbers(a: int, b: int) -> str:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    """
    print("add_number tool invoked")

    result = a + b

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=model,
    tools=[add_numbers, get_time],
    tool_use_behavior="stop_on_first_tool"
)

result = Runner.run_sync(
    agent,
    "What is the a current time and 2 + 5"
)

print(result.final_output)