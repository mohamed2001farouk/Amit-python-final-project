def count_unique_words(words_list):
    word_frequency = {}
    
    for word in words_list:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    return word_frequency

words = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
result = count_unique_words(words)
print(result)
