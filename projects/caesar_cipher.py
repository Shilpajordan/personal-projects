alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
  
  cipher_text = ""

  for letter in text:  
    position = alphabet.index(letter)
    new_position = (position + shift) % 26 # to avoid index out of range error
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

def decrypt(text,shift):
  cipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = (position - shift)%26
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

if direction == 'encode':
  encrypt(text,shift)
elif direction == 'decode':
  decrypt(text, shift)
