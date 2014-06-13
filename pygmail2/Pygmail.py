#!/usr/bin/python3

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

    def sendConfirmation(self, to_addr, subject, text):
        msg = MIMEText(text, 'html')
        msg['Subject'] = subject
        msg['To'] = to_addr
        try:
            conn = SMTP('smtp.gmail.com')
            # conn.set_debuglevel(True)
            conn.login(self.gaccount, self.gpass)
            try:
                conn.sendmail(self.gaccount, to_addr, msg.as_string())
            finally:
                conn.close()
        except Exception as exc:
            sys.exit("Mail failed: {}".format(exc))




if __name__ == "__main__":
    htmlstr = """
    <div style="background-color: yellow">
    <img src="http://s2.lemde.fr/image/2014/06/08/534x0/4434307_7_7e9f_une-assemblee-generale-des-intermittents-du_b3fd2b267a605d9ccc9c269c00712624.jpg">
    <p><b>There is something!</b><p>
    </div>
    """
    x = Pygmail()
    x.sendConfirmation("emma.dessin.belle@gmail.com", "are you ok?", htmlstr)
