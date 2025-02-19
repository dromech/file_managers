import os
import sys
import shutil
import math

# ===== Configuration Settings =====
SPLIT_SIZE = 200  # Number of files per batch folder
BATCH_FOLDER_PREFIX = "batch_"  # Prefix for the batch folder names
# ==================================

def split_files_into_batches(source_folder, batch_size=SPLIT_SIZE):
    """
    Splits files in the source_folder into subfolders containing batch_size files each.
    The last folder may have fewer files if the total number of files isn't a multiple of batch_size.
    """
    # Validate the source folder
    if not os.path.isdir(source_folder):
        print(f"Error: '{source_folder}' is not a valid directory.")
        return

    # List all files (non-recursive) in the directory
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    
    # Optional: Sort files alphabetically
    files.sort()

    num_files = len(files)
    if num_files == 0:
        print("No files found in the provided directory.")
        return

    # Calculate the number of batches needed
    num_batches = math.ceil(num_files / batch_size)
    print(f"Found {num_files} files. Creating {num_batches} folder(s) with up to {batch_size} files each.")

    for i in range(num_batches):
        # Create a new folder for the current batch
        batch_folder = os.path.join(source_folder, f"{BATCH_FOLDER_PREFIX}{i+1}")
        os.makedirs(batch_folder, exist_ok=True)
        
        # Get the slice of files for this batch
        batch_files = files[i * batch_size : (i + 1) * batch_size]
        
        # Move each file into the current batch folder
        for file_name in batch_files:
            src_path = os.path.join(source_folder, file_name)
            dst_path = os.path.join(batch_folder, file_name)
            shutil.move(src_path, dst_path)
            print(f"Moved: {file_name} -> {batch_folder}")

    print("File splitting complete.")

if __name__ == "__main__":
    # Ensure the folder path is provided as a command line argument
    if len(sys.argv) < 2:
        print("Usage: python folder_splitter.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    split_files_into_batches(folder_path)
