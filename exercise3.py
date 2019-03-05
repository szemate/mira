"""
Write a program that reads numbers from the user until the user enters an empty line,
then it prints all the numbers already entered, one by line.
"""

nums = []
while True:
    n = input("Enter a number: ")
    if n == '':
        break
    nums.append(int(n))

print()
print("The numbers are:")
i = 0
while i < len(nums):
    print(nums[i])
    i = i + 1
