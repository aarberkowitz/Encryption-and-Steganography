from pathlib import *
import pyinputplus as pyip
import math
import random

def save_result_to_file(original_path, content, suffix):
    output_path = original_path.with_name(original_path.stem + suffix)
    output_path.write_text(content, encoding="utf-8")
    print(f'File saved to: {output_path}')
    return output_path


def caesar_process(file_path, key, output_suffix):
    file_path = Path(file_path)
    text = file_path.read_text(encoding="utf-8")

    result = ""
    for char in text:
        if char.isalpha():
            key_amount = key % 26
            new_char = chr(((ord(char.lower()) - ord('a') + key_amount) % 26) + ord('a'))
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char

    return save_result_to_file(file_path, result, output_suffix)



def caesar_cipher_text(file_path, key):
    return caesar_process(file_path, key, '_encrypted.enc')

def caesar_decipher_text(file_path, key):
    return caesar_process(file_path, -key, '_decrypted.txt')


def transposition_cipher(input_path):
    input_text_file = Path(input_path)
    input_string = input_text_file.read_text(encoding="utf-8")
    key_value = pyip.inputInt(prompt="Enter the value for the cipher key: ", blank=False)


    rows = key_value
    columns = math.ceil(len(input_string) / key_value)

    # make sure the input string is the right size for the matrix
    input_string = input_string.ljust(rows * columns)
    my_matrix = [["" for _ in range(columns)] for _ in range(rows)]
    index = 0
    for row in range(rows):
        for col in range(columns):
            if index < len(input_string):
                my_matrix[row][col] = input_string[index]
                index += 1
    ciphered_string = ''
    for col in range(columns):
        for row in range(rows):
            ciphered_string += my_matrix[row][col]
    # Display the matrix row by row
    for row in my_matrix:
        print(' '.join(row))

    save_result_to_file(input_path, '_encoded.enc')

def decipher_transposition(input_path):
    input_text_file = Path(input_path)
    input_string = input_text_file.read_text(encoding="utf-8")

    key_value = pyip.inputInt(prompt="Enter the value for the cipher key: ", blank=False)

    rows = key_value
    columns = math.ceil(len(input_string) / key_value)

    # make sure the input string is the right size for the matrix
    input_string.ljust(rows * columns)

    my_matrix = [["" for _ in range(columns)] for _ in range(rows)]
    index = 0
    for col in range(columns):
        for row in range(rows):
            if index < len(input_string):
                my_matrix[row][col] = input_string[index]
                index += 1

    # Display the matrix row by row
    for row in my_matrix:
        print(' '.join(row))

    decoded_string = ''
    for row in range(rows):
        for col in range(columns):
            decoded_string += my_matrix[row][col]
    print(decoded_string)

    save_result_to_file(input_path, decoded_string, "_decoded.txt")

def rsa_encryption(input_path, key):
    input_text_file = Path(input_path)
    text = input_text_file.read_text(encoding="utf-8")

    out = ""
    for char in text:
        new_char = pow(ord(char), key[0], key[1])
        out = " ".join([out, str(new_char)])

    save_result_to_file(input_path, out, "_encoded.enc")

def rsa_decryption(input_path, key):
    input_text_file = Path(input_path)
    enc_text = input_text_file.read_text(encoding="utf-8")

    out = ""
    enc_numbers = list(map(int, enc_text.split()))  # Convert space-separated string to integers
    for num in enc_numbers:
        new_char = chr(pow(num, key[0], key[1]))  # Decrypt using modular exponentiation
        out += new_char

    save_result_to_file(input_path, out, "_decoded.txt")

def rsa_key_generation():
    same_index = True
    prime_numbers = [101, 103, 107, 109, 113, 127, 131, 137,
                     139, 149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223, 227,
                     229, 233, 239, 241, 251, 257, 263, 269,
                     271, 277, 281, 283, 293, 307, 311, 313,
                     317, 331, 337, 347, 349, 353, 359, 367]
    while same_index:
        random_index1 = random.randint(0, len(prime_numbers) - 1)
        random_index2 = random.randint(0, len(prime_numbers) - 1)

        if random_index1 != random_index2:
            same_index = False

    p = prime_numbers[random_index1]
    q = prime_numbers[random_index2]

    n = p * q

    phi = (p - 1) * (q - 1)

    # Choose e, where 1 < e < phi(n) and gcd(e, phi(n)) == 1
    e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    # Compute d such that e * d ≡ 1 (mod phi(n))
    d = mod_inverse(e, phi)

    public_key = (n, e)
    private_key = (n, d)
    # return e, d, n
    return public_key, private_key

    # Function to calculate gcd


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1







# print(matrix)