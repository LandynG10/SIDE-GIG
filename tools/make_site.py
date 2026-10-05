#!/usr/bin/env python3
"""Build a one-page local-business website from a JSON config.

    python3 tools/make_site.py sites/configs/example-plumber.json
    -> sites/out/<slug>/index.html

Standard library only. The output is a single static file you can upload to
Netlify, Cloudflare Pages or GitHub Pages as-is.
"""
import datetime
import html
import json
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "sites" / "_template" / "index.html"
OUT = ROOT / "sites" / "out"

REQUIRED = ["name", "city", "phone", "tagline", "services"]


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def esc(value):
    return html.escape(str(value), quote=True)


def build(cfg):
    missing = [k for k in REQUIRED if not cfg.get(k)]
    if missing:
        raise SystemExit(f"config is missing: {', '.join(missing)}")

    services = "".join(
        f'<div class="card"><h3>{esc(s["title"])}</h3><p>{esc(s.get("text", ""))}</p></div>'
        for s in cfg["services"]
    )
    # Only real reviews copied from the business's Google/Yelp page. Never invent them.
    reviews = "".join(
        '<blockquote class="card review"><div class="stars">★★★★★</div>'
        f'<p>{esc(r["text"])}</p><cite>{esc(r["author"])}</cite></blockquote>'
        for r in cfg.get("reviews", [])
    ) or '<div class="card"><p>Reviews coming soon.</p></div>'
    badges = "".join(f"<span>{esc(b)}</span>" for b in cfg.get("badges", []))

    address = cfg.get("address", cfg["city"])
    values = {
        "name": esc(cfg["name"]),
        "city": esc(cfg["city"]),
        "tagline": esc(cfg["tagline"]),
        "phone": esc(cfg["phone"]),
        "phone_link": re.sub(r"[^0-9+]", "", cfg["phone"]),
        "headline": esc(cfg.get("headline", f'{cfg["tagline"]} in {cfg["city"]}')),
        "subheadline": esc(cfg.get("subheadline", "Fast, friendly, fairly priced. Call today.")),
        "color": cfg.get("color", "#1f6feb") if re.fullmatch(r"#[0-9a-fA-F]{6}", cfg.get("color", "")) else "#1f6feb",
        "address": esc(address),
        "hours": esc(cfg.get("hours", "Call for hours")),
        "service_area": esc(cfg.get("service_area", cfg["city"] + " and nearby")),
        "map_query": urllib.parse.quote_plus(f'{cfg["name"]} {address}'),
        "year": str(datetime.date.today().year),
        "services": services,
        "reviews": reviews,
        "badges": badges,
    }
    page = TEMPLATE.read_text()
    for key, val in values.items():
        page = page.replace("{{" + key + "}}", val)
    leftover = re.findall(r"\{\{(\w+)\}\}", page)
    if leftover:
        raise SystemExit(f"template placeholders not filled: {sorted(set(leftover))}")
    return page


def main(argv):
    if len(argv) != 2:
        raise SystemExit(__doc__)
    cfg = json.loads(Path(argv[1]).read_text())
    slug = cfg.get("slug") or slugify(cfg["name"])
    dest = OUT / slug
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "index.html").write_text(build(cfg))
    print(dest / "index.html")


if __name__ == "__main__":
    main(sys.argv)
