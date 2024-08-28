# DMG File Deleter
## Overview
The DMG File Deleter is a simple Python script that automatically scans your Downloads folder for `.dmg` files and offers to delete them. This helps in keeping your Downloads folder clean and free of unnecessary disk image files.

## Features
- **Automatic Detection**: Automatically detects the Downloads folder on macOS.
- **File Scanning**: Scans the Downloads folder and its subdirectories for `.dmg` files.
- **User Confirmation**: Prompts the user for confirmation before deleting the files.
- **Batch Deletion**: Deletes all detected `.dmg` files upon user consent.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/adamad44/DMG-file-deleter
    cd dmg-file-deleter
    ```

## Usage
1. Run the CLI script:
    ```sh
    python main.py
    ```

2. The CLI will:
    - Scan your Downloads folder for `.dmg` files.
    - Prompt you to confirm if you want to delete all detected `.dmg` files.
    - Delete the files if you confirm with 'y'.

3. Alternatively, you can run the GUI script:
    ```sh
    python GUI.py
    ```

4. The GUI will:
    - Scan your Downloads folder for `.dmg` files.
    - delete them if you wish

## Example
```sh
$ python main.py
No DMG files found in your downloads folder
```

