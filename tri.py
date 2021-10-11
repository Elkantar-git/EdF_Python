import sys

print(' '.join(map(str, sorted(map(int, sys.argv[1:]), reverse=True))))