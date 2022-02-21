the_lest = []
n = int(input())
x = list(map(int, input().split()))

for J in range(1, n):
    key = x[J]
    i = J - 1
    while (i >= 0 and x[i] > key):
         x[i + 1] = x[i]
         i = i - 1
         x[i + 1] = key
the_lest="["+",".join(str(i) for i in x)+"]"
print(the_lest)
