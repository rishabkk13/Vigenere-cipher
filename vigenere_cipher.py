def new_alph(ch):
    ch = ch.lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_alph = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alph
    
   
def encrypt(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1 :
                res += new[alph.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += new[alph.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1    
    return res
    
    
def decrypt(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1 :
                res += alph[new.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += alph[new.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1    
    return res    

exit_loop = 'y'
while(exit_loop=='y'):
    print('\n|-------------------------------------|')
    print("\nWelcome to Vigenere Cipher!\n\nPress 1 to Enrypt a message \nPress 2 to Decrypt a message")
    choice=int(input("\nEnter your choice: "))
    #print('\n|-------------------------------------|\n')
    if choice==1:
        text1 = input('\nEnter message to be encrypted: ')
        key = input('Enter key: ')
        if key.isalpha():
            if len(key) <= len(text1):
                big_key = key * (len(text1) // len(key)) + key[:len(text1) % len(key)]
                text_encrypt = encrypt(text1, big_key)
                print('\nEncryption:\n') 
                print('Your text:',text1)
                print('Key: ',key)
                print('\nEncoded Message:',text_encrypt)
            else:
                print('ERROR: Length of key cannot be greater than length of text! ')
        else:
            print("ERROR: Key is to be a character word! ")


    if choice==2:
        text_to_dec = input('\nEnter message to be decrypted: ')
        key = input('Enter key: ')
        if key.isalpha():
            if len(key) <= len(text_to_dec):
                big_key = key * (len(text_to_dec) // len(key)) + key[:len(text_to_dec) % len(key)]
                text_decrypt = decrypt(text_to_dec, big_key)
                print('\nDecrption:\n')
                print('Text:',text_to_dec)
                print('Key : ',key)
                print('\nDecoded message: ' + text_decrypt)
            else:
                print('ERROR: Length of key cannot be greater than length of text! ')
        else:
            print("ERROR: Key is to be a character word! ")

    print('\n|-------------------------------------|\n')
    print('Do you want to run the program again?(y/n)')
    exit_loop = input('Your choice: ')