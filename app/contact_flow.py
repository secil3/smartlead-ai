
# Iletisim talebinin ad, e-posta, mesaj ve onay adimlarini yonetir.
# Bilgileri gecici olarak tutar; tek basina veritabanina kaydetmez.


import re

def new_contact_flow():
    return {
        "step": "idle",
        "name": "",
        "email": "",
        "message": ""
    }
    
def start_contact_flow(flow):
    flow["step"] = "name"
    return "Iletisim talebinizi olusturalim. Adinizi yazar misiniz?"


def save_contact_name(flow, name):
    name = name.strip()

    if not name or len(name) > 100:
        return "Lutfen 1-100 karakter arasinda bir ad girin."

    flow["name"] = name
    flow["step"] = "email"

    return "Tesekkurler. E-posta adresinizi yazar misiniz?"


def save_contact_email(flow, email):
    email = email.strip()

    if (
        len(email) > 254
        or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email)
    ):
        return "Lutfen gecerli bir e-posta adresi girin."

    flow["email"] = email
    flow["step"] = "message"

    return "Tesekkurler. Iletmek istediginiz mesaji yazar misiniz?"


def save_contact_message(flow, message):
    message = message.strip()

    if not message or len(message) > 2000:
        return "Lutfen 1-2000 karakter arasinda bir mesaj girin."

    flow["message"] = message
    flow["step"] = "confirm"

    return (
        "Iletisim talebinizi kaydetmeden once onayinizi istiyorum.\n"
        f"Ad: {flow['name']}\n"
        f"E-posta: {flow['email']}\n"
        f"Mesaj: {flow['message']}\n"
        "Bu bilgilerin iletisim talebiniz icin kaydedilmesini "
        "onayliyor musunuz? Lutfen 'evet' veya 'hayir' yazin."
    )
    

def handle_contact_confirmation(flow, answer):
    answer = answer.strip().lower()

    if answer == "hayır" or answer == "hayir":
        flow.clear()
        flow.update(new_contact_flow())
        return "Iletisim talebiniz iptal edildi. Bilgileriniz kaydedilmedi."

    if answer == "evet":
        flow["step"] = "approved"
        return "Onayiniz alindi."

    return "Lutfen 'evet' veya 'hayir' yazarak yanit verin."


