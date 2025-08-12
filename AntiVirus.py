import os
import requests
import time
import tkinter as tk
from tkinter import filedialog

virus_total_api_key = "83cc1cd8ee63132bfe2ed2a07edaa3d30ff4a42d7c29f109c61b1649402cc173"

def iterate_files(folder_path):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isdir(full_path):
            iterate_files(full_path)
        else:
            scan_file(full_path)

def scan_file(file_path):
    response=upload_file(file_path)
    scan_id=response.get('scan_id')
    if scan_id:
        is_virus=get_report(scan_id)
        if is_virus:
            print("Virus Detected! Filepath ",file_path)
        else:
            print("{} is not virus".format(file_path))
    else:
        print("unexepected response, no scan id found for file: ", file_path)


def upload_file(file_path):

    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    params = {'apikey': virus_total_api_key}

    file_content=open(file_path,'rb')
    filename=os.path.basename(file_path)
    files = {'file': (filename, file_content)}

    response = requests.post(url, files=files, params=params)
    return response.json()

def get_report(scan_id):
    print("getting report for scan id",scan_id)
    url = 'https://www.virustotal.com/vtapi/v2/file/report'

    params = {'apikey': virus_total_api_key,  'resource': scan_id}

    response = requests.get(url, params=params)

    if not response:
        raise Exception("Unexepcted Erorr in response")
    
    if response.status_code==200: #Received good response
        response=response.json()
        if response.get('response_code') !=1: #Scan is not completed
            print("Scan not completed...")
            time.sleep(5)
            get_report(scan_id)
        else:
            return response.get("positives") >0
    elif response.status.code==204:# Received response without content
        print("Empty response...")
        time.sleep(3)
        get_report(scan_id)
    else: #Received unexpected response
        print("Received unexpected response with status code:", response.status_code)
        return False

#GUI: select folder to scan
def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    folder_selected = filedialog.askdirectory(title="Select a Folder")
    return folder_selected

if __name__ =="__main__":
    folder_path = select_folder()
    if folder_path:
        print(f"Folder selected: {folder_path}")
    else:
        print("No folder selected.")
    iterate_files(folder_path)