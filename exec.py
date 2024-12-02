import requests
import os

def download_and_execute_github_file(url, local_filename=None):
    # Download the file from the given URL
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    
    # If no local filename is provided, use the last part of the URL
    if not local_filename:
        local_filename = url.split('/')[-1]
    
    # Save the file locally
    with open(local_filename, 'w') as file:
        file.write(response.text)
    
    # Execute the file
    exec(open(local_filename).read())

    # Optionally, delete the file after execution
    os.remove(local_filename)

# Example usage:
github_url = 'https://raw.githubusercontent.com/astikspandey/myexperiments/main/Locker/calculator.py'
download_and_execute_github_file(github_url)
