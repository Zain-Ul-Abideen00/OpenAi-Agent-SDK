import asyncio
from agents import Agent, Runner

try:
    from ._shared import build_chat_model, get_gemini_client  # type: ignore
except ImportError:  # Running as a script from the examples directory
    from _shared import build_chat_model, get_gemini_client


async def main() -> None:
    client = get_gemini_client()
    agent = Agent(
        name="ResultAgent",
        instructions="Roman Urdu me jawab do.",
        model=build_chat_model(client),
    )

    result = await Runner.run(
        agent,
        "React vs Next.js ka mukhtasir muqabla roman urdu me batao.",
    )
    print("Final Output:\n", result.final_output)

    # Also show helper properties that are stable in SDK
    print("\nLast agent:", result.last_agent.name)
    print("Last response id:", result.last_response_id)
    print("Items count (new outputs/steps):", len(result.new_items))


if __name__ == "__main__":
    asyncio.run(main())
