import truststore
truststore.inject_into_ssl()

from google import genai
from config import Config

Config.validate()

client = genai.Client(api_key=Config.GEMINI_API_KEY)

def generate_chat_response(prompt: str):
    try:
        response = client.models.generate_content(
            model=Config.MODEL_NAME,
            contents=prompt,
        )
        return response.text
    except Exception as e:
        print(e)
        raise