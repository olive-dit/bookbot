import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  # Beendet das Programm mit Statuscode 1

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words, get_num_chars, sort_dict

if __name__ == "__main__":
    # !!! path = "/home/olive/github.com/olive-dit/bookbot/books/frankenstein.txt"
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    letter_dict = get_num_chars(text)
    letter_dict_split = sort_dict(letter_dict)


    character_report = ""
    for entry in letter_dict_split:
        if entry["character"].isalpha():
            character_report += f"{entry['character']}: {entry['count']}\n"
    
    
    #sort_dict(letter_dict)

    #Print a report
    print(f"""
        ============ BOOKBOT ============
        Analyzing book found at {sys.argv[1]}...
        ----------- Word Count ----------
        Found {num_words} total words
        --------- Character Count -------
        {character_report}
    """)
