from string import ascii_lowercase, ascii_uppercase
import random


random.seed(1)
chars = ascii_lowercase + ascii_uppercase
a = 0
b = len(chars) - 1


def mail_address(n):
    word = ''
    for j in range(n):
        indx = random.randint(a, b)
        word = word + chars[indx]
    address = word + '@mail.ru'
    yield address


N = int(input())

for i in range(5):
    x = mail_address(N)
    print(*x)
