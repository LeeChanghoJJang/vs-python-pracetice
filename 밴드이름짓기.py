import os
import random
color = open('color.txt',encoding='UTF-8').read().split()
food = open('food.txt',encoding='UTF-8').read().split()
print(random.choice(color)+' '+random.choice(food))