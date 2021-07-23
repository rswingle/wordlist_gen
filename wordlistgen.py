#!/usr/bin/env python3

##Generate a complete wordlist of all
##possible combinations of characters combinations
##from 6-24 characters
#

import itertools

chrs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_=+{[}]\|;:,<.>/?`~!@#$%^&*()'

f = open("/library/wordlist.txt", "a")

for x in range(6,32):
	for xs in itertools.product(chrs, repeat=x):
		f.writelines(xs)
		f.write("\n")
		print(xs)

f.close()
