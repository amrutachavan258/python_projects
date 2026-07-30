from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position=(position+shift_amount)%26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"New value is: {cipher_text}")

def decrypt(original_text, shift_amount):
    normal_text = ""
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position-shift_amount)%26
            normal_text += alphabet[new_position]
        else:
            normal_text += char
    print(f"New value is: {normal_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Invalid input")


    again=input(f"Do you want to continue Type 'yes' or 'no': \n").lower()

    if again != "yes":
        print("Goodbye!!!")
        break

