import random


def make_phrase():
  try:
    with open("phrases.txt", "r") as fd:
      phrases = fd.read().splitlines()
    phrase = random.choice(phrases).upper()
  except FileNotFoundError:
    print("Couldn't find phrases.txt, make sure you have it in the same folder as this file.")
    return "When you gaze long into the abyss, the abyss gazes also into you".upper()
  except IndexError:
    print("phrases.txt seems to be empty. Add some phrases to it, one per line.")
  return phrase


def print_gallows(misses):
  # +---+
  # |   |
  # |  \O/
  # |   |
  # |  / \
  # |
  # |_____
  hd,bd,ll,rl,la,ra = tuple("O|/\\\\/"[:misses] + (6*" ")[misses:])
  print(f"+---+\n|   |\n|  {la}{hd}{ra}\n|   {bd}\n|  {ll} {rl}\n|\n|_____")
  print(f"Incorrect guesses made: {misses}/6")

def print_revealed_phrase(phrase, letters_guessed):
  revealed_phrase = ""
  for char in phrase:
      if char.isalpha() == False or char in letters_guessed:
          revealed_phrase += char
      else:
          revealed_phrase += "_"
  print(revealed_phrase)

def get_letter(letters_guessed):
  letter = input("Please enter a letter: ").upper()
  while letter.isalpha() == False or len(letter)>1 or letter in letters_guessed:
      if letter.isalpha() == False or len(letter) > 1:
          print(f'''"{letter}" is not a letter!''')
          letter = input("Please enter a letter: ")
      elif letter in letters_guessed:
          print(f'''"{letter}" has already been guessed!''')
          letter = input("Please enter a letter: ")


  return letter.upper()

def won (phrase, guessed):
  for letter in phrase:
    if letter.isalpha() and letter not in guessed:
      return False
  
  return True

def play_game():
  misses = 0
  phrase = make_phrase()
  #phrase = "HELLO, WORLD"
  guesses = []

  win = False

  print(f"*** Welcome to Hangman ***\n")
  print_gallows(misses)

  while (misses < 6):
    print_revealed_phrase(phrase,guesses)

    if (won(phrase, guesses)):
      win = True
      break

    print(f"Letters guessed: {sorted(guesses)}")

    letter = get_letter(guesses)

    if letter not in phrase:
      misses += 1
      print_gallows(misses)

    guesses.append(letter)

  if (win):
    print("Congratulations!")

  else:
    print("Game Over!")
    print("Solution was: " + phrase)

#play_game()

#"V", "A", "h", "(", "N", "s", "P", "I", "R", "O", "C", "D", "w", "T", "pY", "U", "F", and "e"