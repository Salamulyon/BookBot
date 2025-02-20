
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        text_count = {}
        words = file_contents.split()
        for word in words:
            for letter in word:
                if letter.lower() not in text_count:
                    text_count[letter.lower()] = 1
                else:
                    text_count[letter.lower()] += 1
        for key,value in text_count.items():
            if key.isalpha():
                print(f"The '{key}' character was found {value} times")

main()
