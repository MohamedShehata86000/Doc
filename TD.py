import requests
from my_fake_useragent import UserAgent
import time
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
print(random.choice([F, B, R, G, Y, Bl, P, C, W, PN]) + """


                                        88      a8P   88                            
                                        88    ,88'    ""                            
                                        88  ,88"                                    
                                        88,d88'       88  8b,dPPYba,    ,adPPYb,d8  
                                        8888"88,      88  88P'   `"8a  a8"    `Y88  
                                        88P   Y8b     88  88       88  8b       88  
                                        88     "88,   88  88       88  "8a,   ,d88  
                                        88       Y8b  88  88       88   `"YbbdP"Y8  
                                                                        aa,    ,88  
                                                                         "Y8bbdP"   
                                        ==============================================          
                                        <WELCOM IN SOCIAL SCRIPT BY MOHAMEED SHEHATA> 
                                        ==============================================     
""")

# 6 add member
# 8 add reaction
# 45 premium member
# 7 view
######
# 3 Instagram follow
# 1 insta like
# 2 insta view
###
# 21 YouTube subscribers
# 22 YouTube views
# 23 YouTube like

# 42 Facebook page prof follow
# 40 Facebook like
# 12 TikTok followers

# https://t.me/tasapqta3at?boost

base_url = "https://t.me/tasapqta3at/"
import requests
import re

import random
def ul():
    u=["https://t.me/tasapqta3at","https://t.me/M_S_H_VIP1"]
    url=random.choice(u)
    return url


def repeat():
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
        'id': '6',
        'version': '1.0.16',
    }

    respons = requests.get('https://ston12345.com/wp-admin/admin-ajax.php', params=params1, headers=headers1).text
    w_pattern = r'"_wpnonce" value="(.*?)"'
    w_match = re.search(w_pattern, respons)
    if w_match:
        wp = w_match.group(1)
        print(wp)
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
        'pagename': (None, ul()),
    }

    response = requests.post('https://ston12345.com/wp-admin/admin-ajax.php', params=params, headers=headers,
                             files=files).text
    if 'successfully' in response:
        print(f'{G}Your order was successfully[done]')
    else:
        print(f'{R}Your order was not successfully try later')

while True:
    try:
        repeat()
        time.sleep(120)

    except:pass
