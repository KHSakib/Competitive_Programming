for i in range(int(input())):
    a = int(input())
    ans = []
    list1 = list(map(int, input().split()))
    list2 = sorted(list1)

    for j in list1:
        if list2[a-1]!=j:
            ans.append(j-list2[a-1])
        else:
            ans.append(j-list2[a-2])
    print(*ans)
