# Jozi Buddy 🎤

A local voice AI agent powered by Amazon Nova Sonic — your friendly Johannesburg-based chat companion.

---

## What it does

Jozi Buddy listens through your microphone and talks back through your speakers in real time. Ask it what to do in Joburg, have a casual chat, or just enjoy the company. It keeps its answers short and conversational, with a warm Mzansi flavour.

---

## How it works

- **[Strands Bidi Agents](https://strandsagents.com)** manages the bidirectional audio stream — audio flows in and out at the same time, and you can interrupt Jozi Buddy mid-sentence.
- **[Amazon Nova Sonic](https://aws.amazon.com/bedrock/)** (`amazon.nova-2-5-sonic` in `us-east-1`) is the speech-to-speech model that understands your voice and responds in kind.
- **Echo cancellation** (`AudioIO(audio_processor=True)`) stops the agent from hearing its own voice through your speakers and cutting itself off.

---

## Prerequisites

- Python 3.10 or later
- An AWS account with access to **Amazon Bedrock** in `us-east-1`
- **Nova Sonic model access enabled** in the Bedrock console (see setup step 5 below)
- **PortAudio** installed on your system (needed by PyAudio for microphone/speaker I/O):
  - **Windows:** install via vcpkg — `vcpkg install portaudio:x64-windows` — then copy `portaudio.dll` onto your PATH or into the pyaudio package folder
  - **macOS:** `brew install portaudio`
  - **Linux:** `sudo apt install portaudio19-dev`

---

## Setup

**1. Clone the repo**

```bash
git clone https://github.com/your-username/jozi-voice-buddy.git
cd jozi-voice-buddy
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
```

Windows (CMD):
```cmd
.venv\Scripts\activate
```

macOS / Linux:
```bash
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure AWS credentials**

```bash
aws configure
```

Enter your AWS Access Key ID, Secret Access Key, default region (`us-east-1`), and output format (`json`).

**5. Enable Nova Sonic model access in Bedrock**

1. Open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/) and make sure you're in the **US East (N. Virginia) / us-east-1** region.
2. In the left sidebar go to **Model access**.
3. Find **Amazon Nova Sonic** and request access (it's usually approved instantly).

---

## Run

```bash
python voice_agent.py
```

You'll see:

```
🎤  Jozi Buddy is listening — say something!
    Press Ctrl+C to end the conversation.
```

Start talking. Jozi Buddy will respond through your speakers. You can interrupt it at any time — just start speaking.

---

## End the conversation

Press **Ctrl+C**. You'll get a friendly sign-off:

```
👋  Sharp sharp — lekker chatting with you. Bye for now!
```

---

## Make it your own

The agent's personality lives in the `SYSTEM_PROMPT` constant near the top of `voice_agent.py`:

```python
SYSTEM_PROMPT = (
    "You are Jozi Buddy, a warm and laid-back voice companion based in "
    "Johannesburg, South Africa. ..."
)
```

Change it to anything you like. Some ideas:

- A Cape Town surf guide with beach recommendations
- A patient language tutor for isiZulu or Afrikaans
- A no-nonsense personal trainer that keeps you accountable
- A trivia host for South African history and pop culture

Keep responses short in the prompt (one or two sentences) — spoken answers that are too long feel unnatural.

---

## License

MIT
