#Coded by Mike Musa

#Linkedin: https://www.linkedin.com/in/mikemusa/

#Github: https://github.com/mmusa90/Parrot


import time
from itertools import chain
import email
import imaplib
import sys,os,subprocess
import html2text

import datetime


imap_ssl_host = '10.21.0.28'  # Host SMTP IP Address

username = 'signal@10.21.0.28' # Email username
password = 'Password!23' #Email Password

n=-1 # Assign N as -1 to start 


# Restrict mail search. Be very specific.
# Machine should be very selective to receive messages.
criteria = { # Filter to filter to only receive email, subject, or body only
    
    
}
uid_max = 0



def search_string(uid_max, criteria): # Search based on those filters
    c = list(map(lambda t: (t[0], '"'+str(t[1])+'"'), criteria.items())) + [('UID', '%d:*' % (uid_max+1))]
    return '(%s)' % ' '.join(chain(*c))
    # Produce search string in IMAP format:
    #   e.g. (FROM "me@gmail.com" SUBJECT "abcde" BODY "123456789" UID 9999:*)


def get_first_text_block(msg): # Get email body
    type = msg.get_content_maintype()

    if type == 'multipart':
        for part in msg.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif type == 'text':
        return msg.get_payload()


server = imaplib.IMAP4(imap_ssl_host)#Get host config
server.login(username, password)
server.select('INBOX') #Select Inbox

result, data = server.uid('search', None, search_string(uid_max, criteria))# Save search results and filters

uids = [int(s) for s in data[0].split()]
if uids:
    uid_max = max(uids)
    # Initialize `uid_max`. Any UID less than or equal to `uid_max` will be ignored subsequently.

server.logout() # logout 

def signal():# Signal Function that will read phone numbers from phones.txt
    # file handle fh
    f = open('phones.txt')
    while True:
        line = f.readline()
    
    # in python 3
        print(line)
        if not line:
            break
        signal_msg="Message:",' ',str(dicts.get("0"))
        phone="+14242658541" # Signal Sender
        cmd=['C:\\signal-cli-0.6.2\\bin\\signal-cli.bat', '-u',phone,'send', '-m',signal_msg,"+1"+line] # CMD is a object  to run Signal CLI open source Library and send them to each member on signal
        subprocess.Popen(cmd).wait()#  module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module intends to replace several older modules and functions:                  item.
        time=datetime.datetime.now()
        print(time)
        file= open('logs.txt',"a")
        file.write('\n'+str(time)+"  Message sent to:  "+line + "\n"+"Message: "+str(signal_msg))
        file.write('\n'"===============================")




   
    
dicts = {} # Create dictonary to store emails and filter them

# Keep checking messages ...

while 1:

        
    # Have to login/logout each time because that's the only way to get fresh results.
        server = imaplib.IMAP4(imap_ssl_host)
        server.login(username, password) 
        server.select('INBOX')


        result, data = server.uid('search', None, search_string(uid_max, criteria))

        uids = [int(s) for s in data[0].split()]
        for uid in uids:
            # Have to check again because Gmail sometimes does not obey UID criterion.
            if uid > uid_max:
                result, data = server.fetch(str(uid), "(RFC822)")
                msg = email.message_from_bytes(data[0][1])
                uid_max = uid 
                text = get_first_text_block(msg) # store email body
                print ('New message :::::::::::::::::::::')
                lines = str.join(" ", text.splitlines()) # fix lines
                h = html2text.HTML2Text() # 
                # Ignore converting links from HTML
                h.ignore_links = True 
                converted=(h.handle(lines)) #Convert html to text

               
                
                keys = range(1) # Store only one email every time
                
                
                values = [converted[0:61]] # get all email till 61 chars which is full message 
                for i in keys: # we are only using key 0 and key 1
                    n+=1 # First time key will be 0 
                    if n==2:# if key reaches to 2 set it to 1 
                        n=1


                    dicts[str(n)] = values[i] # first part where will be the key in dictonary; the second part will be adding values from key which is only one
                    

                    
                       
            
            zero = dicts.get("0") # assign variable to get value from key 0
           
            one = dicts.get("1")# assign variable to get value from key 1
           
           
            
            if zero==one: # if first email and second email match then print duplicate and delete key 1

                print("duplicate and i will delete last one")
                dicts.pop("1")
                print("Duplicate")
                print("=======================================================")
                print(dicts)
                print("=======================================================")
                
                
            if zero!=one: # if they're not match means it's new email; assign the 2nd email to key 0 so it can be first email and compare 2nd email if they're match then run duplicate and delete 
                print("Not Match")
                try:
                    dicts[str(0)]=dicts[str(1)]  
                    dicts.pop("1")
                    signal()
                except:# For first time, the key 0 will be there but key 1 won't be there sometimes so this one to avoid this problem and send first email if there's no other email coming
                    print("need key one email")
                    signal()
                print("Not Match")
                print("=======================================================")
                print(dicts)
                print("=======================================================")

                
                
        



            
                
               

server.logout()
time.sleep(1)

