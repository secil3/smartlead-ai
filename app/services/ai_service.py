from groq import Groq
from config import Config


class AIServiceError(Exception):
    """Yapay zeka servisi hatalarini temsil eder."""
    pass


class AIService:
    """Groq uzerinden yapay zeka yaniti uretir."""

    def yanit_uret(self, message, history=None):
        # API anahtari yoksa uygulama cokmeden demo yaniti verir.
        if not Config.GROQ_API_KEY:
            return "Demo modu: Yapay zeka servisi su anda kullanilamiyor."

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

        try:
            client = Groq(api_key=Config.GROQ_API_KEY)
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages
            )
            return response.choices[0].message.content

        except Exception as error:
            # Teknik hata ayrintisini ziyaretciye gostermiyoruz.
            raise AIServiceError(
                "Yapay zeka servisinden yanit alinamadi."
            ) from error


ai_service = AIService()


def get_ai_reply(message, history=None):
    # Mevcut /chat rotasi calismaya devam etsin.
    return ai_service.yanit_uret(message, history)