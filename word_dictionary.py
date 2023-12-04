from PyDictionary import PyDictionary

dictionary = PyDictionary()
while True:
    word = input("Enter a word you want to search for in the dictionary: ")
    if word == "":
        break
    print(dictionary.meaning(word))

    
