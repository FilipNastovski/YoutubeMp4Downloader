import os
import time

def ensure_file_exists(file_path):
    """
    Ensure the file exists. If not, create an empty file.
    """
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass  # Create an empty file
        print(f"Created file: {file_path}")

def remove_duplicates_from_file(file_path):
    """
    Removes duplicate URLs from a file.

    Args:
        file_path (str): Path to the text file to clean.
    """
    try:
        with open(file_path, "r") as file:
            urls = file.readlines()

        # Remove duplicates and preserve order
        unique_urls = list(dict.fromkeys(url.strip() for url in urls if url.strip()))

        # Write back only unique URLs
        with open(file_path, "w") as file:
            file.write("\n".join(unique_urls) + "\n")

        duplicates_removed = len(urls) - len(unique_urls)
        if duplicates_removed > 0:
            print(f"Removed {duplicates_removed} duplicate(s) from {file_path}.")
        else:
            print(f"No duplicates found in {file_path}.")
        print(f"Links to be downloaded = {len(unique_urls)}")
    except Exception as e:
        print(f"An error occurred while cleaning duplicates: {e}")

if __name__ == "__main__":
    file_path = "video_urls.txt"
    ensure_file_exists(file_path)
    remove_duplicates_from_file(file_path)
    print()
