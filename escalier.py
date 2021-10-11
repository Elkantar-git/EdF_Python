import sys

nbr = int(sys.argv[1])
list = []

for i in range(1, nbr + 1):
    list.append(" " * (nbr - i) + ("#" * i))
print('\n'.join(list))