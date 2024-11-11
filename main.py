import os
from youtube import get_random_video
import json

def main():
    # Load the config file
    with open("config.json") as f:
        config = json.load(f)
        
    channel_id = config["channel_id"]
    max_video_results = config["max_video_results"]
    video_duration = config["video_duration"]

    link = get_random_video(channel_id, max_video_results, video_duration)
    print(link)
    # Play the video
    os.system(f"start {link}")

if __name__ == "__main__":
    main()
