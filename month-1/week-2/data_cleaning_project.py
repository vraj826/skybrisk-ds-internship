# -------------------------------------------------
# CLIENT PROJECT – BASIC DATA CLEANING SYSTEM
# Week 2: Data Structures & Functions Only
# -------------------------------------------------

def remove_none(data):
    """Remove None values using list comprehension."""
    return [x for x in data if x is not None]


def remove_duplicates(data):
    """Remove duplicate elements using a set."""
    return list(set(data))


def filter_values(data, limit):
    """Keep only values less than or equal to limit."""
    return [x for x in data if isinstance(x, (int, float)) and x <= limit]


# Sample raw data
raw_data = [10, None, 50, 200, None, 30, 10, 5, 60, 50]

print("Original Data:", raw_data)

# Cleaning steps
step1 = remove_none(raw_data)
print("After Removing None:", step1)

step2 = remove_duplicates(step1)
print("After Removing Duplicates:", step2)

cleaned_data = filter_values(step2, 50)
print("Final Cleaned Data (<= 50):", cleaned_data)
