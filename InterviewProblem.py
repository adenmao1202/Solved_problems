def most_frequent_word(text):
    # Step 1: Check if the input is a string or an array of characters
    if isinstance(text, str):
        words = text.split()  # Convert string to list of words
    elif isinstance(text, list):
        words = text  # If already a list, use it directly
    else:
        return "Invalid input: text must be either a string or an array of characters."

    # Step 2: Initialize a dictionary to store word frequencies
    word_freq = {}

    # Step 3: Iterate through each word in the list
    for x in words:
        # Step 4: Check if the word contains any of the characters in 'appier'
        if any(char in "appier" for char in x):
            # Step 5: Update the word frequency
            word_freq[word] = word_freq.get(x, 0) + 1

    # Step 6: Check if any word was found
    if not word_freq:
        return "No word found containing any of the characters in 'appier'."

    # Step 7: Find the word with the maximum frequency
    max_freq_word = max(word_freq, key=word_freq.get)

    return max_freq_word


# Example usage:
text = "apple banana happier happier happier"
result = most_frequent_word(text)
print("Most frequent word:", result)
