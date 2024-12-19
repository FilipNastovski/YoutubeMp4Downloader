import pyautogui
import pyperclip
import keyboard
import time

def get_current_url_from_browser():
    # Simulate pressing CTRL + L to focus the address bar
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.3)  # Wait for the address bar to be focused

    # Simulate pressing CTRL + C to copy the URL
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait for the clipboard to update

    pyautogui.click(x=10, y=600)
    
    # Get the URL from the clipboard
    url = pyperclip.paste()
    return url

def save_url_to_file(url, filename="video_urls.txt"):
    # Save the URL to the file
    with open(filename, "a") as file:
        file.write(url + "\n")
    print(f"URL saved: {url}")

def listen_for_hotkey():
    print("Listening for ALT + S to save the current URL...")
    while True:
        if keyboard.is_pressed('alt+s'):
            print("Hotkey detected! Extracting URL...")
            pyautogui.click(x=10, y=500)
            # time.sleep(1)
            url = get_current_url_from_browser()
            if url:
                save_url_to_file(url)
            else:
                print("No URL found or clipboard is empty.")
            time.sleep(1)  # Wait a bit before allowing another hotkey press


if __name__ == "__main__":
    listen_for_hotkey()
    