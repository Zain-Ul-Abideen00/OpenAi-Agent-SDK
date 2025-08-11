import asyncio
from agents import Agent, Runner, RunConfig

try:
    from ._shared import build_chat_model, get_gemini_client  # type: ignore
except ImportError:  # Running as a script from the examples directory
    from _shared import build_chat_model, get_gemini_client


async def main() -> None:
    client = get_gemini_client()
    agent = Agent(
        name="ConfigDemo",
        instructions="Roman Urdu me jawab do.",
        model=build_chat_model(client),
    )

    config = RunConfig(
        workflow_name="demo_run_config",
        tracing_disabled=True,
    )

    result = await Runner.run(
        agent,
        input="Travel guide: Karachi me 1 din ka simple plan roman urdu me banao.",
        run_config=config,
        max_turns=3,
    )
    print("Final Output:\n", result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
