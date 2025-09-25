Strings are sequences of characters, so you can use loops (for or while) to go through each character.

 Example 1: Using for loop
word = "Python"

for ch in word:
    print(ch)


 Output:

P
y
t
h
o
n

 Example 2: Count vowels in a string
text = "programming"
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count = count + 1

print("Number of vowels:", count)


 Output:

Number of vowels: 3

Example 3: Using while loop with index
text = "Hello"
i = 0

while i < len(text):
    print(text[i])
    i = i + 1


Output:

H
e
l
l
o
