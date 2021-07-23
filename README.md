This is a simple python script to generate a wordlist of all possible character
combinations in a given range.

The default settings for this tool generates all possible combinations from 6-24 
characters

Once the wordlist is done generating, run hashes.py to generate MD5, SHA1, SHA256, 
and SHA512 hashes of the wordlist. This will generate files for each hash type
that can be used along with the wordlist depending on needs

Make sure to change the path of your wordlist file. For this application, I am using 
unlimited storage at opendrive.com and mounting the webdav service with davfs2.
