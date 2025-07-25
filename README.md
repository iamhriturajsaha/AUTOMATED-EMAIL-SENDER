# 📧Automated Email Sender

A Python-based automated email sender that reads recipient data from an Excel file and sends personalized bulk emails using SMTP. Ideal for announcements, event invitations or newsletters.

---

## 🚀 Features

- Read recipient list from an Excel file
- Compose and send personalized emails
- Secure SMTP connection using TLS
- Logs all sent and failed emails
- Modular and maintainable code

---

## 📁 Project Structure

```
AUTOMATED EMAIL SENDER
│
├── Data.xlxs                 # Excel file with recipient data       
├── email_sender.py           # Main Python script
├── README.md                 # Project documentation              
└── requirements.txt          # Python dependencies
```

---

## 📄 Excel File Format

| Email Address         | Full Name     |
|-----------------------|---------------|
| hildahumes@gmail.com  | Hilda Hummes  |
| joelrtmt@gmail.com    | Joel Rotter   |
| juliustony@gmail.com  | Julius Tony   |

Ensure the file is named `Data.xlsx`.

---

## 🔐 Setup & Usage

1. **Clone the repository**
```bash
git clone https://github.com/iamhriturajsaha/AUTOMATED-EMAIL-SENDER.git
cd AUTOMATED-EMAIL-SENDER
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Update sender credentials**
Edit `email_sender.py` and replace -
```python
SENDER_EMAIL = 'tonychelseafan@gmail.com'
PASSWORD = 'hsghdhhd89nssbs'
```

4. **Run the script**
```bash
python email_sender.py
```
---

## 📦 Dependencies
See `requirements.txt` or install manually -
```bash
pip install pandas openpyxl
```
---

## ⚠️ Security Notice

- Use an **App Password** instead of your actual Gmail password if using Gmail.
- Never commit sensitive data like passwords to public repositories.
