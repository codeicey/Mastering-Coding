from collections import namedtuple

N = int(input())
str1 = input().split()
sum1 = 0
for x in range(N):
    table = namedtuple('table',str1)
    f1,f2,f3,f4 =input().split()
    table = table(f1, f2, f3, f4 )
    sum1 = sum1 + int(table.MARKS)
print(sum1/N)

