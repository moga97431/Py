#Code #By #Mohamed #Salah
#Telegram:https://ch4kacript
try:
	import requests
	import json,time,sys,os
	from user_agent import generate_user_agent
except:
	import os
	os.system('pip install request')
	os.system('pip install tim')
	os.system('pip install sys')
	os.system('pip install user_agent')
def login(user,pas):
	
	url = "https://faucetearner.org/api.php"
	
	params = {
	  'act': "login"
	}
	
	payload = json.dumps({
	  "email": user,
	  "password": pas
	})
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://faucetearner.org",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://faucetearner.org/login.php",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': "show_nt1=1; reg=1; googtrans=/en/ar; googtrans=/en/ar; show_wnt=1"
	}
	
	response = requests.post(url, params=params, data=payload, headers=headers)
	try:
		ok=(response.headers['Set-Cookie'])
		users=(ok.split('user=')[1].split(';')[0])
		return users
	except:
		return 'Error User Or Pass'
def run(user):

	
	url = "https://faucetearner.org/api.php"
	
	params = {
	  'act': "get_faucet"
	}
	
	payload = json.dumps({})
	
	headers = {
	  'User-Agent': generate_user_agent(),
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://faucetearner.org",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://faucetearner.org/faucet.php",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': user
	}
	
	response = requests.post(url, params=params, data=payload, headers=headers)
	
	
	
	
	url = "https://faucetearner.org/api.php"
	
	params = {
	  'act': "faucet"
	}
	
	payload = json.dumps({})
	
	headers = {
	  'User-Agent': generate_user_agent(),
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://faucetearner.org",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://faucetearner.org/faucet.php",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': user
	}
	
	response = requests.post(url, params=params, data=payload, headers=headers)
	
	return response.text

user=('moga97431@gmail.com')
pas=('iGXMi6-V8f%XaVP')
log=login(user,pas)
if 'Error' in log:
	print('Username And Password Error :) ')
else:
	while True:

		li=f"googtrans=/en/ar; googtrans=/en/ar; login=1; user={log}; show_nt1=1"
		res=run(li)
		try:
			re=res.split("class='text-info fs-2'>")[1].split('<')[0]
			animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%",f"Done Get: {re}"]
			for i in range(len(animation)):
			   time.sleep(1)
			   sys.stdout.write("\r[+] Lodaing... " + animation[i % len(animation)])
			   sys.stdout.flush()
		except:
			print('Error Wait Please')
		
