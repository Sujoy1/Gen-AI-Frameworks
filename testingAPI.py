from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)
response = client.embeddings.create(
    input="King had 2 queens",
    model="text-embedding-3-large"
)

print(response.data[0].embedding)