given_string = input().lower()

words_needed = ["sun", "fish", "water", "sand"]

words_count = sum(given_string.count(word) for word in words_needed)

print(words_count)
