### Readme.md PyModEncryptDecrypt

#### Description:

This encrypt_decrypt.py script is designed to do two actions:

1. Encrypt a custom message passed to the script, provide the base64 value of the key parameter's value as a string and save the encrypted version of the message to a filename of the user's choosing.
2. Decrypt the message saved as an encrypted string within the file when the base64 string is provided as the key's parameter value and print the file's decrypted contents to standard out.

Happy encrypting and decrypting! :)

#### Modules to import:

- If you haven't already then you will need to run the following command from terminal of choice:

[Cryptography Library](https://pypi.org/project/cryptography/)


```pip3 install cryptography```

- You shouldn't have to pip install argparse as it is a standard library with Python. If for whatever reason you did not have argparse then the command would be as such below:

[ArgParse Standard Python Library](https://docs.python.org/3/library/argparse.html)


```pip3 install argparse```

#### How to install this Module with Git:

1. Open your terminal of choice on your operating system of choice.
2. Navigate your folder structure to where you want to store this module.
3. Run this command: ```git clone https://github.com/RubixSphere/PyModEncryptDecrypt.git```

#### How to install this Module without Git:

1. Click the green "Code" button in the top right of this repo.
2. Select "Download ZIP"
3. Unzip the archive and then you can run the commands listed in the usage examples below from your terminal of choice.

#### Usage examples:

##### Encrypt:

```
python .\encrypt_decrypt.py --action encrypt --message "This is my super secret message that no body should see without my base64 key" --output_file encrypted_message.txt --key NobodyWillGuessThisKey

Output: Message has been encrypted successfully, yay! Use this key as the value for the --key parameter when you want to decrypt: OGoxB0VUOGQBf8UapQVxqFKgdY5tiJmgYNFB4yaSe1g=
```

*Base64 version of key is displayed to standard out and you will use this value to decrypt in the next step*

##### Decrypt:

```
python .\encrypt_decrypt.py --action decrypt --input_file encrypted_message.txt --key OGoxB0VUOGQBf8UapQVxqFKgdY5tiJmgYNFB4yaSe1g=

Output: I decrypted the message and this is what it says:
This is my super secret message that no body should see without my base64 key
```

#### Help:

```
python.exe .\encrypt_decrypt.py -h
usage: encrypt_decrypt.py [-h] --action {encrypt,decrypt} [--input_file INPUT_FILE]
                          [--output_file OUTPUT_FILE] [--message MESSAGE] [--key KEY]

Encrypt and decrypt messages using a custom key with the Fernet library and output the
encrypted file to a custom filename

options:
  -h, --help            show this help message and exit
  --action {encrypt,decrypt}
                        Action to perform (encrypt or decrypt)
  --input_file INPUT_FILE
                        Input file path
  --output_file OUTPUT_FILE
                        Output file path
  --message MESSAGE     Message to encrypt
  --key KEY             Encryption/Decryption key
```


#### Troubleshooting:

1.

```
ValueError: Fernet key must be 32 url-safe base64-encoded bytes.

OR

binascii.Error: Incorrect padding
```

You have provided a key to the decrypt action that is not the exact base64 value printed to standard out after the encrypt command. Please copy and paste the entire base64 string from the encrypt action's print to standard out in its entirety.

2.

```
   python .\encrypt_decrypt.py --action decrypt --input_file encrypted_message.txt --key "-RiW-iwo5jCTg3w4-Ct4xALnTyDI6i0cMcVkBEr2J54="
usage: encrypt_decrypt.py [-h] --action {encrypt,decrypt} [--input_file INPUT_FILE] [--output_file OUTPUT_FILE] [--message MESSAGE] [--key KEY]
encrypt_decrypt.py: error: argument --key: expected one argument
```

If your key that is generated includes hyphens at the very beginning of the key then just regenerate that key by running the encrypt command parameters again as this causes issues parsing the key vs the arguments even if you wrap the key value in quotes. The encrypt action will generate a new key without hyphens more often than not.


#### Contributing Guidelines:

- Don't open any GitHub issues before reading the entire Readme.md and paying special attention to the troubleshooting and usage sections.
- Make sure if you have a bug or issue to report that you answer the following questions below in your report:
1. Is the issue consistently replicable?
2. At what point did the issue happen?
3. What command did you run?
4. Are all dependencies installed?
5. What operating system are you running?

#### License:

Educational assignment for Python for Networking.





