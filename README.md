## Description

This is a very simple package that enables you to send mail through gmail using python. It's not a big deal, it does not read your emails, no calendars, no drafts...
It does just one thing, sending emails.

## Requirements

* Python 3
* pip3 for installation

## Install

**I recommend using the github repository, it's more up-to-date.**

### Using `setup.py`

    git clone https://github.com/kindlychung/pygmail.git
    cd pygmail
    python3 setup.py install

You can copy the `gmailsend.py` script to a folder in your `$PATH`, for example:

    sudo cp bin/gmailsend.py /usr/local/bin/

### Using pip:

    pip3 install --upgrade git+https://github.com/kindlychung/pygmail.git

As far as I know pip will not take care of the script files in `bin/`.


## Security

It uses smtp, that's all. You can always check the source code, of course


## Usage

### From a interactive python shell or from any python file:

    from pygmail2.Pygmail import Pygmail
    Pygmail().send_mail('u@domain.net', 'hi, there', '<b>important stuff </b>')

### Using the `gmailsend.py` in shell

    gmailsend.py -h
    usage: A python script for sending emails from commandline using gmail
           [-h] [--subj SUBJ] [--body_file BODY_FILE] to_addr

    positional arguments:
      to_addr               Recepient email address

    optional arguments:
      -h, --help            show this help message and exit
      --subj SUBJ, -s SUBJ  Subject of the email
      --body_file BODY_FILE, -b BODY_FILE

* Write up your mail body in the shell in a interactive fashion:

    gmailsend.py your@email.org -s hi_there

* Pipe your mail body to the script:

    echo "<b>hi, how are you?</b>" | gmailsend.py your@email.org -s hi_there

* Load the mail body with a html file:

    wget www.google.com -O body.html
    gmailsend.py your@email.org -s hi_there -b body.html
