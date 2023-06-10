import os
import shutil
from datetime import datetime

def move_media_files(source_dir, destination_dir):
    media_extensions = ['.docx', '.rtf', '.doc', '.txt', '.DOC']
    total_files = 0
    processed_files = 0

    # Count the total number of files to be processed
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in media_extensions:
                total_files += 1

    # Process the files and show progress
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in media_extensions:
                source_path = os.path.join(root, file)
                creation_year = get_file_creation_year(source_path)
                if creation_year is None:
                    print(f"Skipped (Unable to determine creation year): {source_path}")
                    continue
                destination_subdir = os.path.join(destination_dir, str(creation_year))
                os.makedirs(destination_subdir, exist_ok=True)
                destination_path = os.path.join(destination_subdir, file)

                # Skip if the file already exists in the destination directory
                if os.path.exists(destination_path):
                    print(f"Skipped (File already exists): {source_path}")
                    continue

                shutil.move(source_path, destination_path)
                processed_files += 1
                print_progress(processed_files, total_files)

def get_file_creation_year(file_path):
    stat = os.stat(file_path)
    modification_datetime = datetime.fromtimestamp(stat.st_mtime)
    return modification_datetime.year

def print_progress(processed_files, total_files):
    progress = processed_files / total_files * 100
    remaining_files = total_files - processed_files
    remaining_time = remaining_files * 0.5  # Assuming 0.5 seconds per file
    print(f"Progress: {processed_files}/{total_files} ({progress:.2f}%) - Estimated Time Remaining: {remaining_time:.2f} seconds")

# Specify the source directory where the media files are located
source_directory = 'C:\\Some\\Path\\Here\\'

# Specify the destination directory where the photos will be moved
destination_directory = 'C:\\Some\\Path\\Here\\'

# Call the function to move the media files
move_media_files(source_directory, destination_directory)
