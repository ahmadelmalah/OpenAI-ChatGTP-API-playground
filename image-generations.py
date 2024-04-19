# Initalization of the OpenAI API
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.environ.get("api_key"))

response = client.images.generate(
    prompt="a white siamese cat",
    size="1024x1024",
    n=1,
)

image_url = response.data[0].url
print(image_url)
