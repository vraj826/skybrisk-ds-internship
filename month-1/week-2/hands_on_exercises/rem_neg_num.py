# Remove negative numbers using list comprehension
numbers = [10, -4, 7, -1, 22, 0]
positive_nums = [x for x in numbers if x >= 0]
print("Positive Numbers:", positive_nums)
