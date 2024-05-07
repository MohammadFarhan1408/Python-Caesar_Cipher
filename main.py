import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(art.logo)


def caesar(text_str, shift_num, caesar_direction):
    text_encrypt = ""
    if caesar_direction == 'encode':
        shift_num *= 1
    if caesar_direction == 'decode':
        shift_num *= -1
    for char in text_str:
        if char in alphabet:
            index = alphabet.index(char)
            new_position = (index + shift_num) % len(alphabet)
            text_encrypt += alphabet[new_position]
        else:
            text_encrypt += char
    print(text_encrypt)


function_continue = True
while function_continue:
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt: ")
    text = input("Type your message : ").lower()
    shift = int(input("Type the shift number: "))

    caesar(text_str=text, shift_num=shift, caesar_direction=direction)
    user_permission = input("Do you want to restart this function type 'Yes' or 'No' : ").lower()
    if user_permission == "no":
        function_continue = False
