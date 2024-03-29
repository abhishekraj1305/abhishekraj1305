def break_words (stuff):
    """this function will break words for us."""
    words = stuff. split(' ')
    return words

def short_words(words): 
    """shorts the words."""
    return sorted(words)    

def print_first_words(words):
    """print the first word after popping it off."""
    word= words.pop(0)
    print(word)

def print_last_word(words):
    """print the last word after popping it off."""
    word = words.pop(-1) 
    print(word)

def short_sentence(sentence):
    """take in a full sentence and returns the sorted words."""
    words= break_words(sentence)
    return short_words(words)

def print_first_and_last(sentence):
    """print the first and last words of the sentence."""
    words=break_words(sentence)
    print_first_words(words)          
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then print the first and last one."""    
    words = short_sentence(sentence)
    print_first_words(words)
    print_last_word(words)
    


    

    

