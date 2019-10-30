'''
Johnny To
CIS 41A Fall 2019
In-Class Assignment 5
'''
#Part One – Using a main function, Docstrings
#Write a function called hello. The function has no arguments and no return value. It simply prints the text "Hello World". Include a docstring that describes the function.
def hello():
    """Prints 'Hello World!' """
    print('Hello World!')

#Write a main function, as described by the Python main function reading.
def main():
    #From main, call hello and then print hello’s docstring.
    hello()
    print(hello.__doc__ )

#Call main, as described by the Python main function reading.
main()

'''
Execution Results
Hello World!
'''
