import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

# ---------- CONFIGURATION ----------
SMTP_SERVER = 'smtp.gmail.com'
PORT = 587
LOG_FILE = 'logs/email_log.txt'
EMAIL_FILE_PATH = 'Data.xlsx'
EMAIL_SUBJECT = 'Invitation:: FAMILY NOVEMBER MEETING AT 4pm'
EMAIL_TEMPLATE = '''
Greetings {name},

A kind reminder to join our November family meeting. You can find information about this meeting below.

Topic: FAMILY NOVEMBER MEETING
Time: Feb 01 (Tuesday), 2022

Join Zoom Meeting
https://zoom.us/j/98889865931?pwd=SmJJfhrgyfghdshgdf

Meeting ID: 678 867 900
Passcode: 0000001

Looking forward to see you today, cheers

Regards
'''

# ---------- MAIN EMAIL SENDING FUNCTION ----------
def send_bulk_emails(sender_email, sender_password):
    try:
        # Load recipient data
        if EMAIL_FILE_PATH.endswith('.csv'):
            df = pd.read_csv(Data.xlsx)
        else:
            df = pd.read_excel(Data.xlsx)

        required_columns = {'Full name', 'Email Address'}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Input file must contain the following columns: {required_columns}")

        if 'Custom Message' not in df.columns:
            df['Custom Message'] = ''  # Optional column fallback

        recipients = df.to_dict('records')

        # Set up SMTP connection
        server = smtplib.SMTP(SMTP_SERVER, PORT)
        server.starttls()
        server.login(sender_email, sender_password)

        os.makedirs('logs', exist_ok=True)
        with open(LOG_FILE, 'a') as log:
            for recipient in recipients:
                try:
                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = recipient['Email Address']
                    msg['Subject'] = EMAIL_SUBJECT

                    body = EMAIL_TEMPLATE.format(
                        name=recipient['Full name'],
                        custom_message=recipient.get('Custom Message', '')
                    )

                    msg.attach(MIMEText(body, 'plain'))
                    server.sendmail(sender_email, recipient['Email Address'], msg.as_string())

                    status = 'SUCCESS'
                except Exception as e:
                    status = f'FAILED: {str(e)}'

                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log.write(f"{timestamp} - {recipient['Email Address']} - {status}\n")

        server.quit()
        print("Emails sent. Check logs/email_log.txt for details.")

    except Exception as e:
        print(f"Error: {e}")


# ---------- ENTRY POINT ----------
if __name__ == '__main__':
    sender = input("Enter sender email: ")
    password = input("Enter app password: ")
    send_bulk_emails(sender, password)