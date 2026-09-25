# Her ziyaretci icin gecici iletisim oturumu olusturur.
# Iletisim bilgilerini sunucuda 30 dakika tutar.

import time

from app.contact_flow import new_contact_flow


SESSION_TIMEOUT = 30 * 60
contact_flows = {}


def get_contact_flow(session_id):
    now = time.time()

    # Suresi dolan oturumlari temizle.
    expired_ids = [
        current_id
        for current_id, entry in contact_flows.items()
        if now - entry["last_seen"] > SESSION_TIMEOUT
    ]

    for current_id in expired_ids:
        del contact_flows[current_id]

    if session_id not in contact_flows:
        contact_flows[session_id] = {
            "flow": new_contact_flow(),
            "last_seen": now,
        }

    contact_flows[session_id]["last_seen"] = now

    return contact_flows[session_id]["flow"]