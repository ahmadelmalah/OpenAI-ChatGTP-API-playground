# Initalization of the OpenAI API
from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv()
client = OpenAI(api_key=os.environ.get("api_key"))

speech_file_path = "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Today is a wonderful day to build something people love!",
)

response.stream_to_file(speech_file_path)
