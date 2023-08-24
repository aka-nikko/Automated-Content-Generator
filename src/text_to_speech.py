import requests
from requests.exceptions import JSONDecodeError
from rich.progress import track
from mutagen.mp3 import MP3
from config import tts_voice, comm_length

#Fuction for Converting Text To Speech using SteamLabsPolly API (Voice is Set to 'Matthew')
def convert(text, filepath):
    body = {"voice": tts_voice, "text": text, "service": "polly"}
    response = requests.post("https://streamlabs.com/polly/speak", data=body)
    try:
        voice_data = requests.get(response.json()["speak_url"])
        with open(filepath, "wb") as f:
            f.write(voice_data.content)
    except (KeyError):
        print("Please Enter Text")
    except (JSONDecodeError):
        print("Encountered an Error")

def text_to_speech(reddit_obj):
    try:
        print("Converting Text To Audio.")
        length = 0
        convert(text=reddit_obj["thread_title"], filepath="assets/temp/title.mp3")
        length += MP3(f"assets/temp/title.mp3").info.length
        for idx, comment in track(enumerate(reddit_obj["comments"]), "Saving..."):
            #Video Length Will be Less Than Specified Length
            if length > comm_length:
                idx = idx - 1
                break
            convert(text=comment["comment_body"], filepath=f"assets/temp/{idx}.mp3")
            length += MP3(f"assets/temp/{idx}.mp3").info.length
        print("Length of Video Will Be: ", length)
        return length, idx+1
    except Exception as e:
        raise e