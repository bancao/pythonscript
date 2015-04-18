#-*-encoding:utf-8-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib


def create_message():
    msg = MIMEMultipart()
    msg['to'] = 'to'
    msg['from'] = 'from'
    msg['subject'] = 'books'
    return msg

def send_message(msg):
    try:
        server = smtplib.SMTP()
#         server.connect('smtp.qq.com')
#         server.login('email','password')
        server.sendmail(msg['from'], msg['to'],msg.as_string())
        server.quit()
        print "send success"
    except Exception, e:  
        print str(e) 

def send_book_to_kindle():
    cwd = os.getcwd()
    book_folder = cwd + "\\kindle"
    books = get_attachment(book_folder)
    msg = create_message()
    send = 1
    for book in books :
        attach = MIMEText(open(book_folder + "\\" + book, 'rb').read(), 'base64', 'gb2312')
        print 'attachment; filename="%s"' %book.decode('gb2312').encode('utf-8')
        attach["Content-Type"] = 'application/octet-stream'
        attach["Content-Disposition"] = 'attachment; filename="%s"' %book
        msg.attach(attach)
        if send % 25  == 0 or send == len(books):
            send_message(msg)
            msg = create_message()

        send = send + 1   
    
    

def get_attachment(book_folder):
    if os.path.exists(book_folder) :
        print "exist"
    else :
        os.mkdir(book_folder) 
    
    books = os.listdir(book_folder)
    return books;

if __name__ == '__main__':
    send_book_to_kindle()