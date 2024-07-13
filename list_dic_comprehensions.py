
######   list  comprehensions
my_list2 = [number for number in range(0, 101)]
my_list2

my_list3 = [number for number in range(0, 101) if number % 2 == 0]
print(my_list3)

combined = [a + b  for a in "life" for b in "study"]
print (combined)

nested = [letters[1] for letters in [a + b  for a in "life" for b in "study"]]
print(nested)

######    dictionary comprehensions
words = ["life","is","study"]
word_length_dict2 = {word:len(word) for word in words}
print(word_length_dict2)

words = ["life","is","study"]
word_lengths = [4, 2, 5]
pairs = zip(words, word_lengths)
for item in pairs:
    print (item)

words = ["life","is","study"]
word_lengths = [4, 2, 5]
word_length_dict3 = {key:value for (key, value) in zip(words, word_lengths)}
print( word_length_dict3 )

