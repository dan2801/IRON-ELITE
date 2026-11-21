from flask import url_for

from backend.app import ROOT, app, home


def pages_url_for(endpoint, **values):
    if endpoint == "static":
        return "frontend/static/" + values["filename"]
    return url_for(endpoint, **values)


if __name__ == "__main__":
    with app.test_request_context("/"):
        app.jinja_env.globals["url_for"] = pages_url_for
        html = "\n".join(line.rstrip() for line in home().splitlines())
        (ROOT / "index.html").write_text(html + "\n", encoding="utf-8")
