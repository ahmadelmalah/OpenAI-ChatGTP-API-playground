from openai_client import client

response = client.embeddings.create(
    input="hello world!", model="text-embedding-3-small"
)

print(response.data[0].embedding)
