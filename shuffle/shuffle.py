import random


def shuffle(arr):

    for leng in range(len(arr), 1, -1):
        nth = random.randrange(0, leng)
        arr[nth], arr[leng-1] = arr[leng-1], arr[nth]
