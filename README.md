# SmartLead AI

SmartLead AI, DigiPath web sitesi için geliştirilen yapay zekâ destekli dijital asistandır.

Asistan, kullanıcıların DigiPath ve StudentJob hakkında sorularını yanıtlar. Kullanıcı iletişim talebi bırakmak istediğinde ad, e-posta ve mesaj bilgilerini adım adım toplar, kullanıcı onayından sonra veritabanına kaydeder.

## Özellikler

- DigiPath ve StudentJob hakkında yapay zekâ destekli soru-cevap
- İletişim talebi oluşturma
- Ad, e-posta ve mesaj bilgilerinin doğrulanması
- Kullanıcı onayından sonra iletişim talebinin kaydedilmesi
- Yönetici panelinden iletişim taleplerinin görüntülenmesi
- Wix üzerinden canlı chatbot kullanımı
- Render üzerinde yayınlanan Flask backend

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- Groq API
- Flask-CORS
- Gunicorn
- Wix HTML / JavaScript
- Render

## Proje Yapısı

```text
smartlead-ai/
├── run.py
├── config.py
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── routes.py
│   ├── pages.py
│   ├── contact_flow.py
│   ├── session_store.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── ai_service.py
│   └── templates/
│       ├── index.html
│       └── dashboard.html
└── .gitignore



## Mimari
Projede sorumluluklar ayrı modüllere bölünmüştür:
- routes.py: API isteklerini ve uygulama akışını yönetir.
- database.py: Veritabanı işlemlerini yönetir.
- ai_service.py: Groq API ile yapay zekâ iletişimini yönetir.
- contact_flow.py: İletişim talebi adımlarını yönetir.
- session_store.py: Ziyaretçilere ait geçici iletişim oturumlarını yönetir.
- pages.py: Ana sayfa ve yönetici paneli sayfalarını sunar.
- config.py: Ortam değişkenleri ve uygulama ayarlarını içerir.
## Kurulum
Projeyi klonladıktan sonra sanal ortam oluşturun:
python -m venv .venv

Sanal ortamı aktif edin:
source .venv/bin/activate

Gerekli paketleri yükleyin:
pip install -r requirements.txt

Proje kök dizininde .env dosyası oluşturun ve gerekli ortam değişkenlerini ekleyin:
GROQ_API_KEY=
FLASK_SECRET_KEY=
ADMIN_PASSWORD=

.env dosyası güvenlik nedeniyle GitHub deposuna dahil edilmez.
Çalıştırma
Projeyi yerel ortamda çalıştırmak için:
python run.py

Sağlık kontrolü:
http://127.0.0.1:5001/health

Başarılı durumda:
{"status":"ok"}

yanıtı alınır.
## API Endpointleri
- GET /health
  Backend servisinin çalışıp çalışmadığını kontrol eder.
- POST /api/sohbet
  SmartLead AI sohbet isteklerini işler.
- POST /api/leads
  İletişim talebi oluşturur.
- GET /api/leads
  Yönetici yetkilendirmesi ile iletişim taleplerini getirir.
- GET /dashboard
  Yönetici panelini görüntüler.
## Canlı Proje
Backend:
https://smartlead-ai-zkg4.onrender.com
DigiPath web sitesi:
https://secilkeser03.wixsite.com/digipath
Güvenlik
- API anahtarları ve gizli bilgiler .env dosyasında tutulur.
- .env dosyası .gitignore ile GitHub dışında tutulur.
- Yönetici kayıtlarına erişim parola kontrolü ile sınırlandırılmıştır.
- Kullanıcıdan alınan iletişim bilgileri onay sonrasında kaydedilir.
- CORS yapılandırması ile Wix ve backend arasındaki bağlantı sağlanır.

