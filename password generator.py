import string
import random

s_letter = string.ascii_lowercase
b_letter = string.ascii_uppercase
digits = string.digits
symbol = string.punctuation

all_characters = s_letter + b_letter + digits + symbol  

# ask the user for the desired length of the password
length = int(input("Enter the length of the password: "))


password = ''.join(random.choices(all_characters, k=length))

# display the generated password to the user
print("Your password is:", password)

print("Thanks For Using Our System!")




#Created By AAKHS BATCH - 3#
#=======Jakia , Marzana , Shimu , Fahmida , Farzin , Amena , Sumaiya , Ananna=====# 