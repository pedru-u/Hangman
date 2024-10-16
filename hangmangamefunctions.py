
def getword(word):
    wordlist = [x for x in word]
    return wordlist

def createlist(list,correctletters):
    xlist = ['X' for x in list]
    if correctletters:
        for letters in correctletters:    
            for index, letter in enumerate(list):
                if letters == letter:
                    xlist[index] = letter
    if xlist == list:
        return True
    stringxlist = str(xlist).replace(',',' ')
    return stringxlist

def checkletter(word,letter,correctletters,lettersattempted):
    returned = -1
    if letter in lettersattempted:
        returned = -2
        return returned
    elif letter in word:
        for index, letters in enumerate(word):
            if letter == letters:
                returned = index
                correctletters.append(letter)
    lettersattempted.append(letter)
    return returned
if __name__ == '__main__':
    word = getword('banana')
    