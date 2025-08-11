import asyncio
from agents import Runner

try:
    from ._shared import build_agent, get_gemini_client  # type: ignore
except ImportError:  # Running as a script from the examples directory
    from _shared import build_agent, get_gemini_client


async def main() -> None:
    client = get_gemini_client()
    agent = build_agent(
        name="Assistant",
        instructions="Tum ek helpful assistant ho. Roman Urdu me seedha, short jawab do.",
        client=client,
    )

    result = await Runner.run(agent, "Life ka matlab roman urdu me batao.")
    print("Final Output:\n", result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
