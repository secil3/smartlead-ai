
# Her ziyaretci icin gecici iletisim oturumu olusturur.
# Iletisim bilgilerini cerez yerine sunucuda 30 dakika tutar.

import secrets
import time

from flask import session

from app.contact_flow import new_contact_flow


SESSION_TIMEOUT = 30 * 60
contact_flows = {}


def get_contact_flow():
    now = time.time()

    # Suresi dolan oturumlari temizle.
    expired_ids = [
        session_id
        for session_id, entry in contact_flows.items()
        if now - entry["last_seen"] > SESSION_TIMEOUT
    ]

    for session_id in expired_ids:
        del contact_flows[session_id]

    session_id = session.get("contact_session_id")

    if not session_id or session_id not in contact_flows:
        session_id = secrets.token_urlsafe(32)
        session["contact_session_id"] = session_id

        contact_flows[session_id] = {
            "flow": new_contact_flow(),
            "last_seen": now,
        }

    contact_flows[session_id]["last_seen"] = now

    return contact_flows[session_id]["flow"]