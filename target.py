'''
Target game
'''
from random import randrange
from typing import List


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    bukvy = []
    for _ in range(3):
        not_final = []
        for _ in range(3):
            not_final.append(chr(randrange(97, 123)).upper())
        bukvy.append(not_final)
    return bukvy


def get_words(myfile: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    words_from_dict = []
    central = letters[4]
    with open(myfile, 'r') as spysok:
        for i in spysok.readlines():
            letters2 = letters.copy()
            i = i.lower()
            if len(i) >= 4 and central in i:
                counter = 0
                for element in i[:-1]:
                    if element not in letters2:
                        counter += 1
                    else:
                        letters2.remove(letters2[letters2.index(element)])
                if counter == 0 and len(i.lower().replace('\n', "")) >= 4:
                    words_from_dict.append(i.lower().replace('\n', ""))
    return words_from_dict


MYFILE = "en.txt"


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = []
    while True:
        try:
            vidpovid = str(input()).lower()
            if len(vidpovid) >= 4:
                user_words.append(vidpovid.lower())
        except EOFError:
            return user_words


def get_pure_user_words(user_words: List[str], letters: List[str],
                        words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    final = []
    total = []
    central = letters[4]
    # letters2 = letters.copy()
    for i in user_words:
        letters2 = letters.copy()
        if len(i) >= 4 and central in i:
            counter = 0
            for element in i:
                if element not in letters2:
                    counter += 1
                    # print(element, " not in ", letters)
                else:
                    letters2.remove(letters2[letters2.index(element)])
            if counter == 0 and len(i.lower()) >= 4:
                final.append(i.lower())
    for element in final:
        if element not in words_from_dict:
            total.append(element)
    return total


def results():
    '''
    Return result and print it into file
    '''
    first = generate_grid()
    got_from_user = get_user_words()

    with open('result.txt', 'w') as myfile2:
        myfile2.write(' '.join(get_pure_user_words(
            got_from_user, first, get_words(MYFILE, first)))+'\n')
    return get_pure_user_words(
        got_from_user, first, get_words(MYFILE, first))
