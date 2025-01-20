import os
import time

# Define the directory and file name
directory = "/tmp/devops_test"
file_name = "example.txt"
file_path = os.path.join(directory, file_name)

# Check if the directory exists, if not, create it
if not os.path.exists(directory):
    print(f"Directory '{directory}' not found. Creating it now...")
    os.makedirs(directory)
else:
    print(f"Directory '{directory}' already exists.")

# Check if the file exists inside the directory
if not os.path.exists(file_path):
    print(f"File '{file_name}' not found. Creating it now...")
    # Create and write some initial content to the file
    with open(file_path, "w") as file:
        file.write("This is the initial content of the file.")
else:
    print(f"File '{file_name}' already exists.")

# Function to monitor changes in the file content
def monitor_file():
    print(f"Monitoring changes in '{file_name}'...")
    last_modified_time = os.path.getmtime(file_path)  # Get the last modified time of the file

    while True:
        # Check if the file has been modified
        current_modified_time = os.path.getmtime(file_path)
        if current_modified_time != last_modified_time:
            print(f"File '{file_name}' has been modified!")
            last_modified_time = current_modified_time
        time.sleep(2)  # Wait for 2 seconds before checking again

# Call the monitor function
monitor_file()
