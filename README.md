**macOS and Linux**:

Open a terminal and run the following command to install the libraries:

```pip install hashlib shutil tqdm```

If you encounter permission errors, you may need to use sudo:

sudo pip install hashlib shutil tqdm

You will be prompted to enter your password before the installation begins.

**Windows**:
Open the command prompt (cmd) or PowerShell and run the following command to install the libraries:

```pip install hashlib shutil tqdm```

If you encounter permission errors, you may need to run the command prompt or PowerShell as an administrator. To do this, right-click on the respective application and choose "Run as administrator." Then, you can execute the installation command.

Once the libraries are installed successfully, you can proceed to run the Python application without any issues on any of the mentioned operating systems.

**Usage**;
I used these to organize roughly 71k files. there where multiple backups across multiple external drives i had recieved that needed organizing. this also included a lot of crap like .exe, .dll, ico, etc.. random file types.

First step is to organize photos into easily browasble directories. so specify that in the main photoOrganizer script, this will move all media files, photos videos etc.. into newly created folders named after the files creation year. 

The creation year is calculated from the photo metadata, this isn't 100% accurate but gets the jobe done. Once photos had copied over it then took about 30 mins to verify each folder contained media files. and i moved onto removing old / duplicate files.

The second script will analyze the files using the MD5 Hash and verify if a file is in fact a duplicate, then remove it. 


**photoOrganizer.py**
This script is designed to move media files from a source directory to a destination directory based on their creation year. Here's a high-level explanation of what the script does:

1. It imports the necessary modules: `os` for file and directory operations, `shutil` for file movement, and `datetime` for working with dates and times.
2. It defines a function called `move_media_files` that takes two parameters: `source_dir` (the directory where the media files are located) and `destination_dir` (the directory where the files will be moved).
3. The script defines a list called `media_extensions` which contains file extensions representing media files (e.g., `.docx`, `.rtf`, `.doc`, `.txt`, `.DOC`).
4. It initializes variables for keeping track of the total number of files and the number of processed files.
5. The script uses the `os.walk` function to traverse the source directory recursively and count the total number of media files that need to be processed.
6. It then traverses the source directory again and processes each media file individually.
7. For each media file, it checks if the file extension is in the `media_extensions` list.
8. If the file extension matches, it retrieves the full source path of the file and determines the creation year of the file using the `get_file_creation_year` function.
9. If the creation year cannot be determined, it skips the file and prints a message indicating the inability to determine the creation year.
10. It creates a subdirectory in the destination directory based on the creation year and ensures that the subdirectory exists.
11. It generates the full destination path by combining the destination subdirectory and the original file name.
12. If the file already exists in the destination directory, it skips the file and prints a message indicating that the file already exists.
13. If the file doesn't exist in the destination directory, it moves the file from the source path to the destination path using `shutil.move`.
14. It increments the count of processed files and calls the `print_progress` function to display the progress and estimated time remaining.
15. The script defines a function called `get_file_creation_year` that takes a file path as input and retrieves the year of the file's last modification.
16. The `print_progress` function calculates the progress percentage and the estimated time remaining based on the number of processed files and the total number of files. It then prints the progress information.
17. After defining the functions, the script specifies the source directory and the destination directory.
18. Finally, it calls the `move_media_files` function with the specified source and destination directories to initiate the media file moving process.


**Cleanup.py**
In this script:

1. The `delete_files_by_type` function takes the directory to scan (`directory`) and the file types to delete (`file_types`) as parameters.
2. The script uses `os.walk` to traverse the specified directory and its subdirectories.
3. For each file encountered, it checks if the file's extension matches any of the specified file types using a list comprehension and the `endswith` method.
4. If a match is found, it deletes the file using `os.remove` and prints a message indicating that the file has been deleted.
5. You can specify the directory to scan by setting the `directory_to_scan` variable to the desired path.
6. You can specify the file types to delete by setting the `file_types_to_delete` variable as a list of file extensions (e.g., ['.txt', '.docx', '.pdf']).
7. Call the `delete_files_by_type` function with the directory and file types to initiate the deletion process.

Please exercise caution when using this script, as it permanently deletes files. Make sure to double-check the specified directory and file types before running the script.
