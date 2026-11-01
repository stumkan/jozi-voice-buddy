"""
Jozi Buddy — a friendly Johannesburg-based voice companion.

Runs on your laptop using the microphone and speakers.
Press Ctrl+C to end the conversation.

Requirements
------------
pip install "strands-agents[bidi-all,bidi-pyaudio]" boto3

PortAudio must also be installed on your OS (needed by PyAudio):
  macOS : brew install portaudio
  Linux : sudo apt install portaudio19-dev
  Windows: usually bundled with the PyAudio wheel — no extra step needed.

AWS credentials must be configured (aws configure / environment variables)
with access to Amazon Bedrock in us-east-1.
"""

import asyncio
import signal
import boto3

from strands.bidi.agent import BidiAgent
from strands.bidi.io import AudioIO
from strands.bidi.models import BedrockNovaSonicModel

# ── Model configuration ───────────────────────────────────────────────────────
MODEL_ID = "amazon.nova-2-5-sonic"
AWS_REGION = "us-east-1"

# ── Jozi Buddy's personality ──────────────────────────────────────────────────
SYSTEM_PROMPT = (
    "You are Jozi Buddy, a warm and laid-back voice companion based in "
    "Johannesburg, South Africa. You chat casually, sprinkle in a bit of "
    "local flavour (think 'lekker', 'sharp', 'eish'), and love recommending "
    "things to do, eat, and see in Joburg and around Mzansi. "
    "Keep every spoken reply to one or two sentences — short and natural."
)


async def main() -> None:
    # Pin the AWS region explicitly so the agent always hits us-east-1
    # regardless of the user's default profile or AWS_DEFAULT_REGION env var.
    session = boto3.Session(region_name=AWS_REGION)

    model = BedrockNovaSonicModel(
        model_id=MODEL_ID,
        boto_session=session,
        voice="tiffany",   # If you remove this line, the voice will be of a male.
    )

    agent = BidiAgent(
        model=model,
        system_prompt=SYSTEM_PROMPT,
    )

    # AudioIO with audio_processor=True enables WebRTC echo cancellation,
    # noise suppression, and automatic gain control.  This stops the agent
    # from hearing its own voice through the open speakers and cutting itself
    # off mid-sentence.
    audio = AudioIO(audio_processor=True)

    print()
    print("🎤  Jozi Buddy is listening — say something!")
    print("    Press Ctrl+C to end the conversation.\n")

    try:
        # agent.run() streams audio in both directions until cancelled.
        await agent.run(
            inputs=[audio.input()],
            outputs=[audio.output()],
        )
    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    finally:
        print("\n👋  Sharp sharp — lekker chatting with you. Bye for now!")


if __name__ == "__main__":
    # Handle Ctrl+C cleanly on all platforms.
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋  Sharp sharp — lekker chatting with you. Bye for now!")
