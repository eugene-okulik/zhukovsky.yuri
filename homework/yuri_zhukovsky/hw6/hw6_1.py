text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

words = text.split()
modified_words = []

for word in words:
    if ',' in word:
        word = word.replace(',', 'ing,')
    elif '.' in word:
        word = word.replace('.', 'ing.')
    else:
        word += 'ing'
    modified_words.append(word)

print(' '.join(modified_words))
