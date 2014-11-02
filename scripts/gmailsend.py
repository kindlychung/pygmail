#!/usr/bin/env python3

import argparse
import sys

from pygmail2.Pygmail import mo


parser = argparse.ArgumentParser("A python script for sending emails from commandline using gmail")
parser.add_argument("to_addr", help="Recepient email address")
parser.add_argument("--subj", "-s", help="Subject of the email", default="No subject")
parser.add_argument("--body_file", "-b", help="Body of email")
parser.add_argument("--attach", "-a", nargs = "*", help = "Attachments")

args = parser.parse_args()

if args.body_file == None:
    mailbody = sys.stdin.read()
else:
    with open(args.body_file) as readfh:
        mailbody = readfh.read()

if args.attach == None:
    args.attach = ""

mo.sm(args.to_addr, args.subj, mailbody, args.attach)
