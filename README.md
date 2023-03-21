# CF-Server-side-IP-picker
This is a tool designed for only Iranian users, this tool will help you get best IPs for your config from [ircf](ircf.space)

Sadly I could not find main repo so if you have any link to it please inform me.

this site picks best Cloudflare IPs based on your ISP, it's obvious to all that this domain will be banned real soon which will cause issues.

A solution to this is adding a CNAME record in your dashboard however I heard multiple times that some user can not open Cloudflare dashboard however some of IPs may work. So, it triggered my mind into developing a new script which you must run it into your server.

# How to use

This code will generate `index.html` which is basically a HTML file to preview contents on your site, this HTML file contains all IPs for specific ISP and all you need is domain so you can read it through your link.

First of all, you need to install nginx so you can run index file in your specific destination.
After installing nginx execute python code in same folder and let it run, this code will update IPs each 5 minutes, all you need is visiting your domain with that specific address and get the IP from your browser.

Here's the main code:
```
import time
import socket
import json
import time
#Open json file create name values
f = open('domains.json')
data = json.load(f)
array = []
prefix = ["mci","mtn","mkh","rtl","ast","hwb","sht","prs","mbt","ask","rsp","afn","ztl","psm"]
Name = ["HamrahAval","Irancell","Mokhaberat","Rightel","AssiTech","HighWeb","Shatel","ParsOnline","MobinNet","AndisheSabz","Respina","Afranet","Zitel","Pishgaman"]
#Make an infinite loop to run code each 5 minutes
while(True):
    #Display tip and create name value for html file
    #Since this is for website I disable print command
    for n in range(0,13):
        Output = (prefix[n] + " = " + Name[n])
        #print(Output)
    print(" ")
    #Exctract links and ping them for IP
    for i in data['addresses']:
        response=socket.gethostbyname(i)
        print(i + " = " + response)
        array.append(i)
        
    #store data in html file to show it on website    
    r_path = (r"index.html")    
    with open (r_path , 'w') as c:
        for n in range(0,13):
            Output = ("<br>" + prefix[n] + " = " + Name[n])
            c.write(Output)
        for i in data['addresses']:
            response=socket.gethostbyname(i)
            j = (i + " = " + response)
            c.write("<br>" + j)

    #store data in text file so I can recall it if needed
    t_path = (r"fixedIPs.txt")        
    with open (t_path , 'w') as d:
        for i in data['addresses']:
            response=socket.gethostbyname(i)
            j = (i + " = " + response)
            d.write("{}\n".format(j))

    time.sleep(300)        
```
