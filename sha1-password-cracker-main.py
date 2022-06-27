import hashlib as hlib

def sha_1_cracker(hs):
    hash = hs  

def sha_1_gen(hs):
    sha = hlib.sha1(str(hs).encode("utf-8")).hexdigest()  
    return sha 

ch = input("1. to generate a hash\n2.to crack password")

if (ch == "1"):#hash generation
    hs=input("Input the string to be hashed\n")    
    print("Generated sha1 hash = ",sha_1_gen(hs))

elif(ch=="2"):
    hs=input("Input the hash to be cracked\n")
    stri = input("Enter the string\n")
    #pass_file = input("Input the filename of password/Wordlist")
    #pass_list =
    sha_ge = sha_1_gen(stri)

    if(sha_ge== hs):
        print (f"password is = {stri}")

    else:
        print("Wrong password")
 
else:
    print("Wrong Choice")
    
