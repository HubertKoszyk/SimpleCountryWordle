import random

file = open("words.txt", "r",encoding="utf-8")
data = []
for line in file:
  data.extend(line.strip().split(" "))
choseen_word = random.choice(data)
i = 1
chars = []
print("/////WITAJ W PROSTYM WORDLE/////")
print("ZGADNIJ PAŃSTWO KTÓRE MA", len(choseen_word), "LITER")
print("MASZ 6 PRÓB")
bad_chars = []
chars_in_word = []
for i in range(1, 6):
  input_type = input("ZGADNIJ SŁOWO ").capitalize()
  input_type_list = list(input_type)
  if len(input_type) > len(choseen_word) or len(input_type) < len(choseen_word):
    print("SŁOWO JEST ZA DŁUGIE LUB ZA KRÓTKIE")
    print("TO TWOJA", i, "PRÓBA")
    i = i + 1
    continue
  else:
    if input_type == choseen_word:
      print("BRAWO WYGRAŁEŚ")
      break
    else:
      print("NIESTETY NIE ZGADŁEŚ")
      same_chars = set(input_type) & set(choseen_word)
      chars.extend(same_chars)
      def sprawdzanie_tablic():
        for i in range(len(input_type_list)):
          if input_type_list[i] == choseen_word[i]:
            print("Litera", input_type_list[i], "jest w dobrym miejscu")
          elif input_type_list[i] in choseen_word:
            print("Litera", input_type_list[i], "jest w słowie")
          else:
            print("Litera", input_type_list[i], "nie pojawia się w słowie")
      sprawdzanie_tablic()
      print("TO TWOJA", i, "PRÓBA")
      print("TWOJE SŁOWO MA", len(choseen_word), "LITER")
      i = i + 1

print("KONIEC GRY. UKRYTE SŁOWO TO", choseen_word)
