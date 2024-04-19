# Initalization of the OpenAI API
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.environ.get("api_key"))

audio_file = open("audio.mp3", "rb")
transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

print(transcription.text)
