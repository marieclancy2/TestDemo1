import pathlib.Path

def count_words(allLines):
    word_count = dict()
    for line in allLines:
        messy_words = line.split(" ")
        for messy_word in messy_words:
            cleaner_word = messy_word.rstrip("""!@#$%^&*()-={}[]"';:,./?""")
            clean_word = cleaner_word.lstrip("""!@#$%^&*()-={}[]"';:,./?""")
            if clean_word in word_count:
                word_count[clean_word]+=1
            else:
                word_count[clean_word] = 1
    return word_count

def main():
    path = pathlib.Path.cwd()/'warpeace.txt'
    file = open(str(path))
    all_lines = file.readlines()
    results = count_words(all_lines)
    for word in results:
        print(f"{word} appears {results[word]} times")

if __name__ == '__main__':
    main()