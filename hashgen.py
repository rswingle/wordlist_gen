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

md5 = open("/library/md5.txt", "a")
sha1 =  open("/library/sha1.txt", "a")
sha256 = open("/library/sha256.txt", "a")
sha512 =  open("/library/sha512.txt", "a")


with open("/data/wordlist.txt") as f:
    for line in f:
        print(compute_MD5_hash(line))
        md5.write(line)

with open("/data/wordlist.txt") as f:
    for line in f:
        print(compute_SHA1_hash(line))
        sha1.write(line)

with open("/data/wordlist.txt") as f:
    for line in f:
        print(compute_SHA256_hash(line))
        sha256.write(line)

with open("/data/wordlist.txt") as f:
    for line in f:
        print(compute_SHA512_hash(line))
        sha512.write(line)


md5.close()
sha1.close()
sha256.close()
sha512.close()
