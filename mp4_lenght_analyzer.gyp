import os
from moviepy.editor import VideoFileClip

def get_video_duration(file_path):
    try:
        clip = VideoFileClip(file_path)
        duration = clip.duration
        clip.reader.close()
        return duration
    except Exception as e:
        print(f"Error: {e}")
        return None

def analyze_mp4_files(directory):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found.")
        return

    mp4_files = [file for file in os.listdir(directory) if file.endswith('.mp4')]
    if not mp4_files:
        print(f"No MP4 files found in '{directory}'.")
        return

    for mp4_file in mp4_files:
        file_path = os.path.join(directory, mp4_file)
        duration = get_video_duration(file_path)
        if duration is not None:
            print(f"File: {mp4_file}, Duration: {duration} seconds")

if __name__ == "__main__":
    directory_path = "/Users/dor/Desktop/mp4_analyze"  # Replace with the directory containing your MP4 files
    analyze_mp4_files(directory_path)


