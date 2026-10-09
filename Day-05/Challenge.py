# Day 05 - Python Strings Challenge
# 30 Days Python Challenge for Data Analytics

# Challenge 1: Create a sentence using name and city

name = input("Enter your name: ")
city = input("Enter your city: ")

print("My name is " + name + " and I live in " + city)


# Challenge 2: Count characters in a sentence

sentence = input("Enter a sentence: ")

print("Total Characters:", len(sentence))


# Challenge 3: Convert name to uppercase and lowercase

name = input("Enter your name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())


# Challenge 4: Clean extra spaces

city = input("Enter your city with extra spaces: ")

clean_city = city.strip()

print("Clean City:", clean_city)


# Challenge 5: Replace a word

sentence = input("Enter a sentence: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

updated_sentence = sentence.replace(old_word, new_word)

print("Updated Sentence:", updated_sentence)


# Challenge 6: Extract first and last characters

word = input("Enter a word: ")

print("First Character:", word[0])
print("Last Character:", word[-1])


# Challenge 7: Extract first three characters

word = input("Enter a word: ")

print("First 3 Characters:", word[:3])


# Challenge 8: Find a character

sentence = input("Enter a sentence: ")
character = input("Enter a character to find: ")

print("Position:", sentence.find(character))


# Challenge 9: Product information

product = input("Enter product name: ")
price = input("Enter product price: ")

print("Product:", product)
print("Price:", price)


# Challenge 10: Simple Data Cleaning

customer_name = input("Enter customer name: ")

clean_name = customer_name.strip().title()

print("Clean Customer Name:", clean_name)