import asyncio
from dataclasses import dataclass
from agents import Agent, Runner, function_tool, RunContextWrapper

try:
    from ._shared import build_chat_model, get_gemini_client  # type: ignore
except ImportError:  # Running as a script from the examples directory
    from _shared import build_chat_model, get_gemini_client


@dataclass
class UserInfo:
    name: str
    uid: int


@function_tool
async def fetch_user_name(ctx: RunContextWrapper[UserInfo]) -> str:
    return f"User ka naam: {ctx.context.name} (id={ctx.context.uid})"


async def main() -> None:
    client = get_gemini_client()
    agent = Agent[UserInfo](
        name="ContextAgent",
        instructions=(
            "Roman Urdu me jawab do. Agar zarurat ho to `fetch_user_name` tool use karo."
        ),
        model=build_chat_model(client),
        tools=[fetch_user_name],
    )

    user = UserInfo(name="Ali", uid=123)

    result = await Runner.run(
        agent,
        input="Mera naam kya hai? roman urdu me batao",
        context=user,
    )

    print("Final Output:\n", result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
