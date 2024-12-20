# YouTube Video Downloader

This repository contains a simple and efficient YouTube video downloader tool designed to streamline downloading YouTube videos or audio. Follow the instructions below to set up and use the program.

---

## Prerequisites

Before using this tool, ensure the following:

- **Python**: Install Python (version 3.7 or later) from [python.org](https://www.python.org/downloads/).
- **Pip**: Ensure `pip` (Python's package manager) is installed. You can verify this by running `python -m pip --version` in a terminal.

---

## Getting Started

### 1. **Download the Program**
- Download the repository as a ZIP file by clicking the green **Code** button on GitHub.
- Extract the ZIP file to a desired location on your computer.

### 2. **Run the Setup**
- Locate and run the file `Create Shortcuts.bat`.  
- You might encounter a "Windows protected your PC" prompt. If this happens:
  - Click **More info** and then **Run anyway**.
  - If prompted, provide administrator permissions.

### 3. **Verify Setup**
- After running the setup, two icons should appear on your desktop:
  - **Url Getter**
  - **Video Downloader**

---

## How to Use

### **Url Getter**
This program collects YouTube video URLs. Here's how to use it:

1. **Start the Program**: Double-click the **Url Getter** desktop icon. Wait for the program to load. It will notify you when it is ready and listening for the hotkey.
2. **Open YouTube Video**: In your browser, navigate to the YouTube video you wish to download. Ensure the browser is the active window.
3. **Capture the URL**:
   - Press the hotkey `ALT+S`. The program will:
     - Automatically select the browser address bar using `CTRL+L`.
     - Copy the URL using `CTRL+C`.
   - You will be notified when the program successfully captures the URL.
4. **Repeat for Multiple Videos**: Continue adding URLs by navigating to other videos and pressing the hotkey again.
5. **Exit**: To stop the program, close the command prompt window.

**Notes**: 
- Only URLs starting with `www.youtube.com` will be saved.
- Duplicate URLs are automatically removed.
- Saved URLs can be found in the `video_urls.txt` file for review.

---

### **Video Downloader**
This tool provides options to process the collected video URLs. Double-click the **Video Downloader** desktop icon and select one of the following options:

1. **MP4 Downloader**: Downloads all videos listed in `video_urls.txt` in 480p resolution.
2. **MP3 Downloader**: Downloads all videos listed in `video_urls.txt` as audio files (MP3 format).
3. **Backup and Wipe URLs**: 
   - Creates a backup of `video_urls.txt` in the `Url Backups` folder (created if it doesn't exist).
   - Wipes `video_urls.txt` after creating the backup to avoid re-downloading the same videos.

---

## File Details

- **`video_urls.txt`**: Contains the list of collected YouTube video URLs. You can manually edit this file if necessary.
- **`Url Backups` Folder**: Stores backup copies of `video_urls.txt`. Backup filenames include a user-specified name and the `_backup` postfix.

---

## Additional Notes

- Ensure the browser is the active window when using the **Url Getter**.
- Shortcut hotkeys like `CTRL+L` and `CTRL+C` are standard for most browsers but may vary depending on your operating system or browser settings. Check these if you encounter issues.
- For any discrepancies in URLs or downloads, review and edit the `video_urls.txt` file before running the **Video Downloader**.

Enjoy seamless downloading of your favorite YouTube videos and audio!
