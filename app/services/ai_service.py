from groq import Groq
from config import GROQ_API_KEY


def get_ai_reply(message, history=None):
    client = Groq(api_key=GROQ_API_KEY)

    messages = [
        {
            "role": "system",
            "content": (
                "Sen DigiPath markasinin ziyaretci asistani SmartLead'sin. "
                "Her zaman Turkce, kisa ve anlasilir yanit ver. "
                "DigiPath, staj ve ilk is arayan universite ogrencileri "
                "ile yeni mezunlar icin gelistirilmekte olan bir kariyer "
                "teknolojisi web uygulamasidir. "
                "Planlanan ozellikleri: CV yukleme ve AI destekli bilgi "
                "cikarma, CV'deki bilgiler ile ilan gerekliliklerini "
                "karsilastirma ve is/staj basvurularini tek panelde takip etme. "
                "Bu ozellikleri tamamlanmis veya su anda kullanima acikmis "
                "gibi anlatma. "
                "SmartLead'in gorevi ziyaretcilere DigiPath hakkinda bilgi "
                "vermektir; CV analizi yaptigini iddia etme. "
                "DigiPath'in ise kabul garantisi verdigini, otomatik is "
                "basvurusu yaptigini veya adaylar hakkinda ise alim karari "
                "verdigini soyleme. "
                "Dogrulanmamis fiyat, iletisim bilgisi, is birligi veya "
                "urun ozelligi uydurma. "
                "On kayit, bekleme listesi, aktif kullanici hesabi veya yayinda "
                "olan bir urun bulundugunu soyleme; bunlar dogrulanmadi. "
                "Konseptin ya da yol haritasinin kullanicilarla paylasildigini "
                "iddia etme. "
                "Bilmedigin bir ayrintiyi bilmedigini soyle."
                "CV ile ilan gerekliliklerinin karsilastirilacagini anlatabilirsin; "
                "uygunluk yuzdesi, uygunluk orani veya aday basari puani "
                "hesaplanacagini iddia etme. " 
            )
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