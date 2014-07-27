# Description

This is a very simple package that enables you to send mail through gmail using python. It's not a big deal, it does not read your emails, no calendars, no drafts...
It does just one thing, sending emails.

# Requirements

* Python 3
* pip3 for installation

# Install

pip3 install --upgrade git+https://github.com/kindlychung/pygmail.git

# Security

It uses smtp, that's all. You can always check the source code, of course


# Usage

## From a interactive python shell or from any python file:

    from pygmail2.Pygmail import Pygmail
    Pygmail().send_mail('u@domain.net', 'hi, there', '<b>important stuff </b>')

## Using the `gmailsend`
