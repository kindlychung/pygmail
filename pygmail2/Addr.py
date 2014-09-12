import csv
import os
import re

class Addr:
    def __init__(self):
        homedir = os.getenv("HOME")
        configFile = os.path.join(homedir, ".pygmail", "email.csv")
        with open(configFile, "r") as fh:
            reader = csv.reader(fh)
            for row in reader:
                name = row[0]
                name = self.getkey(name)
                emailAddr = row[1]
                emailAddrKey = self.getkey(emailAddr)
                nameEmailKay = name + "_" + emailAddrKey
                setattr(self, emailAddrKey, emailAddr)
                setattr(self, nameEmailKay, emailAddr)



    def getkey(self, mystring):
        mystring = mystring.strip()
        mystring = mystring.lower()
        mystring = re.sub(r"[^a-z_]", "_", mystring)
        return mystring





ad = Addr()
