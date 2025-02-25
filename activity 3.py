sentence = input("Enter a sentence: ").lower()
print("Word Frequency: ")

words = sentence.split(' ')
dict_word = {}

for word in words:
    if word in dict_word:
        dict_word[word] += 1
    else:
        dict_word[word] = 1
print(dict_word)