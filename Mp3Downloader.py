import os
import subprocess
from yt_dlp import YoutubeDL
from concurrent.futures import ThreadPoolExecutor

def open_local_downloads_folder():
    # Get the path to the 'downloads' folder in the current directory (where the script is located)
    script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    downloads_folder = os.path.join(script_directory, "Mp3Downloads")  # Append 'downloads' to the script directory

    # Check if the 'downloads' folder exists
    if os.path.exists(downloads_folder):
        # Open the folder in the file explorer
        subprocess.run(["explorer", downloads_folder])
    else:
        print(f"The folder '{downloads_folder}' does not exist.")

def download_audio(url, output_folder="downloads"):
    """
    Download a YouTube video as MP3 to a specific folder using yt-dlp.

    Args:
        url (str): The URL of the YouTube video to download.
        output_folder (str): The folder where the audio will be saved.
    """
    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best available audio
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',  # Extract audio after download
                'preferredcodec': 'mp3',      # Convert to MP3
                'preferredquality': '192',    # Audio quality (kbps)
            }
        ],
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Save the file in the specified folder
        'noplaylist': True,  # Download a single video, not a playlist
    }

    try:
        print(f"Downloading audio (MP3): {url}")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Successfully downloaded audio: {url}\n")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def download_audios_from_file(file_path, output_folder="downloads"):
    """
    Read URLs from a file and download each audio as MP3 to the specified folder.

    Args:
        file_path (str): Path to the text file containing YouTube URLs.
        output_folder (str): The folder where audio files will be saved.
    """
    try:
        # Read URLs from file
        with open(file_path, "r") as file:
            urls = [line.strip() for line in file if line.strip()]

        if not urls:
            print("No URLs found in the file.")
            return

        # Use ThreadPoolExecutor to download audios concurrently, with a limit of 10 concurrent downloads
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(lambda url: download_audio(url, output_folder), urls)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # File containing YouTube URLs (one per line)
    input_file = "video_urls.txt"

    # Folder where the downloaded audios will be saved
    output_folder = "Mp3Downloads"

    # Start downloading audio files
    download_audios_from_file(input_file, output_folder)
    
    input("Press Enter to exit...")
    open_local_downloads_folder()
