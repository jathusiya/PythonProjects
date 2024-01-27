from moviepy.editor import VideoFileClip, clips_array, concatenate_videoclips


def concatenate_videos(video1_path, video2_path, output_path):
    # Load the video clips
    video1 = VideoFileClip(video1_path)
    video2 = VideoFileClip(video2_path)

    # Concatenate the videos end-to-end
    final_clip = concatenate_videoclips([video1, video2], method="compose")
    #
    # # Concatenate the videos horizontally in one display
    # final_clip = clips_array([[video1], [video2]])

    # Write the concatenated video to a file
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')


if __name__ == "__main__":
    # Replace 'video1.mp4', 'video2.mp4', and 'output.mp4' with your actual file paths
    concatenate_videos("C:/Users/hp/Desktop/Project/portfolio/static/videos/hack.mp4",
                       "C:/Users/hp/Desktop/Project/portfolio/static/videos/hack1.mp4",
                       "C:/Users/hp/Desktop/Project/portfolio/static/videos/hack4.mp4")

