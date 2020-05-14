## What is a Vigenere Cipher?  
Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets .The encryption of the original text is done using the Vigenère square or Vigenère table
1) The table consists of the alphabets written out 26 times in different rows, each alphabet shifted cyclically to the left compared to the previous alphabet, corresponding to the 26 possible Caesar Ciphers.
2) At different points in the encryption process, the cipher uses a different alphabet from one of the rows.
3) The alphabet used at each point depends on a repeating keyword  

### Some important features of these codes:
1) vigenere_cipger.py works only on alphabets, and not on numbers and special characters
2) The 'cipher key' isn't case sensitive
3) Normal text/cipher text is case sensitive
4) matrix.py is just a fun program that simulates ideally all possible permutations to create the encryption/decryption matrix
