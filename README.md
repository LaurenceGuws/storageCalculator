# Storage Calculator

## Overview

The Storage Calculator is a Python script designed to efficiently calculate the sizes of folders within a specified drive or directory. It skips critical system folders to focus on user data and provides detailed output in a CSV file, including human-readable sizes in GB and MB alongside the raw size in bytes.

## Features

- **Efficient Calculation**: Utilizes multiprocessing to speed up the folder size calculations.
- **System Folder Exclusion**: Skips essential system and hardware-related folders based on the operating system.
- **Detailed Output**: Outputs folder sizes in a CSV file with sizes in GB, MB, and bytes, sorted by size.
- **Statistics**: Provides detailed scan statistics including elapsed time and folders processed per second.

## Requirements

- Python 3.6 or higher
- `tqdm` package for progress bar
- `multiprocessing` (part of Python's standard library)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/storage-calculator.git
   cd storage-calculator
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     .\venv\Scripts\Activate.ps1
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install necessary packages**:

   ```bash
   pip install tqdm
   ```

## Usage

To run the script and calculate folder sizes for a specified drive or directory:

```bash
python main.py <drive_path>
```

For example, to scan the C: drive on a Windows system:

```bash
python main.py C:\
```

## Output

- The script will generate a `folder_sizes.csv` file in the current directory.
- The CSV file contains the following columns: `Size (GB)`, `Size (MB)`, `Size (Bytes)`, `Folder`.
- The script will also print scan statistics including the total elapsed time and the number of folders processed per second.

## Example Output

```
Starting to calculate sizes in C:\...
Scanning folders: 100%|█████████████████████████████████████████████████████| 2000/2000 [00:30<00:00, 65.23folders/s]
Size calculation complete in 30.66 seconds.
Processed 2000 folders at 65.23 folders/second.
Folder sizes have been written to folder_sizes.csv
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README provides a comprehensive overview of your project, detailing its features, installation steps, usage instructions, and more. It should help users quickly understand how to use and contribute to the Storage Calculator.