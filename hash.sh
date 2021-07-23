#!/bin/bash

#cat /library/UserAccount-passwords.txt > md5sum -

while read p; do
   echo "$p" | md5sum >> /library/wordlist-md5.txt
   echo "$p" | md5sum
done < /library/wordlist.txt

while read p; do
    echo "$p" | sha1sum >> /library/wordlist-sha1.txt
    echo "$p" | sha1sum
 done < /library/wordlist.txt

while read p; do
    echo "$p" | sha256sum >> /library/wordlist-sha256.txt
    echo "$p" | sha256sum
 done < /library/wordlist.txt

while read p; do
    echo "$p" | sha512sum >> /library/wordlist-sha512.txt
    echo "$p" | sha512sum
 done < /library/wordlist.txt

