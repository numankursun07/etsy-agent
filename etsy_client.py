import os
from pathlib import Path

import requests
from dotenv import load_dotenv


load_dotenv()

SHOP_ID = 52079194
API_BASE = "https://api.etsy.com/v3/application"


def load_tokens():
    token_file = Path("etsy_tokens.txt")

    if not token_file.exists():
        raise FileNotFoundError("etsy_tokens.txt bulunamadı.")

    tokens = {}

    for line in token_file.read_text().splitlines():
        if "=" in line:
            key, value = line.strip().split("=", 1)
            tokens[key] = value

    if "ACCESS_TOKEN" not in tokens:
        raise RuntimeError("ACCESS_TOKEN bulunamadı.")

    return tokens


def get_headers():
    keystring = os.getenv("ETSY_KEYSTRING")
    shared_secret = os.getenv("ETSY_SHARED_SECRET")

    if not keystring or not shared_secret:
        raise RuntimeError("Etsy API bilgileri .env dosyasında bulunamadı.")

    tokens = load_tokens()

    return {
        "x-api-key": f"{keystring}:{shared_secret}",
        "Authorization": f"Bearer {tokens['ACCESS_TOKEN']}",
    }


def get_shop():
    response = requests.get(
        f"{API_BASE}/shops/{SHOP_ID}",
        headers=get_headers(),
        timeout=20,
    )

    response.raise_for_status()
    return response.json()


def get_active_listings():
    response = requests.get(
        f"{API_BASE}/shops/{SHOP_ID}/listings/active",
        headers=get_headers(),
        params={"limit": 25},
        timeout=20,
    )

    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    shop = get_shop()
    listings = get_active_listings()

    print("Etsy bağlantısı başarılı.")
    print("Mağaza:", shop["shop_name"])
    print("Shop ID:", shop["shop_id"])
    print("Aktif ilan sayısı:", listings["count"])