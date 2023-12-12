import sys

def readlines(filename):
    with open(filename) as file:
        return file.readlines()


def character_analysis(lines):
    new_dic = {}
    total = 0
    for line in lines:
        for character in line:
            key = character.lower()
            total += 1
            if key not in new_dic:
                new_dic[key] = 0
            new_dic[key] += 1

    new_dic = get_analsis(new_dic, total)
    return new_dic

def get_analsis(new_dic, total):
    for key, value in new_dic.items():
        new_value = round(value / total, 3)
        new_dic[key] = new_value
    return new_dic

def main(infile):
    lines = readlines(infile)
    new_dic = character_analysis(lines)
    print(new_dic)



if __name__ == '__main__':
    main(sys.argv[1])
