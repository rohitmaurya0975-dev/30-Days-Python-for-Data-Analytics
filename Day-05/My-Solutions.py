# Day 05 - My Solutions
# Topic: Python Strings

# Q01
name = "Rohit"
print(name)

# Q02
first_name = "Rohit"
last_name = "Maurya"
print(first_name + " " + last_name)

# Q03
course = "Data Analytics"
print(len(course))

# Q04
language = "Python"
print(language[0])
print(language[2])
print(language[-1])

# Q05
city = "Varanasi"
print(city[-1])
print(city[-2])

# Q06
language = "Python"
print(language[0:3])
print(language[3:6])
print(language[:])

# Q07
name = "rohit"
print(name.upper())
print(name.lower())

# Q08
city = "   Delhi   "
print(city.strip())

# Q09
city = "Mumbai"
print(city.replace("Mumbai", "Delhi"))

# Q10
name = "Rohit"
print(name.find("h"))

# Bonus
product = "Laptop"
price = 50000
quantity = 2

print(
    "I bought " + product +
    " at a price of " + str(price) +
    " for " + str(quantity) + " units."
)