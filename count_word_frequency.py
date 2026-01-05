def count_word_freuency(words):
  word_count = {}
  for word in words:
    word_count[word]=word_count.get(word,0)+1
  return word_count


words = ["ADHITHYA", "IS", "ADHITHYA", "DATA", "SCIENCE"]
print(count_word_freuency(words))

print(count_word_freuency("ADHITHYA"))

