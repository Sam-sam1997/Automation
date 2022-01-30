import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yaml


# Web Scrabing
credentials = yaml.load(open('./credentials.yml'), Loader=yaml.FullLoader)

# Email
from Web_Scrabing import df, data_frame

print(data_frame)

# Create a secure SSL context
try:
    smtp_server = "smtp.gmail.com"
    port = credentials['host_port']  # For starttls
    sender_email = credentials['my_id']  # sender's mail id
    receiver_email = credentials['recipant_id']  # list of reciever's mail ids
    password = credentials['my_password']
    context = ssl.create_default_context()
    print('SSL run succesfully')
except Exception as e:
    print(e)
# Try to log in to server and send email
try:
    server = smtplib.SMTP(host=credentials['host_add'], port=credentials['host_port'])
    server.ehlo()
    server.starttls()
    server.login(credentials['my_id'], credentials['my_password'])
    print('Succesfully logged in')
except Exception as e:
    print(e)
# Creation of the MIMEMultipart Object
try:
    recipients = credentials['recipant_id']
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = "Top 5 Authors and Ratings"
    msg['From'] = credentials['my_id']
    msg['To'] = credentials['recipant_id']

    html = """\
  <html>
    <head></head>
    <body>
      {0}
    </body>
  </html>
  """.format(df.to_html())

    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    print('Object created')
except Exception as e:
    print(e)

# Sending email
try:
  server.send_message(msg)
  server.quit()
  print('Email sent')
except Exception as e:
  print(e)



