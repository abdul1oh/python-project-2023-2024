
from random import randint

words = ["apple","banana","cherry","kivi"]
number = randint(0,len(words)-1)
word = words[number]
found_letters = ["_"] * len(word)
hards = 8
print(f"Word contain {len(word)} letter! Try to find it")

while hards > 0:
     print("".join(found_letters))
     player = input("Write one letter! ")

     if player in word:
          for i in range(len(word)):
               if word[i] == player:
                    found_letters[i] = player
     else:
          hards -= 1
          print(f"Letter is not in the word! Try again, Hards = {hards}")

     if "_"  not in found_letters:
          print(f"Congurulation!!! You found the word >> {word}")
          break
else:
     print(f"Unfortunately You lostt in this game! WORD == {word}")








