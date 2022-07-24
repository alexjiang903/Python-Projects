#Password Generator Project
import random
import json
from json.decoder import JSONDecodeError
from os import stat

def gen_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= 20
    nr_symbols = 10
    nr_numbers = 10

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

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

    x = list(unshuffled_pwd)
    random.shuffle(x)

    shuffled_pwd = ''.join(x)

    return shuffled_pwd

name = input("Input customer name (first last): ")
database_data = {}
with open("database.json", "r") as f:
    try:
        database_data = json.load(f)
    except JSONDecodeError:
        database_data = {}
    database_data[name] = gen_pw()

with open("database.json", "w") as f:
    json.dump(database_data, f)
print("Customer added successfully")


