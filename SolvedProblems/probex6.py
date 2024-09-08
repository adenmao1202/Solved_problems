import sys

""" Input Format:

The first line contains the input words separated by the commas, which are used for building a dictionary.

The rest of the lines are the search words after the dictionary is built.

(NOTE: All words are lowercase.)

Output Format:

Print out the result including the starting alphabet letter (i.e. A to Z) and the order of the searched word in the letter category, which is separated by " " (whitespace character) at each line according to the corresponding input word.

(NOTE: If the query word is not found in the dictionary, try to use print "NOT FOUND".)
"""
import sys


def build_dic(building_dic):
    organized_dic = {}

    all_words = sorted(building_dic.split(","))  # 照字母順序排序

    for word in all_words:
        first_letter = word[0].upper()  # 大寫字首

        if first_letter not in organized_dic:
            organized_dic[first_letter] = []  # 創建新的字首在 organized_dic 中

        organized_dic[first_letter].append(word)

    return organized_dic


def find_word(organized_dic, finding_word):
    if len(finding_word) == 0:
        return "NOT FOUND"
    else:
        first_letter = finding_word[0].upper()  # 確認字首

        if (
            first_letter in organized_dic
            and finding_word in organized_dic[first_letter]
        ):
            position = organized_dic[first_letter].index(finding_word)
            return f"{first_letter} {position + 1}"
        else:
            return "NOT FOUND"


def main():
    input_data = sys.stdin.read().strip().split("\n")  # Read all input lines

    if len(input_data) == 0:
        return

    # The first line is the dictionary words
    dictionary_words = input_data[0]
    organized_dic = build_dic(dictionary_words)

    # The rest are the query words
    query_words = input_data[1:]

    for word in query_words:
        print(find_word(organized_dic, word))


if __name__ == "__main__":
    main()
