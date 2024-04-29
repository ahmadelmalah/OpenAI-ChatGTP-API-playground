from openai_client import client

audio_file = open("audio.mp3", "rb")
transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

print(transcription.text)
