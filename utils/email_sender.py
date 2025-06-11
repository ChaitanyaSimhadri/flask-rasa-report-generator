import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipient_email, attachment_path=None):
    """Sends an email with an optional attachment."""
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your password

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        message.attach(part)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")
