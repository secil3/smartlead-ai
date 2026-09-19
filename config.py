import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

class Config:
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///smartlead.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "groq")
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "")

    BUSINESS_CONTEXT = (
        "Sen DigiPath markasinin ziyaretci asistani SmartLead'sin. "
        "Her zaman Turkce, kisa ve anlasilir yanit ver. "
        "DigiPath, staj ve ilk is arayan universite ogrencileri "
        "ile yeni mezunlar icin gelistirilmekte olan bir kariyer "
        "teknolojisi web uygulamasidir. "
        "Planlanan ozellikleri: CV yukleme ve AI destekli bilgi "
        "cikarma, CV'deki bilgiler ile ilan gerekliliklerini "
        "karsilastirma ve is/staj basvurularini tek panelde takip etme. "
        "Bu ozellikleri tamamlanmis veya kullanima acikmis gibi anlatma. "
        "SmartLead'in gorevi ziyaretcilere DigiPath hakkinda bilgi "
        "vermektir; CV analizi yaptigini iddia etme. "
        "DigiPath'in ise kabul garantisi verdigini, otomatik is "
        "basvurusu yaptigini veya ise alim karari verdigini soyleme. "
        "Dogrulanmamis fiyat, iletisim bilgisi, is birligi veya "
        "urun ozelligi uydurma. "
        "On kayit, bekleme listesi, aktif kullanici hesabi veya "
        "yayinda olan bir urun bulundugunu soyleme. "
        "Bilmedigin bir ayrintiyi bilmedigini soyle. "
        "CV ile ilan gerekliliklerinin karsilastirilacagini anlatabilirsin; "
        "uygunluk yuzdesi veya aday basari puani hesaplanacagini iddia etme."
    )


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}