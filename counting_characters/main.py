#Devin Longtree [Counting Characters]

import random
grid = ['a','b','c','d']
randomgrid = random.choices(grid, weights = [1,1,1,1], k = random.randint(1, 21))

count_a = randomgrid.count("a")
count_b = randomgrid.count("b")
count_c = randomgrid.count("c")
count_d = randomgrid.count("d")

print(randomgrid)
print("A:",count_a, "B:",count_b, "C:",count_c, "D:",count_d)
