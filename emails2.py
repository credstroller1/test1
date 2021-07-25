from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host = "smtp.office365.com"
port = 587
username = "Frank@redteam-cafe.onmicrosoft.com"
password = "uc1i*f26F&H7$kC"
from_email = Frank

msg = MIMEMultipart("alternative")
msg["Subject"] = "Hello"
msg["From"] = from_email

plain_txt = "This is good Morning"
html_txt = """\
<html>
  <head></head>
  <body>
    <p>hey!<br>
    </p>
  </body>
</html>
"""


part_1 = MIMEText(plain_txt,"plain")
part_2 = MIMEText(html_txt,"html")
msg.attach(part_1)
msg.attach(part_2)

email_conn = SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()





email_conn.quit()
