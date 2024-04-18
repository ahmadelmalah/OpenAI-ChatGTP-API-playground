# Initalization of the OpenAI API
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.environ.get("api_key"))

scenario_one_worded_reponses = [
    {
        "role": "system",
        "content": "You're an assistant that responds with one word",
    },
    {"role": "user", "content": "What's the capital of Egypt?"},
]

scenario_ice_cream_media = [
    {
        "role": "system",
        "content": "You are an assistant that creates short one-line responses to comments that users have left on your ice cream shop's Google reviews page",
    },
    {
        "role": "user",
        "content": "Comments: Great experience - I love the vanilla flavor!",
    },
    {
        "role": "assistant",
        "content": "Hello Ice Cream Fan, thank you so much. Vanilla is our favorite too. SCREAM FOR ICE CREAM!",
    },
    {
        "role": "user",
        "content": "Comments: I liked the many different flavors they have, and there's no line!",
    },
    {
        "role": "assistant",
        "content": "Hello Ice Cream Fan, thanks for that - we have over 50 different flavors. SCREAM FOR ICE CREAM!",
    },
    {
        "role": "user",
        "content": "Comments: The customer service was great - they were all so helpful!",
    },
    {
        "role": "assistant",
        "content": "Hello Ice Cream Fan, much appreciated. So glad we were helpful. SCREAM FOR ICE CREAM!",
    },
    {"role": "user", "content": "Comments: great location and great staff"},
]

scenario_worldcup = [
    {
        "role": "system",
        "content": "You're an assistant that responds to questions about the World Cup 2026",
    },
    {"role": "user", "content": "When and where is it?"},
]


# Creating the completion and printing the response
completion = client.chat.completions.create(
    model="gpt-3.5-turbo", messages=scenario_worldcup
)
print(completion.choices[0].message.content)
