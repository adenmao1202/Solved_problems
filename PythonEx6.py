import sys


def build_and_search_dictionary(dictionary_words, search_queries):
    organized_dict = {}
    word_count = {}

    # Sort the words before processing them to build the dictionary
    words = sorted(dictionary_words.split(","))
    for word in words:
        first_letter = word[0].upper()
        if first_letter not in organized_dict:
            organized_dict[first_letter] = {}
            word_count[first_letter] = 0

        word_count[first_letter] += 1
        organized_dict[first_letter][word] = word_count[first_letter]

    results = []
    for query in search_queries:
        if query == "":  # Handling empty queries
            results.append("NOT FOUND")
            continue
        first_letter = query[0].upper()
        if first_letter in organized_dict and query in organized_dict[first_letter]:
            results.append(f"{first_letter} {organized_dict[first_letter][query]}")
        else:
            results.append("NOT FOUND")
    return results


def main():
    input_lines = sys.stdin.read()
    splitted = input_lines.strip().split(
        "\n"
    )  # Use strip to remove any trailing newline characters
    dictionary_words = splitted[0]
    search_queries = splitted[1:]

    results = build_and_search_dictionary(dictionary_words, search_queries)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
