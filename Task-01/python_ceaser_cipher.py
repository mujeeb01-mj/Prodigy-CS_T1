letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)
# def encrpt(plaintext, key):
#     Ciphertext = ""
#     for letter in plaintext:
#         letter = letter.lower()
#         if not letter == " ":
#                 index = letters.find(letter)
#                 if index == -1:
#                     Ciphertext += letter
#                 else:
#                      new_index = index + key
#                      if new_index >= num_letters:
#                           new_index -= num_letters
#                      Ciphertext += letters[new_index]  
#     return Ciphertext 

# def decrypyt(ciphertext, key):
#     plaintext = ""
#     for letter in ciphertext:
#         letter = letter.lower()
#         if not letter == " ":
#                 index = letters.find(letter)
#                 if index == -1:
#                     plaintext += letter
#                 else:
#                      new_index = index - key
#                      if new_index < 0:
#                           new_index += num_letters
#                      plaintext += letters[new_index]  
#     return plaintext                                    

def encrypyt_decrpyt(text , mode , key ):
         result = ""
         if mode == "d":
               key = -key
         for letter in text:
             letter = letter.lower()
             if not letter == "":
                  index = letters.find (letter)
                  if index == -1:
                     result += letter
                  else: 
                     new_index = index + key 
                     if new_index >= num_letters: 
                          new_index -= num_letters
                     elif new_index < 0:
                          new_index  += num_letters
                     result += letters [new_index]
         return result           

print()
print(" Ceaser Cipher Program")
print() 

print('Do you want to encrpytor decrypt?')
user_input = input ('e/d: ').lower()
print()

if user_input == "e":
    print("Encryption mode selected")
    print()
    key = int( input("Enter the key (1 through 26):"))
    text = input("Enter the text to encrpyt:")
    Ciphertext = encrypyt_decrpyt(text,user_input, key,)
    print(f"CipherText : {Ciphertext}")
elif user_input == "d":
    print("Decryption mode selected")
    print()
    key = int( input("Enter the key (1 through 26):"))
    text = input("Enter the text to decrpyt:")
    plaintext = encrypyt_decrpyt(text,user_input,key,)
    print(f"PlainText : {plaintext}")
  