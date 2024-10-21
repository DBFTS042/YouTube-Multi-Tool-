import subprocess

playlist_url = "https://youtube.com/playlist?list=PLQYJ8WuT00qw4g81AfDUHOvy8ZkJvhU07&si=NrnRa0IH12lK_NbQ"
subprocess.call(['youtube-dl', '-f', 'bestaudio', '--extract-audio', '--audio-format', 'mp3', '--output', '%(title)s.%(ext)s', playlist_url])
