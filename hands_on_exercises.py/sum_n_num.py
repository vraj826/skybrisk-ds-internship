# Sum of First N Natural Numbers
limit = int(input("\nEnter a limit N: "))
total = 0
i = 1

while i <= limit:
    total += i
    i += 1

print("Sum of first", limit, "numbers is:", total)
