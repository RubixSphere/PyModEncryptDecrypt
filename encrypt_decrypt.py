import argparse # https://docs.python.org/3/library/argparse.html
from cryptography.fernet import Fernet # https://pypi.org/project/cryptography/

# If you haven't already then you will need to run the following command from terminal of choice: pip3 install cryptography
# You shouldn't have to pip install argparse as it is a standard library with Python.

##########################################################################################################################################################################
### This script is designed to do two actions: ###
### 1. Encrypt a message passed to the script, provide the base64 key string and save it to a file. ###
### 2. Decrypt the message saved as an encrypted string within the file when the base64 string is provided and print the file's decrypted contents to standard out. ###
### Happy encrypting! :) ###
##########################################################################################################################################################################

# Called by the main() function to take the user's provided message and encrypt it using the cryptogography -
# module with its Fernet class to the file name that a user provides. The file will be stored in the root of this script's folder.

def write_encrypted_msg(file_path, msg):
    key = Fernet.generate_key()
    cipher_mod = Fernet(key)
    encrypted_msg = cipher_mod.encrypt(msg.encode())

    with open(file_path, 'wb') as file:
        file.write(encrypted_msg)
    
    return key

# Called by the main() function to decrypt the encrypted message.

def read_encrypted_msg(file_path, key):
    cipher_mod = Fernet(key)

    with open(file_path, 'rb') as file:
        encrypted_msg = file.read()

    decrypted_msg = cipher_mod.decrypt(encrypted_msg).decode()
    return decrypted_msg

# Parse the arguments and pass them to the script.

def main():
    parser = argparse.ArgumentParser(description='Encrypt and decrypt messages using a custom key with the Fernet library and output the encrypted file to a custom filename')
    parser.add_argument('--action', choices=['encrypt', 'decrypt'], required=True, help='Action to perform (encrypt or decrypt)')
    parser.add_argument('--input_file', help='Input file path')
    parser.add_argument('--output_file', help='Output file path')
    parser.add_argument('--message', help='Message to encrypt')
    parser.add_argument('--key', help='Encryption/Decryption key')

    args = parser.parse_args()

# Encrypt action error handling:

    if args.action == 'encrypt':
        if not args.message or not args.output_file:
            parser.error('When you are encrypting, make sure to provide values for the parameters --message and --output_file')

# Encrypt action successful:
        
        key = write_encrypted_msg(args.output_file, args.message)
        print(f'Message has been encrypted successfully, yay! Use this key as the value for the --key parameter when you want to decrypt: {key.decode()}')

# Decrypt action error handling:

    elif args.action == 'decrypt':
        if not args.input_file or not args.key:
            parser.error('When you are decrypting, make sure to provide values for the parameters --input_file and --key. The --key value should be sourced from the terminal output of the encrypt command.')

# Decrypt action successful:

        decrypted_msg = read_encrypted_msg(args.input_file, args.key.encode())
        print(f'I decrypted the message and this is what it says:\n{decrypted_msg}')

# Run the main() function of the script only if the script is executed directly and -
# not if it's imported as another module into another python script:

if __name__ == "__main__":
    main()
