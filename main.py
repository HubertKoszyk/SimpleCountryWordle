import random

file = open("slowa.txt", "r")
data = []
for line in file:
  data.extend(line.strip().split(" "))
choseen_word = random.choice(data)
i = 1
chars = []
print("/////WITAJ W PAŃSTWA WORDLE/////")
print("Zgadnij słowo składające się z", len(choseen_word), "liter")
print("Litery odgadnięte są w losowej kolejności")
bad_chars = []
chars_in_word = []
for i in range(1, 10):
  input_type = input("Zgadnij słowo:").capitalize()
  input_type_list = list(input_type)
  if len(input_type) > len(choseen_word) or len(input_type) < len(
      choseen_word):
    print("Słowo jest za długie lub za krótkie")
    print("To twoja", i, "próba")
    i = i + 1
    continue
  else:
    if input_type == choseen_word:
      print("Brawo, zgadłeś!")
      break
    else:
      print("Niestety, nie zgadłeś.")
      same_chars = set(input_type) & set(choseen_word)
      chars.extend(same_chars)
      def sprawdzanie_tablic():
        for i in range(len(input_type_list)):
          if input_type_list[i] == choseen_word[i]:
            print("Literka", input_type_list[i], "jest na swoim miejscu")
          elif input_type_list[i] in choseen_word:
            print("Literka", input_type_list[i], "jest w słowie")
          else:
            print("Literka", input_type_list[i], "nie występuje w słowie")
      print("Wspólne znaki to", chars)
      sprawdzanie_tablic()
      print("To twoja", i, "próba")
      print("To słowo ma", len(choseen_word), "liter")
      i = i + 1

print("Koniec gry ułożone słowo to:", choseen_word)



