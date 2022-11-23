
for tcas in range(int(input())):
    a = int(input())
    ans = []
    list1 = list(map(int, input().split()))

    if len(list1)==1:
        print("YES")
        continue
    a = False
    ans = "YES"
    for i in range(len(list1)-1):
        if a == True and list1[i+1] < list1[i]:
            ans = "NO"
            break
        if list1[i+1] > list1[i]:
            a = True
    print(ans)
