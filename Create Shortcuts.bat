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

:: Check if requirements-ShortuctCreator.txt exists and install requirements if not already installed
IF EXIST "requirements-ShortuctCreator.txt" (
    echo Installing requirements from requirements-ShortuctCreator.txt...
    pip install -r requirements-ShortuctCreator.txt
) ELSE (
    echo No requirements-ShortuctCreator.txt found. Installing all requirements
    IF EXIST "requirements.txt" (
        echo Installing requirements from requirements.txt...
        pip install -r requirements.txt
    ) ELSE (
        echo No requirements.txt found.
    )
)

:: Clear the clutter
call cls

:: Run the script (UrlAutomation.py)
echo Running ShortutCreator.py...
python ShortutCreator.py

:: Pause to keep the command window open (optional)
:: pause
