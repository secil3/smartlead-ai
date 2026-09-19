from groq import Groq
from config import Config


def get_ai_reply(message, history=None):
    client = Groq(api_key=Config.GROQ_API_KEY)

    messages = [
        {
            "role": "system",
            "content": Config.BUSINESS_CONTEXT
        }
    ]

    if history:
        messages.extend(history)

    messages.append({
        "role": "user",
        "content": message
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    return response.choices[0].message.content