import sys


def pass_crack(pass_hash, word_list):
    hashes = word_list.readlines()
    for line in hashes:
        password, hash = line.split(':')
        if hash.strip() == pass_hash:
            print("\n[+] Password Found")
            print("Password for this Hash {0} is '{1}'".format(pass_hash, password))
            sys.exit()
    else:
        print("\n[-] Password Not Found")

pass_hash = sys.argv[1]
try:
    word_list = open(sys.argv[2])
except Exception as e:
    print(e)
    sys.exit()

pass_crack(pass_hash, word_list)