words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def display_item(key, value):
    print(key * value)

for item in words.items():
    display_item(*item)