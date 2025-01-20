# BasicAutoPython
basic level devops automation using python
Sure! Below is a **README** file for the Python automation script we discussed. It includes a **detailed explanation** of what the script does, how to use it, and an overview of its functionality.

---

# DevOps Automation Script (Python)

This Python script automates the creation of directories and files, as well as monitoring a file for changes. It is intended for DevOps beginners to learn how automation works by performing simple file operations and monitoring changes. 

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Script Explanation](#script-explanation)
- [Extensions & Improvements](#extensions-improvements)
- [License](#license)

## Overview

This Python script automates the following tasks:

1. **Checks if a specific directory exists**. If the directory does not exist, it creates it.
2. **Checks if a file exists inside the directory**. If the file does not exist, it creates the file and writes initial content into it.
3. **Monitors the file for changes**. It continuously checks for modifications to the file and notifies the user if the file's content changes.

This script is useful for basic DevOps tasks such as directory/file management, automation, and file monitoring.

## Prerequisites

To run the script, you need the following:

1. **Python 3.x** installed on your system. You can download it from [Python Official Website](https://www.python.org/downloads/).
   
2. The `os` and `time` modules in Python, which are part of the Python standard library, so no additional installation is needed for these.

## Installation

1. **Clone the repository** (or simply copy the script into a `.py` file):

   ```bash
   git clone https://github.com/your-username/devops-automation-python.git
   cd devops-automation-python
   ```

   OR

   You can create a new `.py` file with the following content.

2. **Save the script as** `devops_automation.py`.

---

## How to Use

1. Open a terminal/command prompt.
2. Navigate to the folder where the script is saved.
3. Run the script using the following command:

   ```bash
   python3 devops_automation.py
   ```

4. The script will:
   - Check if the directory `/tmp/devops_test` exists. If not, it will create it.
   - Check if the file `example.txt` exists in that directory. If not, it will create it and write initial content.
   - Monitor the file for changes. It will notify you if the file is modified.

### Example Output

```bash
Directory '/tmp/devops_test' not found. Creating it now...
File 'example.txt' not found. Creating it now...
Monitoring changes in 'example.txt'...
```

After the initial setup, the script will continue running, checking for any modifications to `example.txt`. If you manually change the content of `example.txt`, the script will detect this and print:

```bash
File 'example.txt' has been modified!
```

---

## Script Explanation

### 1. **Directory and File Setup**

```python
directory = "/tmp/devops_test"
file_name = "example.txt"
file_path = os.path.join(directory, file_name)
```
- **directory**: Specifies the path where the directory will be created (`/tmp/devops_test`).
- **file_name**: Specifies the name of the file to be created (`example.txt`).
- **file_path**: Combines the directory and file name to get the full path of the file.

### 2. **Checking and Creating Directory**

```python
if not os.path.exists(directory):
    print(f"Directory '{directory}' not found. Creating it now...")
    os.makedirs(directory)
else:
    print(f"Directory '{directory}' already exists.")
```
- The script checks if the directory `/tmp/devops_test` exists using `os.path.exists()`.
- If the directory doesn't exist, it creates the directory using `os.makedirs()`.

### 3. **Checking and Creating File**

```python
if not os.path.exists(file_path):
    print(f"File '{file_name}' not found. Creating it now...")
    with open(file_path, "w") as file:
        file.write("This is the initial content of the file.")
else:
    print(f"File '{file_name}' already exists.")
```
- The script checks if the file `example.txt` exists in the `/tmp/devops_test` directory.
- If the file doesn't exist, it creates the file and writes initial content to it.

### 4. **Monitoring the File for Changes**

```python
def monitor_file():
    print(f"Monitoring changes in '{file_name}'...")
    last_modified_time = os.path.getmtime(file_path)

    while True:
        current_modified_time = os.path.getmtime(file_path)
        if current_modified_time != last_modified_time:
            print(f"File '{file_name}' has been modified!")
            last_modified_time = current_modified_time
        time.sleep(2)
```
- The `monitor_file()` function monitors the file for changes.
- It uses `os.path.getmtime()` to get the last modified time of the file and compares it with the previous check.
- If the file is modified, the script prints a message and updates the last modified time.
- The script checks the file every 2 seconds using `time.sleep(2)` to prevent continuous file access and reduce CPU load.

### 5. **Starting the Monitoring Process**

```python
monitor_file()
```
- The `monitor_file()` function is called to start monitoring the file for any changes.

---

## Extensions & Improvements

This basic script can be extended or improved in several ways:

1. **Error Handling**: Add exception handling for cases where the directory or file path is invalid.
2. **Customizable Path**: Allow the user to input the directory and file path at runtime.
3. **Trigger Actions**: Instead of just monitoring the file, you could trigger specific actions (e.g., restart a service, deploy a build) when the file changes.
4. **Advanced File Monitoring**: Use libraries like `watchdog` for more efficient and robust file monitoring, which is better suited for production environments.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

### Additional Notes

- The script uses basic Python libraries (`os` and `time`) to perform file operations and monitor changes.
- You can modify the `directory` and `file_name` variables to suit your needs.
- The script runs indefinitely to monitor file changes. To stop it, simply interrupt the execution (Ctrl+C in most terminals).

