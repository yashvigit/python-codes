import random

nums = random.sample(range(-15, 16), 10)
squares = [x**2 for x in nums]

print("Random numbers:", nums)
print("Squares:", squares)
