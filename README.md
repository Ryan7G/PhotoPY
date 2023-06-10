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
