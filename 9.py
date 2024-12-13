# Open and read the text file
with open("textfile.txt", "r") as text_file:
    word_list = text_file.read().split()

# Dictionary to keep track of word frequencies
word_frequencies = {}

# Count the occurrences of each word
for term in word_list:
    term = term.lower()
    word_frequencies[term] = word_frequencies.get(term, 0) + 1

# Sort words by frequency in descending order and get the top 5
most_frequent_words = sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)[:5]

# Display the result
print(most_frequent_words)
