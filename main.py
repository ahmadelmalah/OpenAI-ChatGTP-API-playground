from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(api_key=os.environ.get('api_key'))

# Making the request
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Just respond with one word"},
    {"role": "user", "content": "What's the capital of Egypt?"},
  ]
)

print(completion.choices[0].message.content)