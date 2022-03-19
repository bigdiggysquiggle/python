#!/usr/bin/env python3

import shelve

accounts = shelve.open('accounts', 'c')
print(accounts['email'])
