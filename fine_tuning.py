from openai_client import client

file = client.files.create(
    file=open("fine_tuning_data.jsonl", "rb"), purpose="fine-tune"
)

client.fine_tuning.jobs.create(training_file=file.id, model="gpt-3.5-turbo")
