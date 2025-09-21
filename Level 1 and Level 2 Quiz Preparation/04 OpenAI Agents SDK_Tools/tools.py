from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging
from dotenv import load_dotenv
import requests

load_dotenv()
enable_verbose_stdout_logging()

@function_tool(name_override="calculate_sum", description_override="Calculate the given numbers")
def add_numbers(a: int, b: int) -> str:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    """

    result = a + b
    return f"The sum of {a} and {b} is {result}"


agent = Agent(
    name="Assistant",
    instructions="You are helpful assistant",
    tools=[add_numbers]
)

result = Runner.run_sync(
    agent,
    "What is the current weather of Karachi?"
)

print(result.final_output)














# @function_tool
# def get_weather(city: str) -> str:
#     """
#     Get the weather for a given city

#     Args:
#         city : Given city name
#     """
#     try:
#         result = requests.get(
#             f"http://api.weatherapi.com/v1/current.json?key=8e3aca2b91dc4342a1162608252604&q={city}"
#         )

#         data = result.json()

#         return f"The current weather in {city} is {data["current"]["temp_c"]}C with {data["current"]["condition"]["text"]}."
    
#     except Exception as e :
#         return f"Could not fetch weather data due to {e}"