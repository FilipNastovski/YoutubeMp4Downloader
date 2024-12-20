import os
import shutil

def create_backup_and_wipe():
    source_file = "video_urls.txt"
    backup_dir = "Video URL Backups"
    
    # Check if the source file exists
    if not os.path.exists(source_file):
        print(f"The file '{source_file}' does not exist.")
        return

    # Create the backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"Created backup directory: {backup_dir}")

    # Ask the user for the backup file name
    user_input = input("Enter a name for the backup file (without extension): ").strip()
    if not user_input:
        print("Invalid input. Backup name cannot be empty.")
        return
    
    # Append the '_backup' postfix and add the .txt extension
    backup_file = os.path.join(backup_dir, f"{user_input}_backup.txt")

    try:
        # Copy the file to the backup directory
        shutil.copy(source_file, backup_file)
        print(f"Backup created: {backup_file}")
        
        # Wipe the original file
        with open(source_file, 'w') as f:
            f.write("")  # Clear the file content
        print(f"The content of '{source_file}' has been wiped.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_backup_and_wipe()
    input("Press enter to exit.")
