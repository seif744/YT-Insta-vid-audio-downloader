import yt_dlp
import os

def download_video():
    url = input("Enter YouTube URL: ")
    file_name = input("Enter file name (without extension): ")
    folder_path = r"C:\Users\might\OneDrive\Desktop\Bideo" #doesnt go to onedrive desktop be careful

    # Ensure folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Full output path: folder + filename
    output_template = os.path.join(folder_path, file_name + '.%(ext)s')

    ydl_opts = {
        'format': 'best[ext=mp4][vcodec^=avc1][acodec^=mp4a]/best',
        'outtmpl': output_template,
        'postprocessors': []
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

#download_video()


def download_audio_no_ffmpeg():
    url = input("Enter YouTube URL: ")
    file_name = input("Enter audio file name (without extension): ")
    
    folder_path = r"C:\Users\might\Desktop\Bideo"  #doesnt go to onedrive desktop be careful
    os.makedirs(folder_path, exist_ok=True)

    output_template = os.path.join(folder_path, file_name + ".%(ext)s")

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': output_template,
        'postprocessors': []  # No ffmpeg, so no audio conversion
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

#download_audio_no_ffmpeg()

def instagram():
    url = input("Enter Instagram URL: ")
    file_name = input("Enter file name (without extension): ")
    
    folder_path = r"C:\Users\might\Desktop\Bideo"  # Update this to your preferred folder
    os.makedirs(folder_path, exist_ok=True)

    output_template = os.path.join(folder_path, file_name + ".%(ext)s")

    ydl_opts = {
        'format': 'best',
        'outtmpl': output_template,
        'postprocessors': []
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
#instagram()

def insta_audio():
    url = input("Enter Instagram URL: ")
    file_name = input("Enter audio file name (without extension): ")
    
    folder_path = r"C:\Users\might\Desktop\Bideo"  
    os.makedirs(folder_path, exist_ok=True)

    output_template = os.path.join(folder_path, file_name + ".%(ext)s")

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': output_template,
        'postprocessors': []  # No ffmpeg, so no audio conversion
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

#insta_audio()

s=input("Enter if you want to download a youtube 'video', youtube 'audio', insta 'reel' or instagram 'raudio': ").strip().lower()
match(s):
    case "video":
        download_video()
    case "audio":
        download_audio_no_ffmpeg()
    case "reel":
        instagram()
    case "raudio":
        insta_audio()
    case _:
        print("Invalid option. Please enter 'video', 'audio', or 'reel'.")

