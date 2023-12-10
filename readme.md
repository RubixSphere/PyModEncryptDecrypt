### Readme.md PyModEncryptDecrypt

#### Description:

This encrypt_decrypt.py script is designed to do two actions:

1. Encrypt a message passed to the script, provide the base64 key string and save it to a file.
2. Decrypt the message saved as an encrypted string within the file when the base64 string is provided and print the file's decrypted contents to standard out.

Happy encrypting! :)

#### Modules to import:

- If you haven't already then you will need to run the following command from terminal of choice:

```pip3 install cryptography```

- You shouldn't have to pip install argparse as it is a standard library with Python. If for whatever reason you did not have argparse then the command would be as such below:

```pip3 install argparse```

#### Usage examples:

##### Encrypt:

```python .\encrypt_decrypt.py --action encrypt --message "This is my super secret message that no body should see without my base64 key" --output_file encrypted_message.txt --key NobodyWillGuessThisKey```

```Output: Message has been encrypted successfully, yay! Use this key as the value for the --key parameter when you want to decrypt: OGoxB0VUOGQBf8UapQVxqFKgdY5tiJmgYNFB4yaSe1g=```

* Base64 version of key is displayed to standard out and you will use this value to decrypt in the next step *

##### Decrypt:

```python .\encrypt.py --action decrypt --input_file encrypted_message.txt --key OGoxB0VUOGQBf8UapQVxqFKgdY5tiJmgYNFB4yaSe1g=```

```Output: I decrypted the message and this is what it says:```
```This is my super secret message that no body should see without my base64 key```



#### Troubleshooting:


