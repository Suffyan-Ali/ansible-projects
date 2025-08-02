import os
import smtplib
import ssl
from email.message import EmailMessage
from glob import glob

# Configuration
sender_email = "your_email@example.com"
receiver_email = "manager@example.com"
password = "your_app_password"
subject = "Daily Server Report"

# Find latest CSV file in reports/
list_of_files = glob('reports/*.csv')
latest_file = max(list_of_files, key=os.path.getctime)

# Email setup
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content("Please find attached the daily server report.")

with open(latest_file, 'rb') as f:
    file_data = f.read()
    file_name = os.path.basename(latest_file)

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender_email, password)
    server.send_message(msg)

print("✅ Report emailed successfully!")
