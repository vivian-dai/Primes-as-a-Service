from dotenv import load_dotenv
import os
import requests
import smtplib
import ssl

load_dotenv()

sender = 'primesasaservice@gmail.com'
password = 'qywumbvmssinpnhr'
# Get these from server
reciever = 'mmmzzz66g@gmail.com'
start = 181
end = 190

api_key = os.environ('api_key')
prime = requests.get(f"https://lpdet4.deta.dev/genprimebtwn?a={start}&b={end}&apikey={api_key}")

body_msg = f'''Subject: Your Prime
Thank you for purchasing your prime with Primes As A Service. 
Your Prime is: {prime}'''

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as server:
    server.login(sender, password)
    server.sendmail(sender, reciever, body_msg)