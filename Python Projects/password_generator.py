letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits = ['0','1','2','3','4','5','6','7','8','9']
char = ['!','@','#','$','%','&']
print("Welcome to password Generator!")
n_l = int(input("Enter no.of letters you want in your password:"))
n_d = int(input("Enter no.of digits you want in your password:"))
n_c = int(input("Enter no.of special characters you want in your password:"))
password = ""
import random
for i in range(1,n_l+1):
    password += random.choice(letter)
for i in range(1,n_d+1):
    password += random.choice(digits)
for i in range(1, n_c+1):
    password += random.choice(char)
password = list(password)
random.shuffle(password)
p = ''.join(password)
print(p)