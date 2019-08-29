# Parrot

Parrot is an application to send your new emails to Signal as secure text message. It also has feature to end duplicate emails. Built on Python

Thanks to AsamK, Nick Lee

Requirements:

1- You will need to download Signal-Cli Liberary:

https://github.com/AsamK/signal-cli
by:AsamK

Follow instructions for how to setup a Signal account.

2- Edit code to your email settings 

3- Install html2text link:
https://pypi.org/project/html2text/


4- Change Phone in the code to be matched with your Signal account.

phone="+14242658541" # Signal Sender

5- Change cmd location to where you downloaded Signal-CLI
cmd=['C:\\signal-cli-0.6.2\\bin\\signal-cli.bat', '-u',phone,'send', '-m',signal_msg,"+1"+line]


6- Create text file call it phones.txt and you can add phone number in this format
4242658540
2064747750

Don't worry about adding +1 which is US & Canada interational code it's already added. Change  it  to your country code if you were outside North America.

It will create logs.txt as well for all records.

Aditional features:

If you want to connect to SSL SMTP:

imap_ssl_host = 'imap.gmail.com'  # imap.mail.yahoo.com
imap_ssl_port = 993
username = 'USERNAME or EMAIL ADDRESS'
password = 'PASSWORD'


If you want to filter messages:
criteria = {
    'FROM':    'PRIVILEGED EMAIL ADDRESS',
    'SUBJECT': 'SPECIAL SUBJECT LINE',
    'BODY':    'SECRET SIGNATURE',
}


How duplicate works:

The first email will be stored in Array[0], seconed email will be stored in Array[1], it will check if they're matched or not. If they're matched 
it will send the first email. If email was different it will store in Array[0] and send it. 

So no matter how many duplicates you get it will always send one email.


For more information on how to connect emails:

https://gist.github.com/nickoala/569a9d191d088d82a5ef5c03c0690a02


HTML2text is a library to convert incoming email from HTML to Text.


https://www.linkedin.com/in/mikemusa/


