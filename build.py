#!/usr/bin/env python3
"""Build index.html from data/*.json and site/template.html.

Usage: python3 build.py
The page is static. Data is inlined so it opens from disk, from GitHub Pages,
or anywhere else without a server.
"""
import datetime
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
NAMES = ["people", "sources", "hypotheses", "batches", "folders", "documents",
         "curiosities", "candidates", "families", "priors", "leads", "requests", "role"]


def main():
    data = {n: json.loads((ROOT / "data" / f"{n}.json").read_text(encoding="utf-8")) for n in NAMES}
    data["built"] = datetime.date.today().isoformat()

    known = {h["id"] for h in data["hypotheses"]}
    for b in data["batches"]:
        for hid in b["raised"] + b["resolved"]:
            if hid not in known:
                raise SystemExit(f"{b['id']} refers to unknown hypothesis {hid}")
    for d in data["documents"]:
        if not (ROOT / "assets" / "pages" / d["folder"] / d["file"]).exists():
            raise SystemExit(f"{d['id']}: missing web image for {d['file']}")

    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    template = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
    marker = "/*__DATA__*/{}"
    if marker not in template:
        raise SystemExit("template is missing the data marker")
    (ROOT / "index.html").write_text(template.replace(marker, payload), encoding="utf-8")
    print(f"index.html built: {len(data['batches'])} batches, {len(data['documents'])} documents, "
          f"{len(data['hypotheses'])} hypotheses")


if __name__ == "__main__":
    main()
