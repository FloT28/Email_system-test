#import Libraries 
from flask import Flask 
from flask_mail import Mail#Flask extension for sending emails
import smtplib #Simple Mail Transport Protocol client
from email.message import EmailMessage #representing email messages


app = Flask(__name__)

mail = Mail(app)

@app.route("/")
def index(): 
    msg = EmailMessage(
        subject = 'Hi there, it is Easybooking here! ', 
        sender = 'Easybooking31@gmail.com', #Must match MAIL_USERNAME #will add later once created new Gmail
        recipients = ['florence.taele@gmail.com'] #ACUTAL customer email 
    )

    msg.body = "Hi, send you this email from Flask app, let me know if you need anything!"
    mail.send(msg)
    return "Message sent!"

@app.route("/send_html_email")
def send_html_email(): 
    msg = EmailMessage(subject='HTML Email from Flask', 
                  sender='Easybooking31@gmail.com',
                  recipients=['florence.taele@gmail.com'])#add other gmail!
    msg.body = 'Hello flask message sent from Flask-mail'
    mail.send(msg)
    return 'Sent'    

if __name__ == '__main__': 
    app.run(debug=True)