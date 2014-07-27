#!/usr/bin/env python3

from smtplib import SMTP_SSL as SMTP
import sys
from  email.mime.text import MIMEText
import os

class Pygmail:
    def __init__(self):
        homedir = os.environ["HOME"]
        secretfile = os.path.join(homedir, ".pygmailrc")
        with open(secretfile) as secretfile_h:
            secretinfo = secretfile_h.readlines()
            secretinfo = [x.strip() for x in secretinfo]
            self.gaccount = secretinfo[0]
            self.gpass = secretinfo[1]

    def send_mail(self, to_addr, subject, text):
        msg = MIMEText(text, 'html')
        msg['Subject'] = subject
        msg['To'] = to_addr
        try:
            conn = SMTP('smtp.gmail.com')
            conn.login(self.gaccount, self.gpass)
            conn.sendmail(self.gaccount, to_addr, msg.as_string())
        except Exception as exc:
            sys.exit("Mail failed: {}".format(exc))
        finally:
            conn.close()

