import random
from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import proglog
from config import video_list

def background(length):
    bg_video = random.choice(video_list)
    print("Using "+bg_video+" for generating background.")
    total_time = length
    duration = VideoFileClip("assets/backgrounds/"+bg_video).duration
    start_time = random.uniform(20, duration - total_time)
    input_video_path = "assets/backgrounds/"+bg_video
    output_video_path = "assets/temp/clip.mp4"

    with VideoFileClip(input_video_path) as video:
        new = video.subclip(start_time, start_time+total_time)
        new.write_videofile(output_video_path, audio_codec='aac', logger=proglog.TqdmProgressBarLogger(print_messages=False))