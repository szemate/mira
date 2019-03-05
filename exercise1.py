"""
Write a program that reads numbers from the user until the user enters an empty line,
then it prints the sum of the numbers already entered.
"""

s = 0
while True:
    n = input("Enter a number: ")
    if n == '':
        break
    s += int(n)
print("The sum of the numbers is", s)
