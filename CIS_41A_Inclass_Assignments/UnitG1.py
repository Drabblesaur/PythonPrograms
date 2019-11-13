with open('ZenofPython.txt', 'w') as f:
    data = 'Beautiful is better than ugly.\nExplicit is better than implicit.\n'
    f.write(data)
    f.close()

with open('ZenofPython.txt', 'a') as j:
    data2 = "Readability counts.\nIf the implementation is hard to explain, it's a bad idea."
    j.write(data2)
    j.close()

with open('ZenofPython.txt', 'r') as k:
    print(k.read())

'''
Execution:
Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
If the implementation is hard to explain, it's a bad idea.
'''