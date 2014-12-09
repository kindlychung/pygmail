#!/usr/bin/env python3

def main():
    import argparse
    import sys
    from pygmail2.Pygmail import mo

    parser = argparse.ArgumentParser("A python script for sending emails from commandline using gmail")
    parser.add_argument("--to", "-t", nargs="+", help="Recepient email address")
    parser.add_argument("--subj", "-s", help="Subject of the email", default="No subject")
    parser.add_argument("--body_file", "-b", help="You can use an html file.  Default to stdin.", default=None)
    parser.add_argument("--attach", "-a", nargs = "*", help = "Attachments")

    args = parser.parse_args()

    if args.body_file == None:
        mailbody = sys.stdin.read()
    else:
        with open(args.body_file) as readfh:
            mailbody = readfh.read()

    if args.attach == None:
        args.attach = ""

    mo.sm(args.to, args.subj, mailbody, args.attach)

if __name__ == "__main__":
    main()
