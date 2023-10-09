#!/usr/bin/python3
for n in range(97, 123):
    if not (n in (101, 113)):
        print('{}'.format(chr(n)), end='')
