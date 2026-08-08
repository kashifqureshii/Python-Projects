# Personal Assistant

A simple Python voice assistant that can listen to commands and respond to them. It can open websites, play songs, and answer questions using an AI API.

## Features

- Voice commands
- Text to speech
- Speech recognition
- Opens websites
- Plays songs
- Can answer general questions

## Requirements

```bash
pip install SpeechRecognition pyttsx3 gTTS pygame openai PyAudio
```

## How to Run

```bash
python main.py
```

The assistant uses the wake word `Max`.

Some example commands:

```text
open Google
open YouTube
play a song
```

## Files

- `main.py` - main program
- `client.py` - OpenAI client
- `musicLibrary.py` - song links
- `README.md` - project information

## Note

An OpenAI API key is required for the question-answering part of the assistant. Do not upload your API key to GitHub.

