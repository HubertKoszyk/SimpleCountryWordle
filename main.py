import random

file = open("words.txt", "r",encoding="utf-8")
data = []
for line in file:
  data.extend(line.strip().split(" "))
choseen_word = random.choice(data)
i = 1
chars = []
print("/////WELCOME IN SIMPLE COUNTRY WORDLE/////")
print("Guess the word with", len(choseen_word), "letters")
print("You have 6 tries")
bad_chars = []
chars_in_word = []
for i in range(1, 6):
  input_type = input("Guess Word:").capitalize()
  input_type_list = list(input_type)
  if len(input_type) > len(choseen_word) or len(input_type) < len(choseen_word):
    print("Word is too long or to short")
    print("This is your", i, "try")
    i = i + 1
    continue
  else:
    if input_type == choseen_word:
      print("Excelent You Win")
      break
    else:
      print("Unfortunately, you didn't guess.")
      same_chars = set(input_type) & set(choseen_word)
      chars.extend(same_chars)
      def sprawdzanie_tablic():
        for i in range(len(input_type_list)):
          if input_type_list[i] == choseen_word[i]:
            print("Letter", input_type_list[i], "is in right place")
          elif input_type_list[i] in choseen_word:
            print("Letter", input_type_list[i], "is in word")
          else:
            print("Letter", input_type_list[i], "The letter does not appear in the word")
      sprawdzanie_tablic()
      print("This your", i, "try")
      print("This word has", len(choseen_word), "letters")
      i = i + 1

print("End of the game! Hidden Word is:", choseen_word)
