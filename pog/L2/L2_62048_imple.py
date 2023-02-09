def getGCD(w,h):
    
    while h != 0:
        r = w % h
        
        w,h = h,r
    
    return w

def solution(w,h):
    
    # 계산1: 최대공약수(유클리드 호제법)
    gcd = getGCD(w,h)
    
    # 계산2: (전체 사각형) - (대각선 위 사각형)
    cnt = (w * h) - (w+h - gcd)
    return cnt