import os
import pyotp
from instagrapi import Client
from config import insta_caption
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
SECRET = os.getenv("INSTAGRAM_SECRET")

totp = pyotp.TOTP(SECRET)
code = totp.now()

def login():
    try:
        load_dotenv()
        client = Client()
        client.login(USERNAME, PASSWORD, verification_code=code)
        client.dump_settings(os.getenv("INSTA_SETTING"))
    except Exception as e:
        print(e)

def upload_reel(path):
    try:
        load_dotenv()
        print("Uploading to Instagram")
        client = Client()
        client.load_settings(os.getenv("INSTA_SETTING"))
        client.login(USERNAME, PASSWORD, verification_code=code)
        media = client.clip_upload(
            path=path,
            caption=insta_caption,
            thumbnail="assets/temp/frame.jpg"
        )
        media.dict()
        print("Uploaded to Instagram")
    except Exception as e:
        print(e)