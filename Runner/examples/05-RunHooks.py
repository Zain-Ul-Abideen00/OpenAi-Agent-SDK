import asyncio
from typing import Any
from agents import Agent, Runner, RunHooks

try:
    from ._shared import build_chat_model, get_gemini_client  # type: ignore
except ImportError:  # Running as a script from the examples directory
    from _shared import build_chat_model, get_gemini_client


class DemoRunHooks(RunHooks[Any]):
    async def on_agent_start(self, ctx, agent):  # type: ignore[override]
        print("[START] Agent run started:", agent.name)

    async def on_agent_end(self, ctx, agent, output):  # type: ignore[override]
        print("[END] Agent run finished. Final output length:", len(str(output)))

    async def on_tool_start(self, ctx, agent, tool):  # type: ignore[override]
        print(f"[TOOL-START] {tool.name} starting")

    async def on_tool_end(self, ctx, agent, tool, result: str):  # type: ignore[override]
        print(f"[TOOL-END] {tool.name} finished. Result preview:", (result or "").strip()[:60])


async def main() -> None:
    client = get_gemini_client()
    agent = Agent(
        name="HooksAgent",
        instructions="Roman Urdu me jawab do.",
        model=build_chat_model(client),
    )

    result = await Runner.run(
        agent,
        input="Email ka professional draft roman urdu me likho (short).",
        hooks=DemoRunHooks(),
    )
    print("\nFinal Output:\n", result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
