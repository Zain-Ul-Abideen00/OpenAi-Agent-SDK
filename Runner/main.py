import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # Gemini API base URL
)

set_tracing_disabled(disabled=True)  # Disable tracing for cleaner output

async def main():
    agent = Agent(
        name = "Assistant",
        instructions= "You are a helpful assistant. Answer questions to the best of your ability. You can answer in english, urdu or roman urdu.",
        model = OpenAIChatCompletionsModel(
            openai_client=client,
            model="gemini-2.0-flash",  # Specify the Gemini model
        )
    )
    result = await Runner.run(
        agent,
        "What is the meaning of life? answer in roman urdu"  # Example question
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
