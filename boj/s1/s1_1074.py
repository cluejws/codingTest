n,r,c = map(int,input().split())

res = 0
while n !=0 :
    
    n -= 1
    
    # 0영역
    if r < 2 ** n and c < 2 ** n:
        res += (2 ** n) * (2 ** n) * 0
    
    
    # 1영역
    elif r < 2 ** n and c >= 2 ** n:
        res += (2 ** n) * (2 ** n) * 1
        
        c -= (2 ** n)
    
    # 2영역
    elif r >= 2 ** n and c < 2 ** n:
        res += (2 ** n) * (2 ** n) * 2
        
        r -= (2 ** n)
    
    # 3영역
    else:   
        res += (2 ** n) * (2** n) * 3
        
        r -= (2 ** n)
        c -= (2 ** n) 
    
print(res)