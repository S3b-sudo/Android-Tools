import os
import requests

print("Android Tools Installer")
print("==================")
input("Press 'Return' to begin: ")
print("Creating virtual python environment...")
os.system("python -m venv AT")
print("==================")
print("Installing dependencies...")
os.system("source AT/bin/activate && pip install -r requirements.txt")
print("==================")
print("Making run.sh executable...")
os.system("chmod +x run.sh")
print("==================")
print("Making Folders...")
os.system("mkdir res")
os.system("mkdir apk")
print("Done")
print("==================")
print("Would you like to install scrcpy into the res folder?")
print("(1) Yes")
print("(2) No, i will do it manually")
while True:
    choice = input("Choose: ")
    if choice == "1":
        url = "https://github.com/Genymobile/scrcpy/releases/download/v4.1/scrcpy-linux-x86_64-v4.1.tar.gz"
        response = requests.get(url)
        response.raise_for_status()

        print("Downloading scrcpy V4.1...")
        with open("res/filename.tar.gz", "wb") as f:
            f.write(response.content)

        os.system("tar -xvzf res/filename.tar.gz -C res/")  

        os.system("mv res/scrcpy-linux-x86_64-v4.1 res/scrcpy")
        print("Done")
        input("Press 'Return' to quit: ")
        quit()
    if choice == "2":
        break
print("You will need to install scrcpy into the res folder on your own. See https://github.com/S3b-sudo/Android-Tools for instructions.")
input("Press 'Return' to quit: ")
quit()
