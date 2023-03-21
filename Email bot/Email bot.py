from email import message
import smtplib
import speech_recognition as sr
import pyttsx3
from  email.message import EmailMessage



listner = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()



def get_info():
    try:
        with sr.Microphone() as source:
            print('***')
            voice = listner.listen(source)
            info = listner.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('your_email_id','yourpasswd')
    email = EmailMessage()
    email['From']='senders_email'
    email['To']=receiver
    email['Subject']=subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'rick':'friend1@gmail.com',
    
}

def get_email_info():
    talk("Who do you wish to send email")
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk("What's The Subject of the email ")
    subject = get_info()
    talk('Tell me the text in Your email')
    message = input("Write Body of Your Email \n")
    talk('Your email is sent')
    talk('Do you want to send more emails?')
    send_email(receiver,subject,message)
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info
    else:
        pass


get_email_info()
    
