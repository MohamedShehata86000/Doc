import requests
import requests
import random
import time
import re
#################### Colour ##############
F = '\033[1;32m' #اخضر
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
PN='\033[1;35m' #BINK
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
==============================          
<WELCOM IN SOCIAL SCRIPT BY MOHAMEED SHEHATA> 
<you will Hack website Like4Like Now
==============================     
""")
################## Staret Message #######
#Num=int(input("Enter Number You want to Repait added:>> "))
######### instagram Like #######
#######.Log In #######
####token####

######### insta.Likke #####
def Like4like():
	urlt=("https://www.like4like.org/login/")
	t=requests.get(urlt).text
	token_pattern = r'token=(.*?)"'
	token_match = re.search(token_pattern, t)
	if token_match:
	    ft = token_match.group(1)
	    print(ft)
	else:
	    print("Token not found.")	
	##############
	s = requests.Session()
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
            '34.162.190.6:8585']
 
	
	proxy = random.choice(proxy_list)
	proxies = {
   'http': proxy,
   # إضافة البروكسي الأخرى هنا
}        
	
	url="https://www.like4like.org/api/login.php"
	
	hd={
	"Host":"www.like4like.org",
	"content-length":"130",
	"accept":"application/json, text/javascript, */*; q=0.01",
	"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
	"x-requested-with":"XMLHttpRequest",
	"sec-ch-ua-mobile":"?1",
	"user-agent":"Mozilla/5.0 (Linux; Android 11; BASIC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
	"sec-ch-ua-platform":"Android",
	"origin":"https://www.like4like.org",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"cors",
	"sec-fetch-dest":"empty",
	"referer":"https://www.like4like.org/login/",
	
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
#	"cookie":"_gid=GA1.2.655652340.1676265072",
	#"cookie":"PHPSESSID=ud20gkaru0h2610gqcba6dpahf",
	#"cookie":"_gat_gtag_UA_21175192_9=1",
	#"cookie":"_ga_DVWFX221E1=GS1.1.1676265072.4.1.1676266775.0.0.0",
#	"cookie":"_ga=GA1.1.1679109111.1676127906",
	}
	data={
	
	#"time":"1676266774",
	
	"token":ft,
	
	"username":"Weka999",
	
	"password":"Weka86700@@",
	
	"recaptcha":""
	}
	r=s.post(url,headers=hd,data=data,proxies=proxies).json()
	print(r)
	#time.sleep(2)
	
	u=r['data']['url']
	#print(u)
	
	#print(r)
	
	url2="https://www.like4like.org/api/get-user-info.php"
	r2=s.get(url2).text
	
	#print(r2)
	z=s.get("https://www.like4like.org/earn-credits.php?feature=instagramlik")
	#time.sleep(2)
	url3="https://www.like4like.org/api/get-tasks.php?feature=instagramlik"
	#data for post..
	r3=s.get(url3).json()
	#time.sleep(2)
	#print(r3)
	urlp=r3["data"]["tasks"][0]["url"]
	idzad=r3["data"]["tasks"][0]["taskId"]
	idlinka=r3["data"]["tasks"][0]["idlink"]
	idclana=r3["data"]["tasks"][0]["code3"]
#	print(urlp)
#	print(idzad)
#	print(idlinka)
#	print(idclana)
	#url to.get start
	urlgetstart=f"https://www.like4like.org/api/start-task.php?idzad={idlinka}&vrsta=like&idcod={idzad}&feature=instagramlik&_=1676272662212"
	rg=s.get(urlgetstart).text
	#print(rg)
	#finlly post
	urlpost="https://www.like4like.org/api/validate-task.php"
	
	datapost={
	"url":urlp,
	
	"idzad":idzad,
	
	"idlinka":idlinka,
	
	"idclana":idclana,
	
	"cnt":"true",
	
	"vrsta":"like",
	
	"feature":"instagramlik",
	
	"addon":"false",
	
	"version":""
	
	}
	rr=s.post(urlpost,data=datapost).json()
	S=rr["success"]
	Balance=rr["data"]["credits"]
	#print(Balance)
	if S == True:
		print(f"{G}Success added Your Balance Is {Y}{Balance} from instagram Like")
	else:print(f"{R}Error please contact with Developer Mohammed Shehata")
while True:
    Like4like()
######## Facebook profile Follow ########
