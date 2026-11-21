from pathlib import Path
import json
from urllib.parse import urlencode

from flask import Flask, render_template

ROOT = Path(__file__).resolve().parents[1]
app = Flask(
    __name__,
    template_folder=str(ROOT / "frontend" / "templates"),
    static_folder=str(ROOT / "frontend" / "static"),
)


@app.get("/")
def home():
    with (ROOT / "content" / "sitio.json").open(encoding="utf-8-sig") as file:
        site = json.load(file)

    contact = site["contacto"]
    query = urlencode({"text": contact["mensaje_whatsapp"]})
    whatsapp = f"https://wa.me/{contact['whatsapp']}?{query}"
    return render_template("index.html", site=site, whatsapp=whatsapp)
