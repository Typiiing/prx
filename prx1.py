import requests,sys,time
import os as qamar
qamar.system('clear')
try:
  qamar.mkdir('/sdcard/All Proxy')
except:pass
lll = '''

  _____          __               _  __   ____                     
 / ___/  __ __  / /  ___   ____  | |/_/  / __/ ___   ____ ____ ___ 
/ /__   / // / / _ \/ -_) / __/ _>  <   / _/  / _ \ / __// __// -_)
\___/   \_, / /_.__/\__/ /_/   /_/|_|  /_/    \___//_/   \__/ \__/ 
       /___/                                                       

            Tool Proxy Tekal > HTTP + SOCK 4 & 5
'''

def slq():
    qamar.system('clear')
    print(lll)
    print('[1] All Proxy \n[0] Exit\n')
    ch = input('Halbzhera Dllakam : ')
    if ch =='1':
        print('Chawarwan Ba ...')
        time.sleep(5)
        url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
        heed = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': '_gcl_au=1.1.465951981.1635821014; _fbp=fb.1.1635821014329.1500779973; __gads=ID=3e5dbda65b00b1f5-226791b906cb00f8:T=1635821017:RT=1635821017:S=ALNI_MayhgJXQ2Rxee9vLBdS2c-U-GSfPA; __mmapiwsid=28dd1898-4d7a-4ab4-bd16-0d4f531c7958:a7641f7f4e2607af23f26ec18a4ab6deb13a619e; _gaexp=GAX1.2.tqbBwmT-TQi9xsRCddgDxQ.19024.2; _hjid=0be9a98c-b0eb-4756-836d-24ff5e7b13fd; _ga=GA1.2.286910088.1635821014; _gid=GA1.2.2084283645.1637539430; _gat_UA-101859787-2=1; _hjSessionUser_1142173=eyJpZCI6IjRmZDY0MTJjLTRlMTgtNTAwYy04MmRhLWNjMzJiMGRhY2ZjMCIsImNyZWF0ZWQiOjE2Mzc1Mzk0MzMxOTUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1142173=eyJpZCI6ImU2NjVlYzdiLTZlNWQtNGE1YS1iYzEwLWY4MTQ0M2UzZGQ1MSIsImNyZWF0ZWQiOjE2Mzc1Mzk0MzMyNTB9; _hjAbsoluteSessionInProgress=0; _ga_XSEQY8PG42=GS1.1.1637539428.2.1.1637539449.0',
            'Host': 'api.proxyscrape.com',
            'Referer': 'https://www.proxyscrape.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
        }
        ok = requests.get(url,headers=heed).text
        with open('/sdcard/All Proxy/Proxy.txt','a') as kk:
            kk.write(ok)
        link = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all'
        head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': '_gcl_au=1.1.465951981.1635821014; _fbp=fb.1.1635821014329.1500779973; __gads=ID=3e5dbda65b00b1f5-226791b906cb00f8:T=1635821017:RT=1635821017:S=ALNI_MayhgJXQ2Rxee9vLBdS2c-U-GSfPA; __mmapiwsid=28dd1898-4d7a-4ab4-bd16-0d4f531c7958:a7641f7f4e2607af23f26ec18a4ab6deb13a619e; _gaexp=GAX1.2.tqbBwmT-TQi9xsRCddgDxQ.19024.2; _hjid=0be9a98c-b0eb-4756-836d-24ff5e7b13fd; _ga=GA1.2.286910088.1635821014; _gid=GA1.2.2084283645.1637539430; _hjSessionUser_1142173=eyJpZCI6IjRmZDY0MTJjLTRlMTgtNTAwYy04MmRhLWNjMzJiMGRhY2ZjMCIsImNyZWF0ZWQiOjE2Mzc1Mzk0MzMxOTUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1142173=eyJpZCI6ImU2NjVlYzdiLTZlNWQtNGE1YS1iYzEwLWY4MTQ0M2UzZGQ1MSIsImNyZWF0ZWQiOjE2Mzc1Mzk0MzMyNTB9; _hjAbsoluteSessionInProgress=0; _gat_UA-101859787-2=1; _ga_XSEQY8PG42=GS1.1.1637539428.2.1.1637540722.0',
            'Host': 'api.proxyscrape.com',
            'Referer': 'https://www.proxyscrape.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
        }
        ss = requests.get(link,headers=head).text
        with open('/sdcard/All Proxy/Proxy.txt','a') as xx:
            xx.write(ss)
        ll = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all'
        hed = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': '_gcl_au=1.1.465951981.1635821014; _fbp=fb.1.1635821014329.1500779973; __gads=ID=3e5dbda65b00b1f5-226791b906cb00f8:T=1635821017:RT=1635821017:S=ALNI_MayhgJXQ2Rxee9vLBdS2c-U-GSfPA; __mmapiwsid=28dd1898-4d7a-4ab4-bd16-0d4f531c7958:a7641f7f4e2607af23f26ec18a4ab6deb13a619e; _gaexp=GAX1.2.tqbBwmT-TQi9xsRCddgDxQ.19024.2; _hjid=0be9a98c-b0eb-4756-836d-24ff5e7b13fd; _ga=GA1.2.286910088.1635821014; _gid=GA1.2.2084283645.1637539430; _hjSessionUser_1142173=eyJpZCI6IjRmZDY0MTJjLTRlMTgtNTAwYy04MmRhLWNjMzJiMGRhY2ZjMCIsImNyZWF0ZWQiOjE2Mzc1Mzk0MzMxOTUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1142173=eyJpZCI6ImU2NjVlYzdiLTZlNWQtNGE1YS1iYzEwLWY4MTQ0M2UzZGQ1MSIsImNyZWF0ZWQiOjE2Mzc1Mzk0MzMyNTB9; _hjAbsoluteSessionInProgress=0; _gat_UA-101859787-2=1; _ga_XSEQY8PG42=GS1.1.1637539428.2.1.1637541305.0',
            'Host': 'api.proxyscrape.com',
            'Referer': 'https://www.proxyscrape.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
        }
        po = requests.get(ll,headers=hed).text
        with open('/sdcard/All Proxy/Proxy.txt','a') as cc:
            cc.write(po)
            print('Proxy Save Bu La Folder > All Proxy')
    elif ch =='0':
        time.sleep(3)
        print('Darchuit ...')
        sys.exit()
    else:
        print('Halat Krd ...')
        time.sleep(3)
        slq()
slq()

            
