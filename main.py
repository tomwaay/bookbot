import string

#dictonary of all lowercase letters
numLetter = dict.fromkeys(string.ascii_lowercase, 0)

#global
PATH = "books/frakenstien.txt"

def main():
    #open text file
    with open(PATH) as f:
        file_contents = f.read()

    #split words into array w/ no spaces to return length of list which == numWords
    numWords = countWords(file_contents.split())

    #counts the number of letters in the file and adds the count to the dictonary holding the values
    countLetters(file_contents, numLetter)

    #convert dict to list in the form of multiple smaller dicts holding info about each letter and its count in the form of:      letter: key, num: value
    countList = convert(numLetter)

    #sort to descending order on values the "num" key
    countList.sort(reverse=True, key=sort_on)
    
    #prints formatted report
    printReport(PATH, numWords, countList)


def countWords(file):    
    return len(file)

def countLetters(text, dict):
    for word in text.split():
        for letter in list(word.lower()):
            if letter in dict:
                dict[letter] += 1


def sort_on(dict):
    return dict["num"]

def convert(dict):
    main = []
    for entry in dict:
        new = {}
        new["letter"] = entry
        new["num"] = dict[entry]
        main.append(new)
    return main

def printReport(pathSTR, wordCount, letterCounts):
    print(f"--- Begin report of {PATH} ---")
    print(f"{wordCount} words found in the document")
    for count in letterCounts:
        print(f"The '{count["letter"]}' character was found {count["num"]} times")
    print("--- End Report ---")

main()