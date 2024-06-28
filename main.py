import os
import time
import csv
import multiprocessing
from collections import defaultdict
from tqdm import tqdm

# Define critical system folders to exclude
def is_critical_system_folder(folder, os_type, startpath):
    if os_type == 'Windows':
        critical_system_folders = [
            'Windows', 'System32', 'System Volume Information', 'Recovery', 'Boot', 'ProgramData', '$Recycle.Bin'
        ]
    elif os_type == 'Linux':
        critical_system_folders = [
            'bin', 'boot', 'dev', 'etc', 'lib', 'lib64', 'mnt', 'proc', 'root', 'run', 'sbin',
            'srv', 'sys', 'tmp', 'usr', 'var', 'lost+found'
        ]
    else:
        critical_system_folders = []
    return any(os.path.normpath(folder).startswith(os.path.normpath(os.path.join(startpath, sys_folder))) for sys_folder in critical_system_folders)

# Get the size of a file
def get_file_size(filepath):
    try:
        return os.path.getsize(filepath)
    except (FileNotFoundError, OSError):
        return 0

# Calculate the sizes of folders
def calculate_folder_sizes(startpath, os_type):
    folder_sizes = defaultdict(int)
    folder_count = 0

    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        for root, dirs, files in tqdm(os.walk(startpath, topdown=True), desc="Scanning folders"):
            folder_count += 1
            dirs[:] = [d for d in dirs if not is_critical_system_folder(os.path.join(root, d), os_type, startpath)]
            if not is_critical_system_folder(root, os_type, startpath):
                filepaths = [os.path.join(root, f) for f in files]
                sizes = pool.map(get_file_size, filepaths)
                for size in sizes:
                    folder_sizes[root] += size

    return folder_sizes, folder_count

# Write the folder sizes to a CSV file
def write_to_csv(folder_sizes, output_file):
    sorted_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Size (GB)', 'Size (MB)', 'Size (Bytes)', 'Folder'])
        for folder, size in sorted_folders:
            size_gb = size / (1024 ** 3)
            size_mb = size / (1024 ** 2)
            writer.writerow([round(size_gb, 3), round(size_mb, 3), size, folder])

# Main function to run the script
def main(drive_path):
    os_type = 'Windows' if os.name == 'nt' else 'Linux'
    
    start_time = time.time()
    
    print(f"Starting to calculate sizes in {drive_path}...")
    folder_sizes, folder_count = calculate_folder_sizes(drive_path, os_type)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    folders_per_second = folder_count / elapsed_time
    print(f"Size calculation complete in {elapsed_time:.2f} seconds.")
    print(f"Processed {folder_count} folders at {folders_per_second:.2f} folders/second.")
    
    output_csv = 'folder_sizes.csv'
    write_to_csv(folder_sizes, output_csv)
    print(f"Folder sizes have been written to {output_csv}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Calculate folder sizes and save the results.")
    parser.add_argument('drive_path', type=str, help="Path of the drive to scan")
    args = parser.parse_args()
    main(args.drive_path)
