When we mix loops with strings, we can do useful tasks like counting, searching, reversing, or formatting.

 Example 1: Print each character with its position
text = "Python"

for i in range(len(text)):
    print("Position", i, ":", text[i])


 Output:

Position 0 : P
Position 1 : y
Position 2 : t
Position 3 : h
Position 4 : o
Position 5 : n

 Example 2: Count vowels and consonants
text = "programming"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.lower() in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)


 Output:

Vowels: 3
Consonants: 8

 Example 3: Reverse a string using a loop
text = "Python"
reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text   # add character in front

print("Reversed:", reversed_text)


Output:

Reversed: nohtyP

Example 4: Remove spaces from a sentence
sentence = "I love Python programming"
result = ""

for ch in sentence:
    if ch != " ":
        result += ch

print("Without spaces:", result)


Output:

Without spaces: IlovePythonprogramming