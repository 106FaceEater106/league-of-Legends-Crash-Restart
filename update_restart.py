import os
import requests


mydir = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
mydesktop = "c:\\users\\aurora\\desktop\\"


def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))

download("https://github.com/marciomvm/league-of-Legends-Crash-Restart/releases/download/v1.1/restart_aurora.bat", dest_folder=mydir)
download("https://github.com/marciomvm/league-of-Legends-Crash-Restart/releases/download/v1.1/main.exe", dest_folder=mydesktop)

#https://github.com/marciomvm/league-of-Legends-Crash-Restart/releases/download/v1.0/Crash_Restart_V1.0.rar

