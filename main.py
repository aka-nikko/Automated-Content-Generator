from src.reddit_scrape import reddit_scrape
from src.text_to_speech import text_to_speech
from src.background import background
from src.final_video import make_final_video
from src.upload_instagram import login, upload_reel
from src.upload_youtube import upload_video
from src.time_stamp import time_stamp
from time import sleep
from importlib import reload
import config

import platform
if platform.system()=="Windows":
    from src.images_win import title_image, comments_image, remove_temp_files
elif platform.system()=="Linux":
    from src.images_linux import title_image, comments_image, remove_temp_files

def main():
    login()
    while True:
        try:
            #Reload Configurations
            reload(config)

            #Scrape Reddit Post
            reddit_object, video_name = reddit_scrape()

            #Text to Audio
            length, number_of_comments = text_to_speech(reddit_object)

            #Generate Background
            background(length)

            #Generate Title and Comment Images
            title_image(reddit_object)
            comments_image(reddit_object, number_of_comments)

            #Final Video Processing
            path = make_final_video(number_of_comments, video_name)

            #Upload Video to Instagram
            upload_reel(path)
            
            #Upload With Tool
            upload_video(path)

            #Remove Temporary Files, Show Time of Next Upload & Sleep
            remove_temp_files()
            time_stamp()
            sleep(config.sleep_time*60*60)

        #On Keyboard Interrupt (CTRL+c), Remove Temporary Files and Exit
        except KeyboardInterrupt:
            print('Interrupted!')
            sleep(3)
            remove_temp_files()
            break

        #During Any Exception, Print It, Remove Temporary Files and Skip Current Loop
        except Exception as e:
            print(e)
            sleep(3)
            remove_temp_files()
            continue

main()