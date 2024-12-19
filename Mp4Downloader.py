import os
import subprocess
from yt_dlp import YoutubeDL
from concurrent.futures import ThreadPoolExecutor

def open_local_downloads_folder():
    # Get the path to the 'downloads' folder in the current directory (where the script is located)
    script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    downloads_folder = os.path.join(script_directory, "Mp4Downloads")  # Append 'downloads' to the script directory

    # Check if the 'downloads' folder exists
    if os.path.exists(downloads_folder):
        # Open the folder in the file explorer
        subprocess.run(["explorer", downloads_folder])
    else:
        print(f"The folder '{downloads_folder}' does not exist.")


def download_video(url, output_folder="downloads"):
    """
    Download a YouTube video to a specific folder using yt-dlp.

    Args:
        url (str): The URL of the YouTube video to download.
        output_folder (str): The folder where the video will be saved.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Set yt-dlp options
    ydl_opts = {
        'format': 'best[height<=480]',  # Download 480p or closest available resolution
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Save videos in the specified folder
        'noplaylist': True,  # Download a single video, not a playlist
    }

    try:
        print(f"Downloading video: {url}")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Successfully downloaded: {url}\n")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def download_videos_from_file(file_path, output_folder="downloads"):
    """
    Read URLs from a file and download each video to the specified folder.

    Args:
        file_path (str): Path to the text file containing YouTube URLs.
        output_folder (str): The folder where videos will be saved.
    """
    try:
        # Read URLs from file
        with open(file_path, "r") as file:
            urls = [line.strip() for line in file if line.strip()]

        if not urls:
            print("No URLs found in the file.")
            return

        # Use ThreadPoolExecutor to download videos concurrently, with a limit of 5 concurrent downloads
        with ThreadPoolExecutor(max_workers=6) as executor:
            executor.map(lambda url: download_video(url, output_folder), urls)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # File containing YouTube URLs (one per line)
    input_file = "video_urls.txt"

    # Folder where the downloaded videos will be saved
    output_folder = "Mp4Downloads"

    # Start downloading videos
    download_videos_from_file(input_file, output_folder)
    
    input("Press Enter to exit")
    open_local_downloads_folder()
