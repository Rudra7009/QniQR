import pandas as pd
import qrcode
import os
import yagmail

# Create directory for storing QR codes
if not os.path.exists("QR_codes"):
    os.makedirs("QR_codes")

# Read the CSV file with participant details
data = pd.read_csv('attendees.csv')

# Email configuration
sender_email = 'csai22027@glbitm.ac.in'  # Replace with your email
password = 'scmoslvlnrdbbllw'  # Replace with your password

# Initialize yagmail
yag = yagmail.SMTP(sender_email, password)

# Function to send email
def send_email(receiver_email, name, qr_image_path):
    body = f"Hello {name},\n\nPlease find your unique QR code attached.\n\nBest regards,\nYour Team"
    yag.send(to=receiver_email, subject='Your Unique QR Code', contents=body, attachments=qr_image_path)

# Generate QR codes and send emails
for index, row in data.iterrows():
    unique_data = f"Name: {row['Name']}, Roll No: {row['Roll Number']}, UUID: {row['UUID']}"
    qr = qrcode.make(unique_data)

    # Save QR code as an image file
    qr_image_path = f"QR_codes/{row['Name']}_QR.png"
    qr.save(qr_image_path)

    # Send the QR code via email
    send_email(row['Email'], row['Name'], qr_image_path)

print("QR codes generated and emailed successfully!")
