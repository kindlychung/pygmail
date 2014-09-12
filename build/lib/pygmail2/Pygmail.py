from smtplib import SMTP_SSL as SMTP
import sys
from  email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.encoders import encode_base64
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

    def send_mail(self, to_addr, subject, text, attachments = ""):
        msg = MIMEMultipart()

        if isinstance(to_addr, list) or isinstance(to_addr, tuple):
            msg['To'] = ", ".join(to_addr)
        else:
            msg["To"] = to_addr

        msg['From'] = self.gaccount
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg.attach(MIMEText(text, "html"))

        if attachments:
            for attachment in attachments:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(open(attachment, "rb").read())
                encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attachment))
                msg.attach(part)

        try:
            conn = SMTP('smtp.gmail.com')
            conn.login(self.gaccount, self.gpass)
            conn.sendmail(self.gaccount, to_addr, msg.as_string())
        except Exception as exc:
            sys.exit("Mail failed: {}".format(exc))
        finally:
            conn.close()


    def send_mail_file(self, to_addr, subject, mailfile, attachments = ""):
        with open(mailfile) as fh:
            text = fh.read()
        self.send_mail(to_addr, subject, text, attachments = "")

mo = Pygmail()