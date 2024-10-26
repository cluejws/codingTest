def getCount(h, m, s):
    """
     - 초침: 60초에 360도
     - 분침: 60분에 360도
     - 시침: 12시간에 360도
    """
    # 계산1: 각도 구하기
    h_degree = ((h*360/12) + (m*360/12/60) + (s*360/12/60/60)) % 360
    m_degree = ((m*360/60) + (s*360/60/60)) % 360
    s_degree = (s*360/60) % 360
    
    """
     - 1분에 (초침,분침), (초침,시침) 2번 만남
      → 예외1: 1시간마다 제외(-1) = (초침,분침) 59분→00분 
      → 예외2: 12시 제외(-2)     = (초침,분침,시침) 11시59분→12시00분
    """
    # 계산2: 개수 초기화
    cnt = 0
    if (s_degree >= m_degree):
        cnt += 1
    if (s_degree >= h_degree):
        cnt += 1
    
    # 계산3: 개수 구하기
    # 1분에 2번
    # 예외1: 1시간 마다 제외
    # 예외2: 12시 제외
    cnt += (h*60+m) * 2
    cnt -= h
    if (h >= 12): cnt -= 2
    
    return cnt

def solution(h1, m1, s1, h2, m2, s2):
    # 계산1: 개수 구하기
    # 00:00:00 ~ h1:m1:s1 
    # 00:00:00 ~ h2:m2:s2
    cnt1 = getCount(h1, m1, s1)
    cnt2 = getCount(h2, m2, s2)
    
    # 계산2: 예외처리 
    # h1이 00:00:00 또는 12:00:00 경우, +1 
    cnt = cnt2 - cnt1
    if (h1 == 0 or h1 == 12) and (m1 == 0) and (s1 == 0):
        cnt += 1
    
    return cnt