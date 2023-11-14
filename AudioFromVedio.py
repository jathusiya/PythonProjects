# import moviepy.editor

# video = moviepy.editor.VideoFileClip("xyz.mp4")
from moviepy.editor import VideoFileClip

video = VideoFileClip("xyz.mp4")

audio = video.audio
audio.write_audiofile("extrasong.mp3")
