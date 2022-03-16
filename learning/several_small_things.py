#!/usr/bin/env python3

set1 = ['pea', 'nut', 'butt', 'er']

if 'pea' in set1:
    print('peaaaaaaaa')

if 'plop' not in set1:
    print('lol')

print(set1.index('butt'))

set1.insert(2, '-')
print(set1)

set1.remove('-')
print(set1)

set2 = [5, 4, 3, 2, 1]
print(set2)
set2.sort()
print(set2)
set2.sort(reverse=True)
print(set2)

set3 = ['a', 'z', 'A', 'Z']
print(set3)
set3.sort(key=str.lower)
print(set3)
