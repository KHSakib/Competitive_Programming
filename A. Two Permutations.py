for tcas in range(int(input())):
    n,p,q = map(int, input().split())
    
    if n==p and n==q: 
        print("Yes")
        continue
    
    ans = n-2 >= (p+q) and "Yes" or "No"
    print(ans)
