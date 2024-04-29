from openai_client import client

response = client.images.generate(
    prompt="a white siamese cat",
    size="1024x1024",
    n=1,
)

image_url = response.data[0].url
print(image_url)
