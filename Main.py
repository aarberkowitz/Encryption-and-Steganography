import pyinputplus as pyip
from pathlib import *
from steganography import *
from ciphers_and_encryption import *
from test import rsa_key_generation


def encrypt_file_menu():
    encryption = pyip.inputMenu(choices=['Caesar', 'Transposition', 'RSA', 'Return to Main Menu', 'Exit'],
                                prompt='Which encryption method would you like to use?\n', numbered=True)
    if encryption == 'Return to Main Menu':
        return True
    if encryption == 'Exit':
        return False
    while True:
        try:
            input_path = pyip.inputFilepath(prompt='Enter the path for the file you wish to encrypt, or write back or exit: ', mustExist=True)
            if input_path == 'back' or input_path == 'Back':
                return True
            if input_path == 'exit' or input_path == 'Exit':
                return False
            text = Path(input_path)
            assert text.suffix == '.txt'
            break
        except AssertionError:
            print("Error: input an existing text file")


    # Caesar parameter:
    if encryption == 'Caesar':
        key = pyip.inputInt(prompt='How many letters over would you like to move: ', min=1, max=25)
        caesar_cipher_text(input_path, key)
    # Transposition key
    elif encryption == 'Transposition':
        transposition_cipher(input_path)
    # RSA Keys
    elif encryption == 'RSA':
        key_gen = pyip.inputYesNo(prompt="do you need to generate an RSA key? yes/no ")
        if key_gen == 'yes':
            rsa_key_public, rsa_key_private = rsa_key_generation()
            print(f"your public and private keys are: public: {rsa_key_public} private: {rsa_key_private}")
            rsa_encryption(input_path, rsa_key_public)
        else:
            rsa_key = input("enter your RSA key pair: ")
            rsa_encryption(input_path, rsa_key)

    return True


def decrypt_file_menu():
    encryption = pyip.inputMenu(choices=['Caesar', 'Transposition', 'RSA', 'Return to Main Menu', 'Exit'],
                                prompt='Which encryption method would you like to use?\n', numbered=True)

    if encryption == 'Return to Main Menu':
        return True
    if encryption == 'Exit':
        return False
    while True:
        try:
            input_path = pyip.inputFilepath(prompt='Enter the path for the file you wish to encrypt, or write back or exit: ', mustExist=True)
            if input_path == 'back' or input_path == 'Back':
                return True
            if input_path == 'exit' or input_path == 'Exit':
                return False
            text = Path(input_path)
            assert text.suffix == '.enc'
            break
        except AssertionError:
            print("Error: input an existing .enc file")

    # Caesar parameter:
    if encryption == 'Caesar':
        key = pyip.inputInt(prompt='How many letters over would you like to move: ', min=1, max=25)
        caesar_decipher_text(input_path, key)
    # Transposition key
    elif encryption == 'Transposition':
        decipher_transposition(input_path)
    # RSA Keys
    elif encryption == 'RSA':
        key_gen = pyip.inputYesNo(prompt="do you need to generate an RSA key? \n yes/no ")
        if key_gen == 'yes' or key_gen == 'y':
            rsa_key_public, rsa_key_private = rsa_key_generation()
            print(f"your public and private keys are: public: {rsa_key_public} private: {rsa_key_private}")
        else:
            rsa_key_private = input("enter your private key as a tuple: ")
        rsa_decryption(input_path, rsa_key_private)
    return True


def hide_message_menu():
    while True:
        try:
            image_path = pyip.inputFilepath(
                prompt='Enter the filepath of the image you want to enter a message into, or write back or exit: ', mustExist=True)
            if image_path == 'back' or image_path == 'Back':
                return True
            if image_path == 'exit' or image_path == 'Exit':
                return False
            image = Path(image_path)
            assert image.suffix == '.png' or image.suffix == '.jpg'
            break
        except AssertionError:
            "Error: enter an existing image"
    while True:
        try:
            text_path = pyip.inputFilepath(prompt='Enter the filepath of the text you want to insert in the image: ',
                                           mustExist=True)
            text = Path(text_path)
            assert text.suffix == '.txt'
            break
        except AssertionError:
            print("Error: enter an existing text file")

    embed_message_in_image(image_path, text_path)
    return True


def extract_message_menu():
    while True:
        try:
            image_path = pyip.inputFilepath(
                prompt='Enter the filepath of the image you want to extract a message from, or write back or exit: ', mustExist=True)
            if image_path == 'back' or image_path == 'Back':
                return True
            if image_path == 'exit' or image_path == 'Exit':
                return False
            image = Path(image_path)
            assert image.suffix == '.png' or image.suffix == '.jpg'
            break
        except AssertionError:
            print("Error: enter an existing image")

    extract_message_from_image(image_path)
    return True


def exit_program():
    return False


def main():
    running = True
    while running:
        first_menu = pyip.inputMenu(choices=['Encrypt a Text File', 'Decrypt a Text File', 'Hide a message in an image',
                                             'Extract a message in an image', 'Exit'],
                                    prompt='What would you like to do? \n', numbered=True)
        # encryption menu
        if first_menu == 'Encrypt a Text File':
            running = encrypt_file_menu()

        # chose decrypt a file
        elif first_menu == 'Decrypt a Text File':
            running = decrypt_file_menu()
        # chose Hide a message in picture
        elif first_menu == 'Hide a message in an image':
            running = hide_message_menu()
        # chose Extract a message in picture
        elif first_menu == 'Extract a message in an image':
            running = extract_message_menu()
        elif first_menu == 'Exit':
            running = exit_program()


main()
