import asyncio
from agents import Agent, Runner

try:
    from ._shared import build_chat_model, get_gemini_client  # type: ignore
except ImportError:  # Running as a script from the examples directory
    from _shared import build_chat_model, get_gemini_client


async def main() -> None:
    client = get_gemini_client()
    agent = Agent(
        name="StreamingResultAgent",
        instructions="Roman Urdu me jawab do.",
        model=build_chat_model(client),
    )

    result = Runner.run_streamed(agent, input="Taareef-e-Ustaad pe 4 linein roman urdu me likho.")

    async for event in result.stream_events():
        if getattr(event, "type", None) == "raw_response_event":
            data = getattr(event, "data", None)
            delta = getattr(data, "delta", None)
            if isinstance(delta, str):
                print(delta, end="", flush=True)

    print("\n\nFinal Output:\n", result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
