def getResult(n):
    print_arr = ['1', '2', '4']
    
    # 계산
    res = ''
    while n > 0:
        
        # 계산1: n -= 1로 출력 배열에 맞게 n 변화
        n -= 1
        
        # 계산2: n % 3(나머지)로 출력 배열을 통해 res 생성
        res = print_arr[n % 3] + res
        
        # 계산3: n //= 3로 n 변화
        n = n // 3
    
    return res

def solution(n):
    
    res = getResult(n)
    return res