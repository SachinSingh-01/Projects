'''Mini Text Analyzer Tool (Moderate)
What to build
Count words
Count characters
Find unique words
Check palindrome words
Concepts used
String operations
List and set for words
Loop for analysis
Functions for each task
if-else for conditions'''
def count_words(words):
    return len(words)

def count_characters(sentence):
    return len(sentence)

def find_unique_words(words):
    return set(words)

def find_palindrome_words(words):
    palindromes = []
    for word in words:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes
sentence = input("Enter the word/sentence: ")
words = sentence.split()
word_count = count_words(words)
char_count = count_characters(sentence)
unique_words = find_unique_words(words)
palindrome_words = find_palindrome_words(words)
print("\n--- Text Analysis Result ---")
print("Total Words:", word_count)
print("Total Characters:", char_count)
print("Unique Words:", unique_words)
print("Palindrome Words:", palindrome_words)
