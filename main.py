from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()
os.makedirs('./logs', exist_ok=True)

class OAuth():
    def __init__(self, client_id, client_secret, refresh_token):
        self.token_url = 'https://oauth2.googleapis.com/token'
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
    
    def get_new_tokens(self):
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token"
        }

        response = requests.post(self.token_url, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to refresh token: {response.text}")

if __name__ == "__main__":
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

    try:
        oauth = OAuth(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
        tokens = oauth.get_new_tokens()

        print("New Access Token:", tokens["access_token"])

        if "refresh_token" in tokens:
            print("New Refresh Token:", tokens["refresh_token"])
        else:
            print("No new refresh token returned.")
    except Exception as e:
        crnt_time = datetime.now()
        print(f"[{crnt_time.strftime('%d-%m-%Y %H:%M:%S')}] Error:", ''.join(str(e).splitlines()))

        with open(f"logs/{crnt_time.strftime('%d-%m-%Y')}-error.log", "a") as f:
            err = str(e).splitlines()
            for e in err:
                f.write(f"{crnt_time.strftime('%H:%M:%S')}\t{e}\n")