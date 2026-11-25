import random

def shuffle_list(items):
    # Copy the list first so the original list isn't mutated in place
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled

print(shuffle_list([1, 2, 3, 4, 5]))

def unique_random_numbers():
    return random.sample(range(10), k=7)

print(unique_random_numbers())