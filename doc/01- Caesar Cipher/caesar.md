#Caesar Cipher

it  is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

## The Encryption Function

    E(x) = (x + k) mod |alphabet|
     

## The Decryption Function

    D(x) = (x - k) mod |alphabet|

## Breaking the cipher

because of the key size limitation, the attacker can try all possible shifts in a brute force attack.
another way to guess the right key is to use frequency analysis more on that in the next chapter.