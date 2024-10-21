import subprocess

playlist_url = "YOUR_YOUTUBE_PLAYLIST_URL"
subprocess.call(['youtube-dl', '-f', 'bestaudio', '--extract-audio', '--audio-format', 'mp3', '--output', '%(title)s.%(ext)s', playlist_url])
