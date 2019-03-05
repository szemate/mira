"""
Write a program that reads numbers from the user until the user enters an empty line,
then it prints all the numbers already entered and their sum.
"""

nums = []
while True:
    n = input("Enter a number: ")
    if n == '':
        break
    nums.append(int(n))

i = 0
s = 0
result = ""
while i < len(nums):
    s = s + nums[i]
    result = result + str(nums[i])
    if i < len(nums) - 1:
        result = result + " + "
    i = i + 1

result += " = " + str(s)
print(result)
