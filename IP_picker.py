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
