#!/usr/bin/env python3

import shelve
import getpass

accounts = shelve.open('accounts', 'c')
print("enter email address:")
accounts['email'] = input()
accounts['email_pw'] = getpass.getpass('enter password:')
accounts.close
