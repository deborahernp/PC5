import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def enviar_correo():
    smtp_server = 'smtp.gmail.com'  
    smtp_port = 587  
    sender_email = 'tu_correo@gmail.com'
    sender_password = 'tu_contraseña'  
    
    receiver_email = 'destinatario@gmail.com'
    subject = 'Reporte de Procesamiento'
    body = 'Adjunto el reporte generado.'
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    file_path = './reporte1.csv'  # Ruta al archivo que quieres adjuntar
    
    with open(file_path, 'rb') as file:
        attachment = MIMEApplication(file.read(), _subtype="xlsx")
        attachment.add_header('Content-Disposition', 'attachment', filename=file_path)
        msg.attach(attachment)
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
