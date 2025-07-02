#Jeremy Durdel
#Chapter 9 and 10 Lab 2
#07/02/2025

import csv

#Main Function, takes all information and combines it
def main():
    print("File Processor")
    print()

    file_name = input("Enter the name of the file you wish to process: ")

    word_total = word_count(file_name)
    capitalized_total = capitalization(file_name)

    print(f"The file {file_name} contains {word_total} words of which "
    f"{capitalized_total} of them are capitalized.")


def word_count(file_name):
    word_count = 0

    with open(file_name, newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            #Joins fields, splits into words, counts words
            join_text = " ".join(row)
            words = join_text.split()
            word_count += len(words)

    return word_count


def capitalization(file_name):
    capitalization = 0

    with open(file_name, newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            #joins fields, splits, gathers words that start with an uppercase letter, counts
            join_text = " ".join(row)
            for word in join_text.split():
                if word[0].isupper():
                    capitalization += 1
    return capitalization


main()