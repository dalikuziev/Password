import random as r

letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("PyPassword Generatorga xush kelibsiz!\nParolingiz haqida ma'lumot bering")

password = ""
text = []
nr_letters = int(input("Harflar soni: "))
nr_numbers = int(input(f"Raqamlar soni: "))
nr_symbols = int(input(f"Belgilar soni: "))

for n in range(nr_letters):
  text.append(r.choice(letters))
for n in range(nr_numbers):
  text.append(r.choice(numbers))
for n in range(nr_symbols):
  text.append(r.choice(symbols))

r.shuffle(text)

for n in text:
  password += n

print(f"Sizning parolingiz tayyor - {password}")
