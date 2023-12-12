import sys
import string

def readlines(filename):
    with open(filename) as file:
        return file.readlines()

def get_dic(cipher):
    cipher_dic = {}
    for line in cipher:
        line = line.strip().split(',')
        cipher_dic[line[1]] = line[0]
    return cipher_dic

def cipher_stuff(cipher, input_text):
    lower_alphabet = string.ascii_uppercase
    upper_alphabet = string.ascii_lowercase
    output_text = []
    for line in input_text:
        new_line = []
        for character in line:
            if character.islower():
                new_character = cipher[character]
                new_line.append(new_character.lower())
            elif character.isupper():
                new_uppercase = cipher[character.lower()]
                new_line.append(new_uppercase.upper())
            else:
                new_line.append(character)
        output_text.append(''.join(new_line))
    return output_text



def writelines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)

def main(infile, input_text, outfile):
    cipher = readlines(infile)
    cipher_dic = get_dic(cipher)
    input_text = readlines(input_text)
    new_text = cipher_stuff(cipher_dic, input_text)
    writelines(outfile, new_text)



if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
