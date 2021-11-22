#!/usr/bin/env python3
import re
from argparse import ArgumentParser


# Find hash in list of passwd:hash pair file
def rainbow_table_passwd_finder(path, hashed_string):
    with open(path, 'r') as file:
        check_if_match = False
        for words in file:
            # Check, if passwd:hash pair are valid, if not continue read file
            if re.match(r'\S+:\w+', words):
                # Check for match
                if words.strip('\n').split(':')[1].find(hashed_string) == 0:
                    check_if_match = True
                    print('Got a match!\n'+words)
                    break
            else:
                continue
        if not check_if_match:
            print('No match')


if __name__ == '__main__':
    # Available arguments(in cmd type -h for help)
    parser = ArgumentParser()
    parser.add_argument('-r', '--rainbow', help="Path to rainbow table /home/kali/rainbow.txt", default='', required=True)
    parser.add_argument('-w', '--word', help="SHA256/SHA512/MD5 hash (exmpl. d9bb8452...)", default='', required=True)
    args = parser.parse_args()

    # Regex to check, if input word is hash
    if re.findall(r'[A-Fa-f0-9]{32,}', args.word):
        try:
            rainbow_table_passwd_finder(args.rainbow, args.word)
        except FileNotFoundError:
            print('Not existing file or path')
    else:
        print('Not correct hash format')
