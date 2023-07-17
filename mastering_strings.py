# Reverse strings
def reverse_string_recurssion(sentence):
    if sentence:
        sentence = sentence[-1] + reverse_string_recurssion(sentence[:-1])
    return sentence

def reverse_string(sentence):
    return sentence[::-1]

# Reverse words in sentences
def reverser(string1, p1 = 0, p2 = None):
    if len(string1)<2:
        return string1
    p2 = p2 or len(string1)-1
    while p1 < p2:
        string1[p1], string1[p2] = string1[p2], string1[p1]
        p1 += 1
        p2 -= 1
    return string1

def reversing_words_sentence_logic(string1):
    # First, reverse the whole sentence
    reverser(string1)
    #print(string1)
    p = 0
    start = 0
    while p < len(string1):
        if string1[p] == u"\u0020":
            #reverse the word again
            reverser(string1, start, p-1)
            print(string1)
            start = p+1
        p += 1
    # Reverse the last word
    reverser(string1, start, p-1)
    print(string1)
    return "".join(string1)

def reverse_words_brute(string):
    word, sentence = [],[]
    for character in string:
        if character != " ":
            word.append(character)
        else:
            if word:
                sentence.append("".join(word))
            word = []
    if word!= "":
        sentence.append("".join(word))
    sentence.reverse()
    return " ".join(sentence)

def reverse_words_slice(sentence):
    new_word = []
    words = sentence.split(" ")
    for word in words[::-1]:
        new_word.append(word)
    return " ".join(new_word)

if __name__ == "__main__":
    import timeit
    sentence = '123 456 789 10'
    
    # print(timeit.timeit('reverse_string_recurssion(sentence)', setup = 'from __main__ import reverse_string_recurssion, sentence'))
    # print(timeit.timeit('reverse_string(sentence)', setup = 'from __main__ import reverse_string, sentence'))

    print(reversing_words_sentence_logic(list(sentence)))
    print(reverse_words_brute(sentence))
    print(reverse_words_slice(sentence))

    # print(timeit.timeit('reversing_words_sentence_logic(list(sentence))', setup = 'from __main__ import reversing_words_sentence_logic, sentence', number = 10000))
    # print(timeit.timeit('reverse_words_brute(sentence)', setup = 'from __main__ import reverse_words_brute, sentence', number = 10000))
    # print(timeit.timeit('reverse_words_slice(sentence)', setup = 'from __main__ import reverse_words_slice, sentence', number = 10000))

