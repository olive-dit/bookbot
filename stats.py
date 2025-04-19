def get_num_words(text):
    num_words = 0
    words = text.split()
    for word in words:
        num_words += 1
    return num_words
    #print(f"{num_words} words found in the document")


# Diese Funktion schreibt den Text klein und fügt einzigartige Buchstaben und dessen Anzahl in ein Dictionary ein.

def get_num_chars(text):
    letters = text.lower()
    letter_dict = {}
    for letter in letters:
        if letter not in letter_dict:
            letter_dict[letter] = 0
        letter_dict[letter] += 1
    return letter_dict
    

# Diese Funktion teilt das Dictionary in mehrere und sortiert sie anschließend.
def sort_dict(letter_dict):
    letter_dict_split = []
    for a, b in letter_dict.items():
        letter_dict_split.append({"character": a, "count": b})
    
    letter_dict_split.sort(key=lambda x: x["count"], reverse=True)
    #print(letter_dict_split)
    return letter_dict_split

#sorted_letters = sort_dict(letter_dict)