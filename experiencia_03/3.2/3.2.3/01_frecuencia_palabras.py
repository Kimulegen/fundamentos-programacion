#! Python3
# Generate a dictionary with the number of ocurrences of each word in a text

# initialize variables
word_dict = {}

# ask user for a text, split the text into a list of words
txt = input("Ingrese un texto\n> ")
txt_array = txt.split(" ")

# create dictionary
for word in txt_array:
    word_dict.setdefault(word, 0)
    word_dict[word] += 1

# show dictionary
print(word_dict)
