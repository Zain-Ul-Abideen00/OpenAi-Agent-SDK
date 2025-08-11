import asyncio
from agents import Agent, Runner
from agents.exceptions import AgentsException, MaxTurnsExceeded

try:
    from ._shared import build_chat_model, get_gemini_client  # type: ignore
except ImportError:  # Running as a script from the examples directory
    from _shared import build_chat_model, get_gemini_client


async def main() -> None:
    # Intentionally set a very low max_turns via RunConfig in a way that could raise
    client = get_gemini_client()
    agent = Agent(
        name="ErrorDemo",
        instructions=(
            "Roman Urdu me jawab do. Agar samajh na aaye to bar bar poochne ki koshish karo."
        ),
        model=build_chat_model(client),
    )

    try:
        # Using a trickier prompt may cause tool/handoff thoughts; we also bound max_turns
        result = await Runner.run(
            agent,
            input="Itna ambiguous prompt do ke agent confuse ho jaye.",
            run_config=None,
            max_turns=1,
        )
        print("Final Output:\n", result.final_output)
    except MaxTurnsExceeded as e:
        print("[ERROR] MaxTurnsExceeded:", str(e))
    except AgentsException as e:
        print("[ERROR] AgentsException:", str(e))
    except Exception as e:
        print("[ERROR] Unexpected:", str(e))


if __name__ == "__main__":
    asyncio.run(main())
