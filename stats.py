def get_num_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    chars = {}
    lower = text.lower()
    for l in lower:
        if l in chars:
            chars[l] += 1
        else: 
            chars[l] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sorted(chars): 
    list = []
    for char in chars:
        new_dict = {"char": char, "num": chars[char]}
        list.append(new_dict)
    list.sort(reverse=True, key=sort_on)
    return list