import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwd_letters = ''
for x in range(0,nr_letters):
  char = random.choice(letters)
  pwd_letters += char


pwd_symbols = ''

for x in range(0,nr_symbols):
  symb = random.choice(symbols)
  pwd_symbols += symb


pwd_nums = ''
for x in range(0,nr_numbers):
  nums = random.choice(numbers)
  pwd_nums += nums

unshuffled_pwd = pwd_letters + pwd_symbols + pwd_nums
print(f'Your password is: {unshuffled_pwd}')        

x = list(unshuffled_pwd)
random.shuffle(x)

shuffled_pwd = ''.join(x)
print(f'An even stronger randomized password would be: {shuffled_pwd}')   #HARD LEVEL FINAL SOLUTION

password = []

for x in range(1,nr_letters+1):
  password.append(random.choice(letters))

for x in range(1,nr_symbols+1):
  password.append(random.choice(symbols))

for x in range(1,nr_numbers+1):
  password.append(random.choice(numbers))


random.shuffle(password)

shuffled_pwd = ''
for x in password:  
  shuffled_pwd += x 

print(f'Another strong password would be: {shuffled_pwd}')




