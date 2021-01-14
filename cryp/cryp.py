import hashlib
import sys

def main():
    f = open("info", "r")
    h = f.read()
    g = h.split("\n")
    mdp = "fc2298f491eac4cff95e7568806e088a901c904cda7dd3221f551e5b89b3c3aa"
    salt = "5UA@/Mw^%He]SBaU"

    for i in g:
        i = i + salt
        b = hashlib.sha256(i.encode('utf-8'))
        b = b.hexdigest()
        if b == mdp:
            print(i)
            sys.exit(0)




main()