import hashlib

string = input("Enter the string to be hashed: ")

print("============== Your Options are: sha224, sha256, sha512, sha3_256, sha1, md5 ==================")

hash = input("Enter The Hash Type: ")

if hash == "sha224":
    print(hashlib.sha224(bytes(string, 'utf-8')).hexdigest())

if hash == "sha256":
    print(hashlib.sha256(bytes(string, 'utf-8')).hexdigest())

elif hash == "sha512":
    print(hashlib.sha512(bytes(string, 'utf-8')).hexdigest())

elif hash == "sha3_256":
    print(hashlib.sha3_256(bytes(string, 'utf-8')).hexdigest())

elif hash == "sha1":
    print(hashlib.sha1(bytes(string, 'utf-8')).hexdigest())

elif hash == "md5":
    print(hashlib.md(bytes(string, 'utf-8')).hexdigest())

else:
    print("Error: Please check your hash type it may be correct or not added to this program")
    print("""As you know there are many types of hashes
        So i added some of the famous one
        You can add more if you like.. """)