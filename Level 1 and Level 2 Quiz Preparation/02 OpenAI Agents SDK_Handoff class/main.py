from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from agents import set_tracing_disabled, enable_verbose_stdout_logging
from dotenv import load_dotenv
import os

load_dotenv()
enable_verbose_stdout_logging()
set_tracing_disabled(True)

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

python_agent = Agent(
    name="PythonAgent",
    instructions="You are a Python code execution agent.",
    handoff_description="Handles Python-related code execution.",
    model=model
)

triage_agent = Agent(
    name="Assistant",
    instructions="""If the user query is about Python, You must always call the tool transfer_to_python_agent.
    Do not answer Python queries yourself""",
    handoffs=[python_agent],
    model=model
)

result = Runner.run_sync(
    triage_agent,
    "What is Python response in 2 lines"
)

print(result.final_output)