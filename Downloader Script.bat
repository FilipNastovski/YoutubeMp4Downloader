@echo off
setlocal


:: Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python from https://www.python.org/downloads/.
    pause
    exit /b
)

:: Check if pip is installed
python -m pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Pip is not installed. Please install pip by running: python -m ensurepip --upgrade
    pause
    exit /b
)

echo Python and pip are installed.

:: Check if .venv exists
IF NOT EXIST ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
) ELSE (
    echo Virtual environment already exists.
)

:: Activate the virtual environment
call .venv\Scripts\activate

:: Check if requirements.txt exists and install requirements if not already installed
IF EXIST "requirements-videodownloader.txt" (
    echo Installing requirements...
    pip install -r requirements-videodownloader.txt
) ELSE (
    echo No requirements-videodownloader.txt found. Installing all requirements
	IF EXIST "requirements.txt" (
		echo Installing requirements...
		pip install -r requirements.txt
	) ELSE (
    echo No requirements.txt found.
	)
)

:: clear the clutter
call cls

:: Ensure video_urls.txt exists and remove duplicates
echo Checking and cleaning URLs in video_urls.txt...
python CheckAndCleanUrls.py

:: Ask user for script choice (mp4, mp3, or backup)
echo Which script would you like to run?
echo 1. MP4 Downloader (Download videos)
echo 2. MP3 Downloader (Download music only)
echo 3. Backup and Wipe URLs
echo.
set /p choice="Enter choice (1, 2, or 3): "

:: Run the appropriate script based on the user's input
IF "%choice%"=="1" (
    echo Running MP4 downloader...
    python Mp4Downloader.py
) ELSE IF "%choice%"=="2" (
    echo Running MP3 downloader...
    python Mp3Downloader.py
) ELSE IF "%choice%"=="3" (
    echo Running Backup and Wipe URLs script...
    python BackupAndWipeUrls.py
) ELSE (
    echo Invalid choice.
)


:: Pause to keep the command window open
:: pause
