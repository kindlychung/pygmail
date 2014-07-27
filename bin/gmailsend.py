#!/usr/bin/env python3

import argparse 
import sys

from pygmail2.Pygmail import Pygmail


parser = argparse.ArgumentParser("A python script for sending emails from commandline using gmail")
parser.add_argument("to_addr", help="Recepient email address")
parser.add_argument("--subj", "-s", help="Subject of the email", default="No subject")
parser.add_argument("--body_file", "-b", help="Body of email")

args = parser.parse_args()

if args.body_file == None:
    mailbody = sys.stdin.read()
else:
    with open(args.body_file) as readfh:
        mailbody = readfh.read()
        
Pygmail().send_mail(args.to_addr, args.subj, mailbody)