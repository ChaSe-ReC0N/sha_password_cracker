import hashlib as hlib

hs=input("Input the sha_hash to be cracked")
pass_file = input("Input the filename of password/Wordlist")
#pass_list =

def sha_1_cracker():
    hash = hs
    
    

def sha_1_gen(hs):
    sha = hlib.sha1(str(hs).encode("utf-8")).hexdigest()  
    return sha 


print("Generated sha1 hash = ",sha_1_gen(hs))