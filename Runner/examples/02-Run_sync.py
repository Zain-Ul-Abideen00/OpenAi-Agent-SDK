from agents import Runner

try:
    from ._shared import build_agent, get_gemini_client  # type: ignore
except ImportError:  # Running as a script from the examples directory
    from _shared import build_agent, get_gemini_client


def main() -> None:
    client = get_gemini_client()
    agent = build_agent(
        name="Assistant",
        instructions="Roman Urdu me simple jawab do.",
        client=client,
    )

    # Synchronous run
    result = Runner.run_sync(agent, "Ek chota sa motivational quote roman urdu me do.")
    print("Final Output:\n", result.final_output)


if __name__ == "__main__":
    main()
