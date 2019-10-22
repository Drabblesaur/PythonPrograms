'''
Johnny To
CIS 41A   Fall 2019
Unit B take-home assignment
'''

# SCRIPT 2
'''
Use three named "constants" for the following:
small beads with a price of 9.20 dollars per box
medium beads with a price of 8.52 dollars per box
large beads with a price of 7.98 dollars per box
'''
SMALL_BEADS_PRICE = 9.20
MED_BEADS_PRICE = 8.52
LARGE_BEADS_PRICE = 7.98

# Ask the user how many boxes of small beads, how many boxes of medium beads, and how many large beads they need
# (use the int Built-in Function to convert these values to int).
smallBeads = int(input("How many Small Beads? :"))
medBeads = int(input("How many Medium Beads? :"))
largeBeads = int(input("How many Large Beads? :"))
# Calculation
smallTotal = round((smallBeads*SMALL_BEADS_PRICE),2)
medTotal = round((medBeads*MED_BEADS_PRICE),2)
largeTotal = round((largeBeads*LARGE_BEADS_PRICE),2)
finalTotal = round((smallTotal + medTotal + largeTotal),2)
# Print the invoice
print("SIZE      QTY    COST PER BOX      TOTALS")
print(f"Small     {str(smallBeads).rjust(3)}           {str(SMALL_BEADS_PRICE).rjust(5)}      {str(smallTotal).rjust(6)}")
print(f"Medium    {str(medBeads).rjust(3)}           {str(MED_BEADS_PRICE).rjust(5)}      {str(medTotal).rjust(6)}")
print(f"Large     {str(largeBeads).rjust(3)}           {str(LARGE_BEADS_PRICE).rjust(5)}      {str(largeTotal).rjust(6)}")
print(f"TOTAL                          {str(finalTotal).rjust(10)}")

'''
Execution Results:
TEST 1

How many Small Beads? :10
How many Medium Beads? :9
How many Large Beads? :8
SIZE      QTY    COST PER BOX      TOTALS
Small      10             9.2        92.0
Medium      9            8.52       76.68
Large       8            7.98       63.84
TOTAL                              232.52

TEST 2
How many Small Beads? :5
How many Medium Beads? :10
How many Large Beads? :15
SIZE      QTY    COST PER BOX      TOTALS
Small       5             9.2        46.0
Medium     10            8.52        85.2
Large      15            7.98       119.7
TOTAL                               250.9


'''