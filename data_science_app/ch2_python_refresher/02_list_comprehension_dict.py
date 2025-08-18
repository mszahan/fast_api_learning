from random import seed, randint

seed(10) # set random seed to make examples reproducible

random_dictionary = {i: randint(1, 10) for i in range(5)}
print(random_dictionary)