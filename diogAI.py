# Usando API do Gemini
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

prompt = input("Pergunte alguma coisa: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)