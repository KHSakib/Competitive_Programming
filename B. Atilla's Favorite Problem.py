for i in range(int(input())):
    a = int(input())
    s = input()

    c = s[0]
    for j in s:
        if c<j: c = j
    print(ord(c)-96)
