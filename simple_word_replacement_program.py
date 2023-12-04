def replace_word():
    str = "hi, how are you?"
    word_to_replace = input("Please input a word you want to replace: ")
    word_replacement = input("Please input the replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()