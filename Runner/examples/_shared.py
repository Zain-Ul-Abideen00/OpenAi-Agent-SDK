import os
from typing import Optional

from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, set_tracing_disabled, enable_verbose_stdout_logging

enable_verbose_stdout_logging()


def get_gemini_client() -> AsyncOpenAI:
    """Initialize and return an AsyncOpenAI client for Gemini-compatible endpoint.

    Requires GEMINI_API_KEY in environment or .env.
    Disables tracing by default for classroom demos.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")

    base_url = os.getenv("GEMINI_BASE_URL")

    client = AsyncOpenAI(api_key=api_key, base_url=base_url)
    set_tracing_disabled(True)
    return client


def build_chat_model(client: AsyncOpenAI, model_name: str = "gemini-2.0-flash") -> OpenAIChatCompletionsModel:
    """Create an OpenAIChatCompletionsModel bound to provided client and model name."""
    return OpenAIChatCompletionsModel(openai_client=client, model=model_name)


def build_agent(
    name: str = "Assistant",
    instructions: str = "Tum ek helpful assistant ho. Roman Urdu me jawab do.",
    *,
    client: Optional[AsyncOpenAI] = None,
    model_name: str = "gemini-2.0-flash",
) -> Agent:
    """Convenience factory for a basic Agent with given name/instructions."""
    _client = client or get_gemini_client()
    return Agent(
        name=name,
        instructions=instructions,
        model=build_chat_model(_client, model_name=model_name),
    )
