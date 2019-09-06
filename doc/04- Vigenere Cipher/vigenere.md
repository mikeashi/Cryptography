# Vigenere Cipher


The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution.

## The Encryption Function

 E(x_i) = (x_i + k_i) mod |alphabet|
 
 ## The Decryption Function
 
 D(x_i) = (x_i - k_i) mod |alphabet|
 
 ## Keyspace size
 
 |alphabet|^|key|