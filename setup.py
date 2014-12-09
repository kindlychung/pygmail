from setuptools import setup

setup(
    name = "pygmail2",
    packages = ["pygmail2"],
    version = "0.3.7",
    entry_points = {"console_scripts": ['gmailsend = pygmail2.sendMailScript:main']},
    description = "Send mail from gmail using python",
    author = "Kaiyin Zhong",
    author_email = "kindlychung@gmail.com",
    url = "https://github.com/kindlychung/pygmail",
    keywords = ["gmail", "email"]
    )

