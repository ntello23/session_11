# find three letter words in input.txt that start with b

puncutation = '.,?!:;\''
def find_words(file_name):
    """
    Prints three letters words starting with b from a file
    :param file_name:
    :return:
    """
    with open(file_name) as file:
        for line in file:
            for p in puncutation:
                line = line.replace(p, ' ')
            for word in line.split():
                if len(word) == 3 and word.lower()[0] == 'b':
                    print(word)
    return

find_words('input.txt')