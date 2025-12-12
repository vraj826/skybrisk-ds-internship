# ------------------------------------------
# CLIENT PROJECT – TEMPERATURE ANALYZER
# Week 1: Python Basics Only
# ------------------------------------------

print("Enter temperature readings (type -1 to stop):")

count = 0
total = 0
highest = -9999
lowest = 9999

while True:
    temp = float(input("Temperature: "))

    # Exit condition
    if temp == -1:
        break

    # Update total and count
    total += temp
    count += 1

    # Update highest and lowest
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

if count > 0:
    print("\n----- Temperature Report -----")
    print("Total Readings:", count)
    print("Average Temperature:", total / count)
    print("Highest Temperature:", highest)
    print("Lowest Temperature:", lowest)
else:
    print("No data entered.")
