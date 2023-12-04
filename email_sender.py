from email.message import EmailMessage
import ssl
import smtplib

email_sender = "test@gmail.com"
email_password = "<input your generated password>"
email_receiver = "test@proton.me"
subject = "Testing mail sending with python"
body = """
This is just a project for sending mail with python.
"""

mail = EmailMessage()
mail["from"] = email_sender
mail["to"] = email_receiver
mail["subject"] = subject
mail.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, mail.as_string())