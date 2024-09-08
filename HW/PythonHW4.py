import json
import string
from typing import List, Tuple, Union


def analyze_text(text: Union[List[str], str], target_word: str) -> Tuple[int, int]:
    total_words = 0
    word_count = 0

    def process_word(word: str) -> str:
        word = word.strip(string.punctuation)

        if word.endswith("es"):
            word = word[:-1]
        return word

    def count_occurrences(word_list: List[str], target: str) -> int:
        return sum(1 for word in word_list if process_word(word) == target)

    def recursive_analysis(text: Union[List[str], str]) -> Tuple[int, int]:
        local_total_words = 0
        local_word_count = 0

        if isinstance(text, str):
            words = text.split()
            local_total_words += len(words)
            local_word_count += count_occurrences(words, target_word)
        elif isinstance(text, list):
            for item in text:
                if isinstance(item, str):
                    words = item.split()
                    local_total_words += len(words)
                    local_word_count += count_occurrences(words, target_word)
                elif isinstance(item, list):
                    nested_total_words, nested_word_count = recursive_analysis(item)
                    local_total_words += nested_total_words
                    local_word_count += nested_word_count

        return local_total_words, local_word_count

    total_words, word_count = recursive_analysis(text)

    return total_words, word_count


if __name__ == "__main__":

    json_input = input()
    input_data = json.loads(json_input)

    nested_text = input_data.get("input", [])

    target_word = input()

    total_words, word_count = analyze_text(nested_text, target_word)

    print(f"Total Words: {total_words}, '{target_word}' Occurrences: {word_count}")
