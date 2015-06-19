#!/usr/bin/env python
import sys

guitars = [ 
    {'es335': 'Xtra Large'},
    {'les paul': 'Large'},
    {'sg': 'Medium-Large'},
    {'stratocaster': 'Medium'},
    {'telecaster': 'Medium-Small'},
    {'baby taylor': 'Small'}
]

users_guitars = []
line = None
while line != 'done':
    line = raw_input("Enter a guitar (type 'done' to finish): ")
    if line != 'done':
        users_guitars.append(line)

for g in guitars:
    for u in users_guitars:
        if u.lower() in g:
            print "%s = %s" % (u, g[u.lower()])

