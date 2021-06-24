#!/usr/bin/env python3


import hashlib

def compute_MD5_hash(string, encoding='utf-8'):
    md5_hasher = hashlib.md5()
    md5_hasher.update(string.encode(encoding))
    return md5_hasher.hexdigest()

def compute_SHA1_hash(string, encoding='utf-8'):
	sha1_hasher = hashlib.sha1()
	sh1_hasher.update(string.encode(encoding))
	return sha1_hasher.hexdigest()

def compute_SHA256_hash(string, encoding='utf-8'):
	sha256_hasher = hashlib.sha256()
	sha256_hasher.update(string.encode(encoding))
	return sha256_hasher.hexdigest()

def compute_SHA512_hash(string, encoding='utf-8'):
	sha512_hasher = hashlib.sha512()
	sha512_hasher.update(string.encode(encoding))
	return sha512_hasher.hexdigest()

hashes = open("hashes.txt", "a")

with open("wordlist.txt") as f:
    for line in f:
        print(compute_MD5_hash(line))
        hashes.write(line)

with open("wordlist.txt") as f:
    for line in f:
        print(compute_SHA1_hash(line))
        hashes.write(line)

with open("wordlist.txt") as f:
    for line in f:
        print(compute_SHA256_hash(line))
        hashes.write(line)

with open("wordlist.txt") as f:
    for line in f:
        print(compute_SHA512_hash(line))
        hashes.write(line)


hashes.close()