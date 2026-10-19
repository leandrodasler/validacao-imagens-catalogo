#!/usr/bin/env python3
"""
Baixa para images/ as imagens do catalog.json que ainda não existem em disco.

Uso:
  python3 download_images.py              # baixa só o que falta
  python3 download_images.py --force      # baixa tudo de novo (sobrescreve)
  python3 download_images.py --dry-run    # só lista o que seria baixado

O arquivo é nomeado pela categoria (images/img_<categoria>.<ext>), com a extensão
detectada pelo Content-Type. Ao final, o campo "image" do catalog.json é atualizado.
"""

import argparse
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
CATALOG = ROOT / "catalog.json"
IMAGES_DIR = ROOT / "images"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
EXTENSIONS = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
}


def download(url, categoria):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as response:
        content_type = response.headers.get_content_type()
        ext = EXTENSIONS.get(content_type)
        if ext is None:
            raise ValueError(f"tipo inesperado: {content_type}")
        path = IMAGES_DIR / f"img_{categoria}{ext}"
        path.write_bytes(response.read())
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--force", action="store_true", help="baixa mesmo que já exista")
    parser.add_argument("--dry-run", action="store_true", help="só lista, não baixa")
    args = parser.parse_args()

    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    pending = [p for p in catalog if args.force or not p["image"]]
    print(f"{len(pending)} de {len(catalog)} imagens para baixar")

    if args.dry_run:
        for p in pending:
            print(f"  cat {p['category']}: {p['sourceUrl']}")
        return

    IMAGES_DIR.mkdir(exist_ok=True)
    failed = []
    for i, p in enumerate(pending, 1):
        try:
            path = download(p["sourceUrl"], p["category"])
            p["image"] = f"images/{path.name}"
            print(f"✓ [{i}/{len(pending)}] {path.name}")
        except Exception as e:
            failed.append((p["category"], str(e)[:80]))
            print(f"✗ [{i}/{len(pending)}] cat {p['category']} - {str(e)[:80]}")
        time.sleep(0.1)

    CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nSucesso: {len(pending) - len(failed)} | Falhas: {len(failed)}")
    for categoria, erro in failed:
        print(f"  cat {categoria}: {erro}")


if __name__ == "__main__":
    main()
