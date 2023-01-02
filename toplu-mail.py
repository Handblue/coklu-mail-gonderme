import smtplib
import email.mime.multipart
import email.mime.application
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# E-posta hesabınızın kullanıcı adı ve parolasını girin
username = 'Buraya Gmail'
password = 'Buraya Aldığınız şifre'


# Gönderilecek e-posta adreslerini bir listeye yazın
to_emails = ['shturk@outlook.com.tr', 'shturk@outlook.com.tr', 'shturk@outlook.com.tr']

# E-posta konusu ve içeriği
subject = 'Test E-posta'
body = 'Deneme Deneme Deneme'

# PDF dosyasının yolunu belirtin
filename = 'C:\\Users\\emir\\Desktop\\blabla.pdf'  #buraya dosya yolunuzu belirtin.

# E-posta mesajını oluşturun
msg = email.mime.multipart.MIMEMultipart()
msg['Subject'] = subject
msg['From'] = username
msg['To'] = ','.join(to_emails)

# PDF dosyasını ekleyin
with open(filename, 'rb') as f:
    
    pdf = email.mime.application.MIMEApplication(f.read(), _subtype='pdf')
    pdf.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(pdf)

# E-posta içeriğini ekleyin
msg.attach(email.mime.text.MIMEText(body, 'plain'))


# SMTP sunucusunu ayarlayın
smtp_server = 'smtp.gmail.com'
port = 587  # Gmail için port numarası

# SMTP bağlantısını açın
server = smtplib.SMTP(smtp_server, port)
server.ehlo()
server.starttls()
server.login(username, password)

# E-postayı gönderin
server.sendmail(username, to_emails, msg.as_string())

# Bağlantıyı kapatın
server.quit()

print('E-posta başariyla gönderildi!')

#not Türkçe karakter kullanmayınız.
