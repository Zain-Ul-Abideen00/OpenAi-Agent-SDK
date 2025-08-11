import os
import asyncio
from agents import Agent, Runner

try:
    from ._shared import build_chat_model, get_gemini_client  # type: ignore
except ImportError:  # Running as a script from the examples directory
    from _shared import build_chat_model, get_gemini_client

# used this block of code from the examples to print the response slowly
STREAM_DELAY_S = float(os.getenv("STREAM_DELAY_S", "0.03"))
STREAM_CHARS_PER_STEP = int(os.getenv("STREAM_CHARS_PER_STEP", "2"))


async def print_slowly(text: str, *, delay_s: float = STREAM_DELAY_S, step_chars: int = STREAM_CHARS_PER_STEP) -> None:
    if step_chars <= 0:
        step_chars = 1
    for i in range(0, len(text), step_chars):
        chunk = text[i : i + step_chars]
        print(chunk, end="", flush=True)
        await asyncio.sleep(delay_s)


async def main() -> None:
    client = get_gemini_client()
    agent = Agent(
        name="Streamer",
        instructions="Roman Urdu me likho. Lambi cheez ko hisso me bhejo takay live feel aaye.",
        model=build_chat_model(client),
    )

    # Start a streamed run
    streamed = Runner.run_streamed(agent, input="Stars pe ek choti nazm roman urdu me likho.")

    print("=== Streaming start ===")
    async for event in streamed.stream_events():
        # Only print text deltas; ignore other event types for simplicity
        if getattr(event, "type", None) == "raw_response_event":
            data = getattr(event, "data", None)
            # ResponseTextDeltaEvent is OpenAI Responses type; guard for providers
            delta = getattr(data, "delta", None)
            if isinstance(delta, str):
                await print_slowly(delta)

    print("\n=== Streaming complete ===")


if __name__ == "__main__":
    asyncio.run(main())
