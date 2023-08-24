import random, os, subprocess
from config import emoji, discription, category, tags

def upload_video(path):
    print("Uploading to Youtube")
    subprocess.run(
        args=[
            'youtube-upload',
            f'--title='+random.choice(emoji)+' '+random.choice(emoji)+' #shorts',
            f'--description='+discription,
            f'--category='+category,
            f'--tags='+tags,
            f'--default-language=en',
            f'--default-audio-language=en',
            os.getcwd()+'/'+path,
        ],
        check=True
    )
    print("Uploaded")