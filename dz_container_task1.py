from itertools import permutations


input_sequence = "k98.ok"


letters = [char for char in input_sequence if char.isalpha()]


unique_words = set()


for r in range(1, len(letters) + 1):
    unique_words.update("".join(p) for p in permutations(letters, r))


sorted_words = sorted(unique_words, key=lambda word: (len(word), word))



print(len(sorted_words))
print("\n".join(sorted_words))
