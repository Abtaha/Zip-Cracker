from zipfile import ZipFile


# Loops over given list till password is found
def check(password_list):
    for password in password_list:
        try:
            with ZipFile(zip_file) as zf:
                zf.extractall(pwd=bytes(password,'utf-8'))
            print("[INFO] CRACKED")
            print("Password:", password)
            return
        except:
            continue
    
    print("[INFO] PASSWORD NOT FOUND IN WORDLIST")



# Titles
print("-" * 60)
print(" " * 23, "ZIP CRACKER")
print("-" * 60)
print()


# Takes Inputs
zip_file = input("Enter the zip file to be cracked: ")
wordlist = input("Enter the wordlist to be used for cracking: ")
print()



#! FILE HANDLING
file = open(wordlist, "r")

# Reads every line from worldlist and formats it
password_list = [a.replace("\n", "") for a in file.readlines()]
check(password_list)

# Cleanly Exit
file.close()