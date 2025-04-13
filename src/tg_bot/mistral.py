import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")

async def mistral_get_content(content):
    model = "mistral-large-latest"

    client = Mistral(api_key=API_KEY)

    chat_response = await client.chat.complete_async(
        model= model,
        messages = [
            {
                "role": "user",
                "content": content,
            },
        ]
    )
    return chat_response.choices[0].message.content