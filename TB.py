import requests
from my_fake_useragent import UserAgent
import re
x = UserAgent(family="chrome")
U = x.random()
import random

#################### Colour ##############
F = '\033[1;32m'  # اخضر
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
PN = '\033[1;35m'  # BINK

def repeat():
    url = "https://t.me/boost/M_S_H_VIP1"

    headers1 = {
        'authority': 'ston12345.com',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://smmstone.com',
        'referer': 'https://smmstone.com/',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': U,
    }

    params1 = {
        'action': 'renderfreeservice',
        'id': '45',
        'version': '1.0.16',
    }

    respons = requests.get('https://ston12345.com/wp-admin/admin-ajax.php', params=params1, headers=headers1).text
    w_pattern = r'"_wpnonce" value="(.*?)"'
    w_match = re.search(w_pattern, respons)
    if w_match:
        wp = w_match.group(1)
        # print(wp)
    else:
        print("Token not found.")

    sc_pattern = r'<input type="hidden" name="shortcode" value="(.*?)"'
    sc_match = re.search(sc_pattern, respons)
    if sc_match:
        sc = sc_match.group(1)
        # print(sc)
    else:
        print("Token not found.")
    # print (response)
    ######

    headers = {
        'authority': 'ston12345.com',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',

        'origin': 'https://smmstone.com',
        'referer': 'https://smmstone.com/',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': U,
    }

    params = {
        'action': 'fsc_request_service',
    }

    files = {
        '_wpnonce': (None, wp),
        'shortcode': (None, sc),
        'pagename': (None, url),
    }

    response = requests.post('https://ston12345.com/wp-admin/admin-ajax.php', params=params, headers=headers,
                             files=files).text
    if 'successfully' in response:
        print(f'{G}Your order was successfully[done]')
    else:
        print(f'{R}Your order was not successfully try later')


from threading import Thread as t

while True:
    try:
        repeat()
    except:pass
