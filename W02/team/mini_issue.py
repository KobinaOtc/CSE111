import random

def main():
    quantity = 2  # or any other number based on your requirement
    present = False
    past = True
    future = False
    sentence = make_sentence(quantity, present, past, future)
    print(sentence)

def get_determiner(quantity):
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word

def get_noun(quantity):
    if quantity == 1:
        noun = ['girl', 'boy', 'woman', 'man', 'book', 'cat', 'dog', 'car', 'bag', 'bottle']
    else:
        noun = ['girls', 'boys', 'women', 'men', 'books', 'cats', 'dogs', 'cars', 'bags', 'bottles']
    noun = random.choice(noun)
    return noun


def get_verb(quantity, present, past, future):
    if present and quantity == 1:
        present = ['runs', 'flys', 'walks', 'throws', 'catchs', 'hides', 'seeks', 'writes', 'reads', 'edits', 'jogs', 'cooks', 'bakes', 'draws', 'paints']
        word = random.choice(present)
    elif past == past:
        past = ['ran', 'flew', 'walked', 'throwed', 'catched', 'hid', 'seeked', 'wrote', 'read', 'edited', 'jogged', 'cooked', 'baked', 'drew', 'painted']
        word = random.choice(past)
    elif future == future:
        future = ['will run', 'will fly', 'will walk', 'will throw', 'will catch', 'will hide', 'will seek', 'will write', 'will read', 'will edit', 'will jog', 'will cook', 'will bake', 'will draw', 'will paint']
        word = random.choice(future)
    elif present and quantity != 1:
        present = ['run', 'fly', 'walk', 'throw', 'catch', 'hide', 'seek', 'write', 'read', 'edit', 'jog', 'cook', 'bake', 'draw', 'paint']
        word = random.choice(present)

    verb = word
    return verb


def make_sentence(quantity, present, past, future):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, present, past, future)
    sentence = f"{determiner} {noun} {verb}"
    return sentence

main()
