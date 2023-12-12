import sys
import random
import string

def create_dic(alphabet):
    new_dic = {}
    values = random.sample(alphabet, len(alphabet))
    keys = alphabet
    for key, value in zip(keys, values):
        new_dic[key] = value
    return new_dic

def get_format(cipher):
    new_lines = []
    for key, value in cipher.items():
        new_lines.append((f'{key},{value}\n'))
    return new_lines

def writelines(filename, content):
    with open(filename, 'w') as file:
       file.writelines(content)

def main(outfile):
    alphabet = string.ascii_lowercase
    cipher = create_dic(alphabet)
    format_cipher = get_format(cipher)
    writelines(outfile, format_cipher)



if __name__ == '__main__':
    main(sys.argv[1])
