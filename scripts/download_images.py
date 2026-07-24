# -*- coding: utf-8 -*-
"""Download free Unsplash images (no watermark) into assets/images/."""
from pathlib import Path
import urllib.request
import ssl

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images"
OUT.mkdir(parents=True, exist_ok=True)

# Stable Unsplash source URLs (free license, no watermark)
# format: category -> list of (filename, url)
IMAGES = {
    "gym": [
        ("hero.jpg", "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1540497077202-7c8a3999166f?w=900&q=80&auto=format&fit=crop"),
    ],
    "wellness": [
        ("hero.jpg", "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1518611012118-696072aa579a?w=900&q=80&auto=format&fit=crop"),
    ],
    "crossfit": [
        ("hero.jpg", "https://images.unsplash.com/photo-1517963879433-6ad2b056d712?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1526506118085-60ce8714f8c5?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1434682772747-f16d3ea162c3?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1581009146145-b5ef050c149a?w=900&q=80&auto=format&fit=crop"),
    ],
    "market": [
        ("hero.jpg", "https://images.unsplash.com/photo-1542838132-92c53300491e?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1604719312566-8912e9227c6a?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=900&q=80&auto=format&fit=crop"),
    ],
    "hyper": [
        ("hero.jpg", "https://images.unsplash.com/photo-1604719312566-8912e9227c6a?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=900&q=80&auto=format&fit=crop"),
    ],
    "organic": [
        ("hero.jpg", "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1488459716781-31db52582fe9?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1461354464878-ad92f492a5a0?w=900&q=80&auto=format&fit=crop"),
    ],
    "clinic": [
        ("hero.jpg", "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?w=900&q=80&auto=format&fit=crop"),
    ],
    "dental": [
        ("hero.jpg", "https://images.unsplash.com/photo-1606811841689-23dfddce3e95?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1629909613654-28e377c37b09?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1609840114035-3c981b782dfe?w=900&q=80&auto=format&fit=crop"),
    ],
    "family": [
        ("hero.jpg", "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1581595220892-b0739db3b8c5?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?w=900&q=80&auto=format&fit=crop"),
    ],
    "restaurant": [
        ("hero.jpg", "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=900&q=80&auto=format&fit=crop"),
    ],
    "bistro": [
        ("hero.jpg", "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1493770348161-369560ae357d?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=900&q=80&auto=format&fit=crop"),
    ],
    "grill": [
        ("hero.jpg", "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1544025162-d76694265947?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1558030006-450675393462?w=900&q=80&auto=format&fit=crop"),
    ],
    "cafe": [
        ("hero.jpg", "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1498804103079-a6351b050096?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1511920170033-f8396924c348?w=900&q=80&auto=format&fit=crop"),
    ],
    "salon": [
        ("hero.jpg", "https://images.unsplash.com/photo-1560066984-138dadb4c035?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1562322140-8baeececf3df?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1633681926022-84c23e8cb2d6?w=900&q=80&auto=format&fit=crop"),
    ],
    "realestate": [
        ("hero.jpg", "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=900&q=80&auto=format&fit=crop"),
    ],
    "saas": [
        ("hero.jpg", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1553877522-43269d4ea984?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=900&q=80&auto=format&fit=crop"),
    ],
    "portfolio": [
        ("hero.jpg", "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1558655146-d09347e92766?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1586717791821-3f44a563fa4c?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=900&q=80&auto=format&fit=crop"),
    ],
    "shop": [
        ("hero.jpg", "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=1400&q=80&auto=format&fit=crop"),
        ("card1.jpg", "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=900&q=80&auto=format&fit=crop"),
        ("card2.jpg", "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=900&q=80&auto=format&fit=crop"),
        ("card3.jpg", "https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?w=900&q=80&auto=format&fit=crop"),
    ],
}

CREDITS = """# Image credits

All photos are from **Unsplash** — free to use, no watermark, commercial OK.
https://unsplash.com/license

Downloaded for Ibra Studio demo templates. Replace with client photos when customizing a real site.

Categories map to folders under `assets/images/`.
"""

ctx = ssl.create_default_context()

def download(url, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 5000:
        print("skip", dest.relative_to(ROOT))
        return
    req = urllib.request.Request(url, headers={"User-Agent": "IbraStudio/1.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
        dest.write_bytes(r.read())
    print("ok", dest.relative_to(ROOT), dest.stat().st_size)


def main():
    (OUT / "CREDITS.md").write_text(CREDITS, encoding="utf-8")
    for cat, files in IMAGES.items():
        for name, url in files:
            try:
                download(url, OUT / cat / name)
            except Exception as e:
                print("FAIL", cat, name, e)


if __name__ == "__main__":
    main()
