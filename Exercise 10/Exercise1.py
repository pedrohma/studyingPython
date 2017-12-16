import random

a = random.sample(range(100), 30)
b = random.sample(range(100), 30)

c = [d for d in a if d in b]
print(c)