import os
import igraph
from igraph import Graph

print("hi")
print("lol")

def collatz(num):
    list = []
    ## add current number to list and set num to next number in seq
    while num > 1:
        list.append(num)
        num = collatz_helper(num)
    ## loop breaks when num = 1 --> add 1 to list here
    list.append(1)
    print(*list, sep = ", ")

## returns next number in sequence
def collatz_helper(num):
    if (num % 2 == 0):
        return int(num / 2)
    else:
        return 3 * num + 1

if __name__ == '__main__':
    collatz(13)