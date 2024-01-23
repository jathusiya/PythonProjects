from moviepy.video.io.VideoFileClip import VideoFileClip

def cut_video(input_path, output_path, start_time, end_time):

    clip = VideoFileClip(input_path)
    cut_clip = clip.subclip(start_time, end_time)
    cut_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    # Example usage:
    input_video_path = "C:/Users/hp/Desktop/Project/portfolio/static/videos/hack.mp4"
    output_video_path = "C:/Users/hp/Desktop/Project/portfolio/static/videos/hack1.mp4"
    start_time_seconds = 00  # Start cutting from 10 seconds
    end_time_seconds = 28    # End cutting at 30 seconds

    cut_video(input_video_path, output_video_path, start_time_seconds, end_time_seconds)
