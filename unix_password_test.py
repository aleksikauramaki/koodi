# This script can be used to test if your password is found in a password list.

import crypt

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Read a line from the linux shadow file and send the username and
# password data to the testPass function. Password data includes
# encryption method, salt, and hashed password. Google for "linux
# shadow file explained" for more details.
def main():
    with open("/etc/shadow") as passwords:
        for line in passwords.readlines():
            data = line.split(":")
            username = data[0]
            pw_data = data[1]
            pw_data_list = pw_data.lstrip("$").split("$")
            testPass(data[0], data[1])

# Read a password from a password list, encrypt it using the same
# algorithm as was used for the hashed password in the shadow file.
# Then compare the two hashes and if they match, print out the plaintext
# password and the username. If they dont match, do the same for the next
# password in the list. In case none of the passwords match, then print
# out that no password was found for the user.
def testPass(username, password_data):
    with open("password_list.txt") as dictionary:
        for word in dictionary.readlines():
            word = word.strip("\n")
            if password_data == crypt.crypt(word, password_data):
                print(bcolors.OKGREEN + '[+] The password for user "%s" is "%s"' 
                    % (username, word) + bcolors.ENDC)
                return word
        print('[-] No password found in dictionary for user "%s"' % username)

main()