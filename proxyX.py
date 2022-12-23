import os, requests, time, random

https=["https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
          "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt",
          "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt"]
http=["https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
          "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
          "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt",
          "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
          "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
          "https://www.proxy-list.download/api/v1/get?type=http",
          "https://www.proxyscan.io/download?type=http",
          "https://api.openproxylist.xyz/http.txt",
          "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
          "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
          "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
          "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
          "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt"]
socks4=["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
              "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
              "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
              "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
              "https://www.proxy-list.download/api/v1/get?type=socks4",
              "https://www.proxyscan.io/download?type=socks4",
              "https://api.openproxylist.xyz/socks4.txt",
              "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
              "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
              "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt",
              "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
              "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
              "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
              "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt"]
socks5=["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
              "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
              "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
              "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
              "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
              "https://www.proxy-list.download/api/v1/get?type=socks5",
              "https://www.proxyscan.io/download?type=socks5",
              "https://api.openproxylist.xyz/socks5.txt",
              "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
              "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
              "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
              "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
              "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
              "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt"]

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

v="1.0b"

def update():
    f="proxyX.py"
    data = requests.get(f"https://raw.githubusercontent.com/EvilGeek/ProxyX/master/{f}").text
    file = open(f, 'wb')
    file.write(bytes(data, 'utf-8'))
    clear()
    print("Updated Successfull!")
    print("Run The Script Again...")
    print("By using"+BOLD+PURPLE+" python3 proxyX.py"+END+END)
    exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getPrList(prlist):
    prdata=[]
    for api in range(0, len(prlist)-1):
        try:
            data=requests.get(prlist[api]).text.split("\n")
            for i in data:
                if i not in prdata:
                    prdata.append(i)
        except ConnectionError:
            print("Network Error")
            return []
        except KeyboardInterrupt:
            print("Bye!")
            exit()
        except Exception as e:
            print("ERROR :\n"+str(e))
            pass
            return []
    if prdata!=[]:
        return prdata
    else:
        return []


def writeToFile(pr="", filename="proxy.txt"):
    file=open(filename,'wb')
    #print(pr)
    time.sleep(10)
    file.write(bytes(pr.strip(), 'utf-8'))

def homeMenu():
    clear()
    print(BLUE+"""▒█▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀▄ ▀▀█▀▀ ▀▄▒▄▀ 
▒█░░░ █░░█ █░░█ █▀▀ █░░█ ░░█░░ ░▒█░░ 
▒█▄▄█ ▀▀▀▀ ▀▀▀░ ▀▀▀ ▀░░▀ ░░▀░░ ▄▀▒▀▄\n\n"""+END)
    print(GREEN+"Grab HTTP/HTTPS/SOCKS4/SOCKS5 Proxies Easily with CodentX Proxy Scrapper Tool.\nTG : CodentX"+END)
    print(YELLOW+"\n1. HTTP\n2. HTTPS\n3. SOCKS4\n4. SOCKS5\n5. Update\n6. About"+END)
    httpProxy=[]
    socks4Proxy=[]
    socks5Proxy=[]
    httpsProxy=[]
    while True:
        try:
            homeChoice=int(input(RED+"Enter Your Choice:    "))
            if homeChoice==1:
                clear()
                print("Getting HTTP Proxies!")
                httpProxy=getPrList(http)
                #print(httpProxy)
                print(f"Got {len(httpProxy)} Proxies")
                time.sleep(4)
                print("Saving them to http.txt")
                pr=""
                for i in httpProxy:
                    pr=pr+"\n"+i
                writeToFile(pr, "http.txt")
                clear()
                print("Done!")
                break
            elif homeChoice==2:
                clear()
                print("Getting HTTPS Proxies!")
                httpsProxy=getPrList(https)
                #print(httpsProxy)
                print(f"Got {len(httpsProxy)} Proxies")
                time.sleep(4)
                print("Saving them to https.txt")
                pr=""
                for i in httpsProxy:
                    pr=pr+"\n"+i
                writeToFile(pr, "https.txt")
                clear()
                print("Done!")
                break
            elif homeChoice==3:
                clear()
                print("Getting SOCKS4 Proxies!")
                socks4Proxy=getPrList(socks4)
                print(f"Got {len(socks4Proxy)} Proxies")
                time.sleep(4)
                print("Saving them to socks4.txt")
                pr=""
                for i in socks4Proxy:
                    pr=pr+"\n"+i
                writeToFile(pr, "socks4.txt")
                clear()
                print("Done!")
                break
            elif homeChoice==4:
                clear()
                print("Getting SOCKS5 Proxies!")
                socks5Proxy=getPrList(socks5)
                print(f"Got {len(socks5Proxy)} Proxies")
                time.sleep(4)
                print("Saving them to socks5.txt")
                pr=""
                for i in socks5Proxy:
                    pr=pr+"\n"+i
                writeToFile(pr, "socks5.txt")
                clear()
                print("Done!")
                break
            elif homeChoice==5:
                lv = requests.get("https://raw.githubusercontent.com/EvilGeek/ProxyX/master/.version").text
                if v != lv:
                    print("Update required!")
                    yORn=input("Wanna Update Now? (y/n)        ")
                    if yORn in ["yes", "y", "Y", "YES", "Yes"]:
                        update()
                    else:
                        clear()
                        print("Nope")
                    break
                else:
                    print("You are using the latest version.")
                    break
            elif homeChoice==6:
                clear()
                print(f"Version: {v}\nA tool build by Vaibhav to scarpe proxies from various sources and to save them in your system.")
                break
            else:
                print("Invalid Choice! Try again.\n")
        except ValueError:
            print("Invalid Input! Try again.\n")
        except KeyboardInterrupt:
            print("Bye!")
            exit()
        except Exception as e:
            clear()
            print("ERROR!")
            print(e)
        
homeMenu()