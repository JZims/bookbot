
book_path = "./books/frankenstein.txt"

def main():       

    # count how many times letters are used
    def count_letters(contents):
        letters = {}
        for character in contents:
            character = character.lower()
            if character in letters:
                    letters[character] += 1
            else:
                    letters[character] = 1
        letter_list = [(key, value) for key, value in letters.items()]
        letter_list.sort(key=lambda x: x[1], reverse=True)
        
        return letter_list

    with open(book_path) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        letter_count = count_letters(file_contents)

    print(f"{word_count} words found in this document.")

    for pair in letter_count:
         if pair[0].isalpha():
            print(f"The character '{pair[0]}' appeared {pair[1]} times in this document.")

 

main()