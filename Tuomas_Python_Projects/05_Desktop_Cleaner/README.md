# Desktop Cleaner App

This Python script organizes files in a specified directory by moving them into subfolders based on their file extensions. It helps keep your downloads or any other directory clean and organized.

## Features

- Automatically creates subfolders based on file extensions.
- Moves files into their respective subfolders.
- Ensures subfolders are created only if they don't already exist.
- Provides feedback on the operations performed.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the script.

2. Ensure you have Python 3.x installed on your system.

## Usage

1. Open the script file and modify the `filepath` variable to point to the directory you want to organize. By default, it is set to `C:/Users/user/Downloads`.

```python
filepath = "C:/Users/user/Downloads"
```

2. Run the script:

```bash
python desktop_cleaner.py
```

## Code Explanation

### Import Libraries

```python
import os
import shutil
```

### Define `create_folder` Function

This function creates a new folder if it doesn't already exist.

```python
def create_folder(folderPath, folderName):
    os.makedirs(folderPath, exist_ok=True)
    print(f"Created new folder: {folderName}")
```

### Main Function

The main function performs the following steps:

1. Prints a welcome message.
2. Checks if the specified filepath exists.
3. Lists all items in the directory.
4. For each item, if it is a file, it:
    - Determines the subfolder name based on the file extension.
    - Creates the subfolder if it doesn't exist.
    - Moves the file to the appropriate subfolder.
    - Prints a message indicating the file has been moved.

```python
def main():
    print("Desktop Cleaner App")

    filepath = "C:/Users/user/Downloads"

    if not os.path.exists(filepath):
        print(f"The specified filepath does not exist: ${filepath}")

    for item in os.listdir(filepath):
        itempath = os.path.join(filepath, item)

        if os.path.isfile(itempath):
            subfolderName = f"{item.split('.')[-1].upper()} FILES"
            subfolderPath = os.path.join(filepath, subfolderName)

            if not os.path.exists(subfolderPath):
                create_folder(subfolderPath, subfolderName)

            new_location = os.path.join(subfolderPath, item)
            shutil.move(itempath, new_location)
            print(f"Moved file '{item}' to folder '{subfolderName}'")
```

### Entry Point

This ensures that the script runs the `main` function when executed directly.

```python
if __name__ == "__main__":
    main()
```

## Notes

- Ensure that the specified filepath exists and is correct before running the script.
- The script is currently set to organize files in the `C:/Users/user/Downloads` directory. You can modify the `filepath` variable to any directory you wish to organize.
