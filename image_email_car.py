import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

password = "jbgpqyhzdxniuvte"
me = "patilshreyash1707@gmail.com"
you = "patilshreyash1707@gmail.com"

def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    email_body ="""<html><body><p>Accident Detected!!!!</p> <img src="ImgFileName"></img></body></html>"""
    message = MIMEMultipart('alternative',None,[MIMEText(email_body,'html')])
    message['Subject']='Test email send'
    message['From']= me
    message['To']= you
    
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    message.attach(image)
    
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(me,password)
        server.sendmail(me,you,message.as_string())
        server.quit()
        print(f'Email send:{email_body}')
    except Exception as e:
        print(f'Error in sending email: {e}')
    
    
    
    
    
    
    # img_data = open(ImgFileName, 'rb').read()
    # msg = MIMEMultipart()
    # msg['Subject'] = 'Crash Alert'
    # msg['From'] = 'patilshreyash1707@gmail.com.cc'
    # msg['To'] = 'shreyashp1707@gmail.com.cc'

    # text = MIMEText("Vehicle Crash Detected. Send HELP")
    # msg.attach(text)
    # image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    # msg.attach(image)

    # # with smtplib.SMTP('smtp.gmail.com', 587) as server:
    # #     server.starttls()
    # #     server.login("patilshreyash1707@gmail.com", "Shreyash7067@")
    # #     text = msg.as_string()
    # #     server.sendmail("patilshreyash1707@gmail.com", "shreyashp1707@gmial.com", text)
    # s = smtplib.SMTP('smtp.gmail.com', 587)
    # s.ehlo()
    # s.starttls()
    # s.ehlo()
    # s.login("patilshreyash1707@gmail.com", "jbgpqyhzdxniuvte")
    # s.sendmail("patilshreyash1707@gmail.com", "shreyashp1707@gmail.com", msg.as_string())
    # s.quit()