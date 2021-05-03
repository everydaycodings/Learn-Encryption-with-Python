from urllib.request import urlopen, hashlib, time

#First, get the hash from the user to get the sha1 hash to crack

md5hash = "d5aa1729c8c253e5d917a5264855eab8" # you can also use input function also just uncomment the next line of code
#md5hash = input("Enter Your String Hash: ")

non_working_dictionary = [25, 21, 24, 31, 34, 35, 36, 58, 59, 60, 78, 87]
wordlist = 0

#Second, we'll open a file full of password guesses
while True:
    wordlist += 1
    if wordlist in non_working_dictionary:
        continue
    else:
        LIST_OF_COMMON_PASSWORDS = open("passwords/{}.txt".format(wordlist), "rt", encoding="utf-8").read()

        #Third, we'll take a guess from the list of passwords we opened, and split it by line

        for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):

        #Fourth, we'll hash the guess we took from the password list so we can compare it to the hash the user gave us

            hashedGuess = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()

        #Fifth, we'll compare the hash the user gave us to the hashed version of the password guess and determine if they are equal

            if hashedGuess == md5hash:

        #Sixth, we'll tell the program what to do if the password guess matches, which is to print the current guess and quit the program.
        #We'll also tell the program what to do if the password guess don't match, which is to return to step 3 to get a new password from the list

                print("The password is ", str(guess))
                quit()
            elif hashedGuess != md5hash:
                print("Password guess ",str(guess)," does not match, trying next...")

        #In the seventh and final step, we'll tell the program what to do if we get all the way through the password list without finding a match.
        print("Password not in database, we'll get them next time.")
        try:
            print("Trying: ",wordlist + 1,".txt")
        except AttributeError:
            print("AttributeError")
        time.sleep(3)