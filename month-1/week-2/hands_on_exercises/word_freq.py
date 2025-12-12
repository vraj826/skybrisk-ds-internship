# Dictionary word frequency counter
text = "apple banana apple mango banana apple"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print("Word Frequency:", freq)
