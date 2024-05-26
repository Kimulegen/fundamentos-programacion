txt = input('Ingrese un texto\n> ')
word_dict = {}

txt_array = txt.split(' ')

for word in txt_array:
    word_dict.setdefault(word,0)
    word_dict[word] += 1

print(word_dict)