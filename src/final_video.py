import proglog
from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
    ImageClip,
    concatenate_videoclips,
    concatenate_audioclips,
    CompositeAudioClip,
    CompositeVideoClip,
)

#Height and Width of Video
W, H = 1080, 1920

def make_final_video(number_of_clips, cleaned_text):
    try:
        print("Creating Final Video")
        VideoFileClip.reW = lambda clip: clip.resize(width=W)
        VideoFileClip.reH = lambda clip: clip.resize(width=H)
        background_clip = (
            VideoFileClip("assets/temp/clip.mp4")
            .without_audio()
            .resize(height=H)
            .crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)
        )

        # Gather All Audio Clips
        audio_clips = []
        for i in range(0, number_of_clips):
            audio_clips.append(AudioFileClip(f"assets/temp/{i}.mp3"))
        audio_clips.insert(0, AudioFileClip(f"assets/temp/title.mp3"))
        audio_concat = concatenate_audioclips(audio_clips)
        audio_composite = CompositeAudioClip([audio_concat])

        # Gather All Images
        image_clips = []
        for i in range(0, number_of_clips):
            image_clips.append(
                ImageClip(f"assets/temp/{i}.png")
                .set_duration(audio_clips[i + 1].duration)
                .set_position("center")
                .resize(width=W - 250),
            )
        image_clips.insert(
            0,
            ImageClip("assets/temp/title.png")
            .set_duration(audio_clips[0].duration)
            .set_position("center")
            .resize(width=W - 250),
        )
        image_concat = concatenate_videoclips(image_clips).set_position(
            ("center", "center")
        )
        image_concat.audio = audio_composite
        final = CompositeVideoClip([background_clip, image_concat])
        video_name = "result/"+cleaned_text+".mp4"
        final.write_videofile(
            video_name, fps=30, audio_codec="aac", audio_bitrate="192k", logger=proglog.TqdmProgressBarLogger(print_messages=False)
        )
        
        #Generating an Image for Thumbnail
        clip = VideoFileClip(video_name)
        clip.save_frame("assets/temp/frame.jpg", t = 1)
        return video_name
    
    except Exception as e:
        raise e from None