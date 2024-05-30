import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
symbols = "[]{}()*/.,-"


all = lower + upper + numbers + symbols


length = 6


password = "".join(random.choices(all, k=length))


print(password)
