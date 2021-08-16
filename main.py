import requests
import win32clipboard
import time
import sys
import os
import json
import webbrowser

name = ""
password = ""
clipboard = win32clipboard

def upload(file):
    url = "https://api.streamable.com/upload"
    # assert os.path.isfile((file))
    vid_file = {'file': open(file, 'rb')}
    title = str(input("Enter video title (leave blank for video file name): "))
    print('Uploading...')
    if title == "":
        title = os.path.split(file)[1][:-4]
    headers = {"title": title}
    result = requests.post(url, auth=(name, password), files=vid_file, data=headers)
    try:
        return result.json()
    except json.decoder.JSONDecodeError:
        print("Uploading was not successful")
        print("Debug" + result + result.text)
        time.sleep(15)



result = upload(sys.argv[1])
if result["status"] == 1:
    print("Uploading was successful")
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardText("https://streamable.com/" + result["shortcode"])
    webbrowser.open(url="https://streamable.com/" + result["shortcode"], autoraise=True)
    clipboard.CloseClipboard()
else:
    print("Uploading was not successful")
    time.sleep(15)
