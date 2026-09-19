from flask import Blueprint, jsonify, request
from app.services.ai_service import get_ai_reply, AIServiceError
from app.database import save_contact_request, get_contact_requests
import secrets
from config import ADMIN_PASSWORD

from app.contact_flow import (
    new_contact_flow,
    start_contact_flow,
    save_contact_name,
    save_contact_email,
    save_contact_message,
    handle_contact_confirmation,
)

from app.session_store import get_contact_flow


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "SmartLead AI calisiyor!"


@main.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@main.route("/api/leads", methods=["POST"])
@main.route("/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True) or {}

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not all(isinstance(value, str) and value.strip()
               for value in (name, email, message)):
            return jsonify({
                "basari": False,
                "error": "Ad, e-posta ve mesaj zorunludur."
                }), 400
        
    name = name.strip()
    email = email.strip()
    message = message.strip()

    if len(name) > 100 or len(email) > 254 or len(message) > 2000:
        return jsonify({
            "basari": False,
            "error": "Girilen bilgiler cok uzun."
        }), 400

    if "@" not in email or email.startswith("@") or email.endswith("@"):
        return jsonify({
            "basari": False,
            "error": "Gecerli bir e-posta adresi girin."
        }), 400

    request_id = save_contact_request(name, email, message)

    return jsonify({
        "basari": True,
        "message": "Iletisim talebiniz kaydedildi.",
        "request_id": request_id
    }), 201
    
    
@main.route("/api/leads", methods=["GET"])
@main.route("/admin/contacts", methods=["GET"])
def admin_contacts():
    provided_password = request.headers.get("X-Admin-Password", "")

    if not ADMIN_PASSWORD or not secrets.compare_digest(
        provided_password, ADMIN_PASSWORD
    ):
        return jsonify({"error": "Yetkisiz erisim."}), 401

    return jsonify({
    "basari": True,
    "contacts": get_contact_requests()
    })




@main.route("/api/sohbet", methods=["POST"])
@main.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}

    if not isinstance(data, dict):
            return jsonify({
            "basari": False,
            "error": "Gecersiz istek."
            }), 400

    message = data.get("message", "")
    history = data.get("history", [])
    flow = get_contact_flow()

    if not isinstance(message, str) or not message.strip():
        return jsonify({
        "basari": False,
        "error": "Lutfen bir mesaj girin."
        }), 400

    if not isinstance(history, list) or len(history) > 20:
        return jsonify({
        "basari": False,
        "error": "Gecersiz sohbet gecmisi."
        }), 400

    for item in history:
        if (
            not isinstance(item, dict)
            or item.get("role") not in ("user", "assistant")
            or not isinstance(item.get("content"), str)
            or not item["content"].strip()
            or len(item["content"]) > 2000
        ):
            return jsonify({
            "basari": False,
            "error": "Gecersiz sohbet gecmisi."
            }), 400


    message = message.strip()
    step = flow["step"]

    if step == "name":
        reply = save_contact_name(flow, message)
    elif step == "email":
        reply = save_contact_email(flow, message)
    elif step == "message":
        reply = save_contact_message(flow, message)
    elif step == "confirm":
        reply = handle_contact_confirmation(flow, message)

        if flow["step"] == "approved":
            request_id = save_contact_request(
            flow["name"],
            flow["email"],
            flow["message"],
            )

            flow.clear()
            flow.update(new_contact_flow())

            reply = (
            f"Iletisim talebiniz kaydedildi. "
            f"Talep numaraniz: {request_id}"
            )
    elif step == "approved":
        reply = "Onayiniz alindi. Kayit islemi henuz baglanmadi."
    elif message.lower() in (
        "iletisim talebi",
        "iletisim kurmak istiyorum",
        "benimle iletisime gecin",
    ):
        reply = start_contact_flow(flow)
    else:
        try:
            reply = get_ai_reply(message, history)
        except AIServiceError:
            return jsonify({
                "basari": False,
                "error": "Yapay zeka servisi su anda kullanilamiyor."
            }), 503
            
        return jsonify({
        "basari": True,
        "reply": reply,
        "contact_flow": {"step": flow["step"]}
        })
    
    
