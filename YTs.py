import youtube_dl

# Ask for the YouTube URL from the user
url = input("Enter the YouTube URL link: ")

# Ask the user to choose a download format
print("Choose a download format:")
print("1 = .mp3")
print("2 = .mp4")
print("3 = .avi")
print("4 = .gif")
format_choice = input("Enter the format number: ")

# Define the download format based on user choice
if format_choice == "1":
    download_format = "bestaudio/best"
elif format_choice == "2":
    download_format = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
elif format_choice == "3":
    download_format = "best[ext=avi]"
elif format_choice == "4":
    download_format = "best[ext=gif]"

# Download the video based on user input
ydl_opts = {
    'format': download_format,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url]).
