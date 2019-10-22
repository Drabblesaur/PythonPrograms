'''
Johnny To
CIS 41A Fall 2019
In-Class Assignment 2
'''
# String Methods
name = input("name?")
print(name.upper())
print(len(name))
print(name[3])
name2 = name.replace("o","x")
print(name2)
print(name)

# Counting and Finding

quote = "Believe you can and you're halfway there."
print(quote.count("a"))
quote = "Believe you can and you're halfway there."

print([i for i, val in enumerate(quote) if val == "a"])

'''
Results:
name?George Washington
GEORGE WASHINGTON
17
r
Gexrge Washingtxn
George Washington
4
[13, 16, 28, 32]

'''
