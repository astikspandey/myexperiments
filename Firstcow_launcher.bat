echo off








if requests.get'https://github.com/astikspandey/myexperiments/blob/main/Individual_code/MY.py'.status_code == 200:
    exec(requests.get('https://github.com/astikspandey/myexperiments/blob/main/Individual_code/MY.py').text)
else:
    print(f"Failed to fetch the file: {response.status_code}")

