string = input("Enter sequence of words: ")
words = string.split(' ')

amount_of_every_word = {}
for word in words:
    word_count = amount_of_every_word.get(word, 0)
    amount_of_every_word[word] = word_count + 1

longest_word = max(len(word) for word in words)

