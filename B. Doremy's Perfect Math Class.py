import math 
for tcas in range(int(input())):
    n = int(input())
    list1 = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans = math.gcd(ans, list1[i])
    print(list1[n-1]//ans)
