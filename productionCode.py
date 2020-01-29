#import pathlib.Path
from typing import List, Dict

def count_words(all_lines):
    word_count = dict()
    if not (type(all_lines) is list):
            return word_count
    for line in all_lines:
        messy_words = line.split(" ")
        for messy_word in messy_words:
            cleaner_word = messy_word.rstrip("""!@#$%^&*()-={}[]"';:,./?""")
            clean_word = cleaner_word.lstrip("""!@#$%^&*()-={}[]"';:,./?""")
            if clean_word in word_count:
                word_count[clean_word]+=1
            else:
                word_count[clean_word] = 1
    return word_count

# def main():
#     path = pathlib.Path.cwd()/'warpeace.txt'
#     file = open(str(path))
#     all_lines = file.readlines()
#     results = count_words(all_lines)
#     for word in results:
#         print(f"{word} appears {results[word]} times")
#
# if __name__ == '__main__':
#     main()