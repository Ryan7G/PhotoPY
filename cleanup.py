import os

def delete_files_by_type(directory, file_types):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if any(file.endswith(file_type) for file_type in file_types):
                os.remove(file_path)
                print(f"Deleted: {file_path}")

# Specify the directory to scan for files
directory_to_scan = '/path/to/directory'

# Specify the file types to delete
file_types_to_delete = ['.txt', '.docx', '.pdf']

# Call the function to delete files
delete_files_by_type(directory_to_scan, file_types_to_delete)