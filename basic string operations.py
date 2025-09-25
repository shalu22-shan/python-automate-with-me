Common String Operations
1. Creating a string
s1 = "Hello"
s2 = 'Python'
print(s1, s2)

2. Concatenation (Joining)
a = "Hello"
b = "World"
c = a + " " + b
print(c)   # Output: Hello World

3. Repetition
word = "Hi "
print(word * 3)   # Output: Hi Hi Hi

4. Indexing (Access characters by position)
text = "Python"
print(text[0])   # P  (first character)
print(text[-1])  # n  (last character)

5. Slicing (Get part of string)
text = "Programming"
print(text[0:6])   # Progra
print(text[3:])    # gramming
print(text[:5])    # Progr

6. Length of string
text = "Python"
print(len(text))   # 6

7. Changing case
s = "Hello World"
print(s.upper())   # HELLO WORLD
print(s.lower())   # hello world
print(s.title())   # Hello World

8. Searching
text = "I love Python"
print("love" in text)   # True
print("java" in text)   # False

9. Replacing
s = "I like Java"
s = s.replace("Java", "Python")
print(s)   # I like Python

10. Splitting and Joining
s = "apple,banana,cherry"
fruits = s.split(",")   # ['apple', 'banana', 'cherry']
print(fruits)

words = ["I", "love", "Python"]
sentence = " ".join(words)
print(sentence)   # I love Python