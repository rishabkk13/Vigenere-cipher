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
    
# Put your text
text1 = 'This is a TEST SENTance'
text_dec = 'Fhvy us g FEFZ EEAZozcr'
# Put your key 
key = 'mango'

if len(key) <= len(text1):
    big_key = key * (len(text1) // len(key)) + key[:len(text1) % len(key)]
    text_encrypt = encrypt(text1, big_key)
    text_decrypt = decrypt(text_dec, big_key)
    
    print('|Encryption:') 
    print('|Your text: "' + text1 + '"')
    print('|Your key : "' + key + '"')
    print('|Res      : ' + text_encrypt)
    print('|----------------------------|')
    print('|Decrption:')
    print('|Your text: "' + text_dec + '"')
    print('|Your key : "' + key + '"')
    print('|Res      : ' + text_decrypt)
    print('|----------------------------|\n')
else:
    print('Error: len(key)>len(text) ')