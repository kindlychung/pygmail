from distutils.core import setup

import platform, os
sysname = platform.system()
if sysname == "Windows":
    binpath = os.getenv("SystemRoot")
else:
    binpath = r"/usr/local/bin"

setup(
    name = "pygmail2",
    packages = ["pygmail2"],
    version = "0.3.0",
    data_files = [(binpath, ["scripts/gmailsend.py"])],
    description = "Send mail from gmail using python",
    author = "Kaiyin Zhong",
    author_email = "kindlychung@gmail.com",
    url = "https://github.com/kindlychung/pygmail",
    keywords = ["gmail", "email"]
    )

