import random

def main():
    numbers = [16.2, 75.1, 52.3]
    words = ['join', 'love', 'smile', 'love', 'cloud', 'head']

    print(numbers)
    append_random_numbers(numbers_list=numbers)
    print(numbers)
    append_random_numbers(numbers_list=numbers, quantity=3)
    print(numbers)
    append_random_words(words)
    print(words)
    append_random_words(words, 5)
    print(words)


def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        number = random.uniform(0, 100)
        number = round(number, 1)
        numbers_list.append(number)

def append_random_words(words_list, quantity=1):
    random_words = [
        "apple", "breeze", "candle", "dragon", "echo", 
        "flame", "galaxy", "horizon", "island", "jigsaw", 
        "kangaroo", "lighthouse", "mystic", "nebula", "oasis", 
        "paradox", "quasar", "ripple", "serene", "twilight", 
        "umbrella", "velocity", "whisper", "xylophone", "yonder", "zephyr"
    ]
    for i in range(quantity):
        # word = random.choice(random_words)
        # words_list.append(word)
        word_index = int(round(random.uniform(0, len(random_words)), 0))
        words_list.append(random_words[word_index])

if "__main__" == __name__:
    main()