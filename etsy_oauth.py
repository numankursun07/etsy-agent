import os
import base64
import hashlib
import secrets
import webbrowser
from urllib.parse import urlencode, urlparse, parse_qs

import requests
from dotenv import load_dotenv
from http.server import BaseHTTPRequestHandler, HTTPServer


load_dotenv()

KEYSTRING = os.getenv("ETSY_KEYSTRING")
SHARED_SECRET = os.getenv("ETSY_SHARED_SECRET")

if not KEYSTRING or not SHARED_SECRET:
    raise RuntimeError("ETSY_KEYSTRING veya ETSY_SHARED_SECRET .env içinde bulunamadı.")

REDIRECT_URI = "http://localhost:3003/oauth/redirect"
AUTH_URL = "https://www.etsy.com/oauth/connect"
TOKEN_URL = "https://api.etsy.com/v3/public/oauth/token"

PORT = 3003

state = secrets.token_urlsafe(32)

code_verifier = secrets.token_urlsafe(64)

code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier.encode("ascii")).digest()
).decode("ascii").rstrip("=")


class OAuthHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path != "/oauth/redirect":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")
            return

        params = parse_qs(parsed.query)

        returned_state = params.get("state", [None])[0]
        authorization_code = params.get("code", [None])[0]

        if returned_state != state:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid state")
            return

        if not authorization_code:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Authorization code missing")
            return

        print("\nAuthorization code received.")

        token_response = requests.post(
            TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "client_id": KEYSTRING,
                "redirect_uri": REDIRECT_URI,
                "code": authorization_code,
                "code_verifier": code_verifier,
            },
            timeout=30,
        )

        print("Token HTTP:", token_response.status_code)

        if token_response.status_code != 200:
            print(token_response.text)

            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Token request failed")
            return

        token_data = token_response.json()

        access_token = token_data.get("access_token")
        refresh_token = token_data.get("refresh_token")

        print("OAuth authorization successful.")
        print("Access token received:", bool(access_token))
        print("Refresh token received:", bool(refresh_token))

        if refresh_token:
            with open("etsy_tokens.txt", "w", encoding="utf-8") as f:
                f.write(f"ACCESS_TOKEN={access_token}\n")
                f.write(f"REFRESH_TOKEN={refresh_token}\n")

            print("\nTokens saved to etsy_tokens.txt")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        html = """
        <html>
        <head>
            <meta charset="utf-8">
            <title>Etsy OAuth</title>
        </head>
        <body>
            <h1>Etsy OAuth başarılı!</h1>
            <p>Yetkilendirme tamamlandı. Bu pencereyi kapatabilirsiniz.</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))


print("Etsy OAuth test server")
print()
print("Redirect URI:")
print(REDIRECT_URI)
print()

authorization_params = {
    "response_type": "code",
    "client_id": KEYSTRING,
    "redirect_uri": REDIRECT_URI,
    "scope": "listings_r listings_w shops_r transactions_r",
    "state": state,
    "code_challenge": code_challenge,
    "code_challenge_method": "S256",
}

authorization_url = AUTH_URL + "?" + urlencode(authorization_params)

print("Authorization URL hazır.")
print("Tarayıcı açılıyor...")

server = HTTPServer(("localhost", PORT), OAuthHandler)

webbrowser.open(authorization_url)

print()
print("Etsy yetkilendirme ekranını bekliyorum...")
print("Tarayıcıdaki işlemi tamamlayın.")
print()

server.handle_request()

print()
print("OAuth işlemi tamamlandı.")