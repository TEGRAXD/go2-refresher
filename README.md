# Google OAuth2 Refresher
A script specifically designed to obtain and manage new access tokens and/or refresh tokens required by Lavalink or similar projects that rely on refreshed Google OAuth2 tokens to function properly.

# Configuration
Please write your client_id, client_secret, and refresh_token in `.env`.

# Limitation
It requires an existing refresh token from a linked device.

# Running
```bash
pip install -r requirements.txt
python main.py
```