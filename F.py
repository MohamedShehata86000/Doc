import requests
import requests
import random
import time
import re
from my_fake_useragent import UserAgent
x=UserAgent(family="chrome")
U=x.random()
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
	
	url="https://www.like4like.org/api/login.php"
	
	hd={
	"Host":"www.like4like.org",
	"content-length":"130",
	"accept":"application/json, text/javascript, */*; q=0.01",
	"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
	"x-requested-with":"XMLHttpRequest",
	"sec-ch-ua-mobile":"?1",
	"user-agent":U,
	"sec-ch-ua-platform":"Android",
	"origin":"https://www.like4like.org",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"cors",
	"sec-fetch-dest":"empty",
	"referer":"https://www.like4like.org/login/",
	
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
#	"cookie":"_gid=GA1.2.655652340.1676265072",
#	"cookie":"PHPSESSID=ud20gkaru0h2610gqcba6dpahf",
#	"cookie":"_gat_gtag_UA_21175192_9=1",
#	"cookie":"_ga_DVWFX221E1=GS1.1.1676265072.4.1.1676266775.0.0.0",
#	"cookie":"_ga=GA1.1.1679109111.1676127906",
	}
	data={
	
	#"time":"1676266774",
	
	"token":ft,
	
	"username":"Samaka999",
	
	"password":"Ss86700@@",
	
	"recaptcha":""
	}
	r=s.post(url,headers=hd,data=data,).json()
	
	u=r['data']['url']
	#print(u)
	
	#print(r)
	
	url2="https://www.like4like.org/api/get-user-info.php"
	r2=s.get(url2).text
	#print(r2)
	z=s.get("https://www.like4like.org/earn-credits.php?feature=instagramlik")
	url3="https://www.like4like.org/api/get-tasks.php?feature=instagramlik"
	#data for post..
	r3=s.get(url3).json()
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
######## Facebook profile Follow ########
def Like4likepf():
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
	
	url="https://www.like4like.org/api/login.php"
	
	hd={
	"Host":"www.like4like.org",
	"content-length":"130",
	"accept":"application/json, text/javascript, */*; q=0.01",
	"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
	"x-requested-with":"XMLHttpRequest",
	"sec-ch-ua-mobile":"?1",
	"user-agent":U,
	"sec-ch-ua-platform":"Android",
	"origin":"https://www.like4like.org",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"cors",
	"sec-fetch-dest":"empty",
	"referer":"https://www.like4like.org/login/",
	
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
#	"cookie":"_gid=GA1.2.655652340.1676265072",
#	"cookie":"PHPSESSID=ud20gkaru0h2610gqcba6dpahf",
#	"cookie":"_gat_gtag_UA_21175192_9=1",
#	"cookie":"_ga_DVWFX221E1=GS1.1.1676265072.4.1.1676266775.0.0.0",
#	"cookie":"_ga=GA1.1.1679109111.1676127906",
	}
	data={
	
	#"time":"1676266774",
	
	"token":ft,
	
	"username":"Samaka999",
	
	"password":"Ss86700@@",
	
	"recaptcha":""
	}
	r=s.post(url,headers=hd,data=data,).json()
	
	u=r['data']['url']
	#print(u)
	
	#print(r)
	
	url2="https://www.like4like.org/api/get-user-info.php"
	r2=s.get(url2).text
	#print(r2)
	p=s.get("https://www.like4like.org/earn-credits.php?feature=facebookusersub")
	url3="https://www.like4like.org/api/get-tasks.php?feature=facebookusersub"
	#data for post..
	r3=s.get(url3).json()
	urlp=r3["data"]["tasks"][0]["url"]
	idzad=r3["data"]["tasks"][0]["taskId"]
	idlinka=r3["data"]["tasks"][0]["idlink"]
	idclana=r3["data"]["tasks"][0]["code3"]
#	print(urlp)
#	print(idzad)
#	print(idlinka)
#	print(idclana)
	#url to.get start
	urlgetstart=f"https://www.like4like.org/api/start-task.php?idzad={idlinka}&vrsta=follow&idcod={idzad}&feature=facebookusersub&_=1676316019136"
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
	
	"vrsta":"follow",
	
	"feature":"facebookusersub",
	
	"addon":"false",
	
	"version":""
	
	}
	rr=s.post(urlpost,data=datapost).json()
	S=rr["success"]
	Balance=rr["data"]["credits"]
	#print(Balance)
	if S == True:
		print(f"{G}Success added Your Balance Is {Y}{Balance} From Facebook profile follow")
	else:print(f"{R}Error please contact with Developer Mohammed Shehata")
################ FaceBook page follow ######
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
	
	url="https://www.like4like.org/api/login.php"
	
	hd={
	"Host":"www.like4like.org",
	"content-length":"130",
	"accept":"application/json, text/javascript, */*; q=0.01",
	"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
	"x-requested-with":"XMLHttpRequest",
	"sec-ch-ua-mobile":"?1",
	"user-agent":U,
	"sec-ch-ua-platform":"Android",
	"origin":"https://www.like4like.org",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"cors",
	"sec-fetch-dest":"empty",
	"referer":"https://www.like4like.org/login/",
	
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
#	"cookie":"_gid=GA1.2.655652340.1676265072",
#	"cookie":"PHPSESSID=ud20gkaru0h2610gqcba6dpahf",
#	"cookie":"_gat_gtag_UA_21175192_9=1",
#	"cookie":"_ga_DVWFX221E1=GS1.1.1676265072.4.1.1676266775.0.0.0",
#	"cookie":"_ga=GA1.1.1679109111.1676127906",
	}
	data={
	
	#"time":"1676266774",
	
	"token":ft,
	
	"username":"Samaka999",
	
	"password":"Ss86700@@",
	
	"recaptcha":""
	}
	r=s.post(url,headers=hd,data=data,).json()
	
	u=r['data']['url']
	#print(u)
	
	#print(r)
	
	url2="https://www.like4like.org/api/get-user-info.php"
	r2=s.get(url2).text
	#print(r2)
	f=s.get("https://www.like4like.org/earn-credits.php?feature=facebooksub")
	url3="https://www.like4like.org/api/get-tasks.php?feature=facebookusersub"
	#data for post..
	r3=s.get(url3).json()
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
	urlch="https://www.like4like.org/checkurl.php"
	dch={"url":urlp}
	ch=s.post(urlch)
	urlgetstart=f"https://www.like4like.org/api/start-task.php?idzad={idlinka}&vrsta=follow&idcod={idzad}&feature=facebookusersub&_=1676314617814"
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
	
	"vrsta":"follow",
	
	"feature":"facebookusersub",
	
	"addon":"false",
	
	"version":""
	
	}
	rr=s.post(urlpost,data=datapost).json()
	S=rr["success"]
	Balance=rr["data"]["credits"]
	#print(Balance)
	if S == True:
		print(f"{G}Success added Your Balance Is {Y}{Balance} facebook page follow")
	else:print(f"{R}Error please contact with Developer Mohammed Shehata")	
###########insta comment###
def Like4likeic():
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
	
	url="https://www.like4like.org/api/login.php"
	
	hd={
	"Host":"www.like4like.org",
	"content-length":"130",
	"accept":"application/json, text/javascript, */*; q=0.01",
	"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
	"x-requested-with":"XMLHttpRequest",
	"sec-ch-ua-mobile":"?1",
	"user-agent":U,
	"sec-ch-ua-platform":"Android",
	"origin":"https://www.like4like.org",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"cors",
	"sec-fetch-dest":"empty",
	"referer":"https://www.like4like.org/login/",
	
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	"cookie":"_gid=GA1.2.655652340.1676265072",
	#"cookie":"PHPSESSID=ud20gkaru0h2610gqcba6dpahf",
#	"cookie":"_gat_gtag_UA_21175192_9=1",
#	"cookie":"_ga_DVWFX221E1=GS1.1.1676265072.4.1.1676266775.0.0.0",
#	"cookie":"_ga=GA1.1.1679109111.1676127906",
	}
	data={
	
	#"time":"1676266774",
	
	"token":ft,
	
	"username":"Samaka999",
	
	"password":"Ss86700@@",
	
	"recaptcha":""
	}
	r=s.post(url,headers=hd,data=data,).json()
	
	u=r['data']['url']
	#print(u)
	
	#print(r)
	
	url2="https://www.like4like.org/api/get-user-info.php"
	r2=s.get(url2).text
	#print(r2)
	c=s.get("https://www.like4like.org/earn-credits.php?feature=instagramcom")
	url3="https://www.like4like.org/api/get-tasks.php?feature=instagramcom"
	#data for post..
	r3=s.get(url3).json()
	urlp=r3["data"]["tasks"][0]["url"]
	idzad=r3["data"]["tasks"][0]["taskId"]
	idlinka=r3["data"]["tasks"][0]["idlink"]
	idclana=r3["data"]["tasks"][0]["code3"]
#	print(urlp)
#	print(idzad)
#	print(idlinka)
#	print(idclana)
	#url to.get start
	urlgetstart=f"https://www.like4like.org/api/start-task.php?idzad={idlinka}&vrsta=comment&idcod={idzad}&feature=instagramcom&_=1676316972027"
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
	
	"vrsta":"comment",
	
	"feature":"instagramcom",
	
	"addon":"false",
	
	"version":""
	
	}
	rr=s.post(urlpost,data=datapost).json()
	S=rr["success"]
	Balance=rr["data"]["credits"]
	#print(Balance)
	if S == True:
		print(f"{G}Success added Your Balance Is {Y}{Balance} instagrm comment")
	else:print(f"{R}Error please contact with Developer Mohammed Shehata")		
####### instagram Follow #####
def Like4likeif():
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
	
	url="https://www.like4like.org/api/login.php"
	
	hd={
	"Host":"www.like4like.org",
	"content-length":"130",
	"accept":"application/json, text/javascript, */*; q=0.01",
	"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
	"x-requested-with":"XMLHttpRequest",
	"sec-ch-ua-mobile":"?1",
	"user-agent":U,
	"sec-ch-ua-platform":"Android",
	"origin":"https://www.like4like.org",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"cors",
	"sec-fetch-dest":"empty",
	"referer":"https://www.like4like.org/login/",
	
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
#	"cookie":"_gid=GA1.2.655652340.1676265072",
#	"cookie":"PHPSESSID=ud20gkaru0h2610gqcba6dpahf",
#	"cookie":"_gat_gtag_UA_21175192_9=1",
#	"cookie":"_ga_DVWFX221E1=GS1.1.1676265072.4.1.1676266775.0.0.0",
#	"cookie":"_ga=GA1.1.1679109111.1676127906",
	}
	data={
	
	#"time":"1676266774",
	
	"token":ft,
	
	"username":"Samaka999",
	
	"password":"Ss86700@@",
	
	"recaptcha":""
	}
	r=s.post(url,headers=hd,data=data,).json()
	
	u=r['data']['url']
	#print(u)
	
	#print(r)
	
	url2="https://www.like4like.org/api/get-user-info.php"
	r2=s.get(url2).text
	#print(r2)
	iF=s.get("https://www.like4like.org/earn-credits.php?feature=instagramfol")
	url3="https://www.like4like.org/api/get-tasks.php?feature=instagramfol"
	#data for post..
	r3=s.get(url3).json()
	urlp=r3["data"]["tasks"][0]["url"]
	idzad=r3["data"]["tasks"][0]["taskId"]
	idlinka=r3["data"]["tasks"][0]["idlink"]
	idclana=r3["data"]["tasks"][0]["code3"]
#	print(urlp)
#	print(idzad)
#	print(idlinka)
#	print(idclana)
	#url to.get start
	urlgetstart=f"https://www.like4like.org/api/start-task.php?idzad={idlinka}&vrsta=follow&idcod&idcod={idzad}&feature=instagramfol&_=1676317443956"
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
	
	"vrsta":"follow",
	
	"feature":"instagramfol",
	
	"addon":"false",
	
	"version":""
	
	}
	rr=s.post(urlpost,data=datapost).json()
	S=rr["success"]
	Balance=rr["data"]["credits"]
	#print(Balance)
	if S == True:
		print(f"{G}Success added Your Balance Is {Y}{Balance} from instagram Follow")
	else:print(f"{R}Error please contact with Developer Mohammed Shehata")
############# Facebook.Share ##
def Like4likeFsh():
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
	
	url="https://www.like4like.org/api/login.php"
	
	hd={
	"Host":"www.like4like.org",
	"content-length":"130",
	"accept":"application/json, text/javascript, */*; q=0.01",
	"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
	"x-requested-with":"XMLHttpRequest",
	"sec-ch-ua-mobile":"?1",
	"user-agent":U,
	"sec-ch-ua-platform":"Android",
	"origin":"https://www.like4like.org",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"cors",
	"sec-fetch-dest":"empty",
	"referer":"https://www.like4like.org/login/",
	
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
#	"cookie":"_gid=GA1.2.655652340.1676265072",
#	"cookie":"PHPSESSID=ud20gkaru0h2610gqcba6dpahf",
#	"cookie":"_gat_gtag_UA_21175192_9=1",
#	"cookie":"_ga_DVWFX221E1=GS1.1.1676265072.4.1.1676266775.0.0.0",
#	"cookie":"_ga=GA1.1.1679109111.1676127906",
	}
	data={
	
	#"time":"1676266774",
	
	"token":ft,
	
	"username":"Samaka999",
	
	"password":"Ss86700@@",
	
	"recaptcha":""
	}
	r=s.post(url,headers=hd,data=data,).json()
	
	u=r['data']['url']
	#print(u)
	
	#print(r)
	
	url2="https://www.like4like.org/api/get-user-info.php"
	r2=s.get(url2).text
	#print(r2)
	Fs=s.get("https://www.like4like.org/earn-credits.php?feature=facebooksha")
	url3="https://www.like4like.org/api/get-tasks.php?feature=facebooksha"
	#data for post..
	r3=s.get(url3).json()
#	print(r3)
	urlp=r3["data"]["tasks"][0]["url"]
	idzad=r3["data"]["tasks"][0]["taskId"]
	idlinka=r3["data"]["tasks"][0]["idlink"]
	idclana=r3["data"]["tasks"][0]["code3"]
#	print(urlp)
#	print(idzad)
#	print(idlinka)
#	print(idclana)
	#url to.get start
	urlgetstart=f"https://www.like4like.org/api/start-task.php?idzad={idlinka}&vrsta=shareposta&idcod={idzad}&feature=facebooksha&_=1676386168076"
	rg=s.get(urlgetstart).text
#	uc="https://www.like4like.org/checkurl.php"
#	dc={"url":urlp}
#	z=s.post(uc,data=dc).text
#	print(z)
	#print(rg)
	#finlly post
	urlpost="https://www.like4like.org/api/validate-task.php"
	
	datapost={
	"url":urlp,
	
	"idzad":idzad,
	
	"idlinka":idlinka,
	
	"idclana":idclana,
	
	"cnt":"true",
	
	"vrsta":"shareposta",
	
	"feature":"facebooksha",
	
	"addon":"false",
	
	"version":""
	
	}
	rr=s.post(urlpost,data=datapost).json()
	S=rr["success"]
	Balance=rr["data"]["credits"]
	#print(Balance)
	if S == True:
		print(f"{G}Success added Your Balance Is {Y}{Balance} From Facebook Share")
	else:print(f"{R}Error please contact with Developer Mohammed Shehata")
############ TikTok Like #####		
def Like4likeTL():
	urlt=("https://www.like4like.org/login/")
	t=requests.get(urlt).text
	token_pattern = r'token=(.*?)"'
	token_match = re.search(token_pattern, t)
	if token_match:
	    ft = token_match.group(1)
	    print(ft)
	else:
	    print("Token not found.")	
	s = requests.Session()
	
	url="https://www.like4like.org/api/login.php"
	
	hd={
	"Host":"www.like4like.org",
	"content-length":"130",
	"accept":"application/json, text/javascript, */*; q=0.01",
	"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
	"x-requested-with":"XMLHttpRequest",
	"sec-ch-ua-mobile":"?1",
	"user-agent":U,
	"sec-ch-ua-platform":"Android",
	"origin":"https://www.like4like.org",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"cors",
	"sec-fetch-dest":"empty",
	"referer":"https://www.like4like.org/login/",
	
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
#	"cookie":"_gid=GA1.2.655652340.1676265072",
#	"cookie":"PHPSESSID=ud20gkaru0h2610gqcba6dpahf",
#	"cookie":"_gat_gtag_UA_21175192_9=1",
#	"cookie":"_ga_DVWFX221E1=GS1.1.1676265072.4.1.1676266775.0.0.0",
#	"cookie":"_ga=GA1.1.1679109111.1676127906",
	}
	data={
	
	#"time":"1676266774",
	
	"token":ft,
	
	"username":"Samaka999",
	
	"password":"Ss86700@@",
	
	"recaptcha":""
	}
	r=s.post(url,headers=hd,data=data,).json()
	
	u=r['data']['url']
	#print(u)
	
	#print(r)
	
	url2="https://www.like4like.org/api/get-user-info.php"
	r2=s.get(url2).text
	#print(r2)
	Tl=s.get("https://www.like4like.org/earn-credits.php?feature=tiktoklike")
	url3="https://www.like4like.org/api/get-tasks.php?feature=tiktoklike"
	#data for post..
	r3=s.get(url3).json()
#	print(r3)
	urlp=r3["data"]["tasks"][0]["url"]
	idzad=r3["data"]["tasks"][0]["taskId"]
	idlinka=r3["data"]["tasks"][0]["idlink"]
	idclana=r3["data"]["tasks"][0]["code3"]
#	print(urlp)
#	print(idzad)
#	print(idlinka)
#	print(idclana)
	#url to.get start
	urlgetstart=f"https://www.like4like.org/api/start-task.php?idzad={idlinka}&vrsta=like&idcod={idzad}&feature=tiktoklike&_=1676383329163"
	rg=s.get(urlgetstart).text
#	uc="https://www.like4like.org/checkurl.php"
#	dc={"url":urlp}
#	z=s.post(uc,data=dc).text
#	print(z)
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
	
	"feature":"tiktoklike",
	
	"addon":"false",
	
	"version":""
	
	}
	rr=s.post(urlpost,data=datapost).json()
	S=rr["success"]
	Balance=rr["data"]["credits"]
	#print(Balance)
	if S == True:
		print(f"{G}Success added Your Balance Is {Y}{Balance} From TikTOk Like")
	else:print(f"{R}Error please contact with Developer Mohammed Shehata")
	
			
						
												
while True:
	try:
		Like4likeif()
			
	except:
		print("NO chance in Instagram follow")
	time.sleep(120)		
	try:
		Like4likeic()
			
	except:
		print("NO chance in Instagram Comment")
	time.sleep(120)
	try:
		Like4likeff()
		
	except:
		print("NO chance in Face Follow")
	time.sleep(120)		
	try:
		Like4likepf()
			
	except:
		print("NO chance in Profile Follow")
	time.sleep(120)		
	try:
		Like4likeFsh()
	except:
		print("NO chance in Facebook Share")
	time.sleep(120)							
	try:
		Like4likeTL()
	except:
		print("NO chance in TikTOK Share")
	time.sleep(120)
	try:
		Like4like()
	except:
		print("No chance in Like")
		
			
				
						
#while True:
#		try:
#			Like4likeif()
#			Like4likeic()
#			Like4likeff()
#			Like4likepf()
#			Like4like()
#			print(f"{G}waiting 1 second for avoide Ban....")
#		except:
#			print(f"{R}Sorry No Chance avalbiale trying....")
#		#time.sleep(3)
#		

