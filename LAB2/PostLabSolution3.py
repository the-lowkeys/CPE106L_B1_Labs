"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

global articles, nouns, verbs, prepositions

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")


def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def getWords():
    articlesList = nounsList = verbsList = prepositionsList = []

    # Articles    
    readerKey = open('articles.txt', 'r')
    temporaryList = readerKey.read()
    temporaryList = temporaryList.split(sep='\n')
    temporaryList.pop(-1)

    articlesList.extend(list(articles))
    articlesList.extend(temporaryList)
    articlesList = tuple(articlesList)
    readerKey.close()

    # Nouns
    readerKey = open('nouns.txt', 'r')
    temporaryList = readerKey.read()
    temporaryList = temporaryList.split(sep='\n')
    temporaryList.pop(-1)

    nounsList.extend(temporaryList)
    nounsList.extend(list(articles))
    nounsList = tuple(nounsList)
    readerKey.close()

    # Verbs
    readerKey = open('verbs.txt', 'r')
    temporaryList = readerKey.read()
    temporaryList = temporaryList.split(sep='\n')
    temporaryList.pop(-1)

    verbsList.extend(list(articles))
    verbsList.extend(temporaryList)
    verbsList = tuple(verbsList)
    readerKey.close()

    # Prepositions
    readerKey = open('prepositions.txt', 'r')
    temporaryList = readerKey.read()
    temporaryList = temporaryList.split(sep='\n')
    temporaryList.pop(-1)

    prepositionsList.extend(list(articles))
    prepositionsList.extend(temporaryList)
    prepositionsList = tuple(prepositionsList)
    readerKey.close()

    # Return Statment
    
    return [articlesList, nounsList, verbsList, prepositionsList]

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


# Preempt loading of Word Lists
hell = getWords()
articles = hell[0]
nouns = hell[1]
verbs = hell[2]
prepositions = hell[3]

# The entry point for program execution
if __name__ == "__main__":
    main()

