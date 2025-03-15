def filter_even_length_words(words):
    return list(filter(lambda x: len(x) % 2 == 0, words))



print(filter_even_length_words(["hello", "world", "python", "AI", "code"]))  
