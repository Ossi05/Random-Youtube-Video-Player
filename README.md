# Random-Youtube-Video-Player
Play a random Youtube video from a certain channel. 

Currently if you just put your YouTube Data API v3 key to .env file it will play a random motivation video from https://www.youtube.com/@BenLionelScott channel. You can change the channel in config.json file

# Setup

### 1. Install Dependencies
Install the required Python packages:
```
pip install -r requirements.txt
```

### 2. Add YouTube Data API v3 Key
Add your Youtube API key to .env file:
```
API_KEY = ""
```

### 3. Configure the Settings
- Edit `config.json` to change the settings:
  - `channel_id`: YouTube channel's ID to retrieve videos.
  - `video_duration`: YouTube video's duration (`"short"`, `"medium"`, `"long"`, `"any"`).
  - `max_video_results`: The maximum number of videos to retrieve.


### 4. Running main.py
    Next run main.py file
    ```Python main.py```
