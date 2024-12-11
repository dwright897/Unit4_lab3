# Dalton W.
# Unit4_lab3
# File Reverse

from StackClass import ArrayStack

def cleaned_word(word):
    clean = ""
    for item in word:
        if item.isalpha():
            clean += item
    return clean

def reverse_words(input_filename, output_filename, stack):
    with open(input_filename, 'r')as filename:
        contents = filename.read()

    words = contents.split()


    for item in words:
        cleaned = cleaned_word(item)
        if len(cleaned) >0:
            stack.push(cleaned)

    reversed = []
    while len(stack) >0:
        reversed.append(stack.pop())

    with open(output_filename, 'w') as filename:
        filename.write(' '.join(reversed))

        






def main():
    stack = ArrayStack()
    input_file = "earnest.txt"
    output_file = "earnest_reversed.txt"

    reverse_words(input_file, output_file, stack)

    print(f"Words from {input_file} have been reversed and saved to {output_file}")







if __name__ == "__main__":
    main()