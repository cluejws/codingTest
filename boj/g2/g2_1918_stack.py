# 입력
import sys
input = sys.stdin.readline

alp_line = input().rstrip()

# 계산1: 계속적으로 res 만들기
res = ''
res_stack = []
for alp in alp_line:
    
    if alp == '(':
        res_stack.append(alp)
    
    elif alp == ')':
        
        # (1) '(' 만나기 전까지 res에 반영
        while res_stack[-1] != '(':            
            data = res_stack.pop()
            res = res + data
        
        # (2) '('를 제거
        data = res_stack.pop()
        
    elif alp in ['*','/']:  
        
        # (1) 이전( '*', '/' ) res에 반영
        while len(res_stack) != 0 and res_stack[-1] in ['*','/']:
            data = res_stack.pop()
            res = res + data
        
        # (2) 현재( '*', '/' ) 추가
        res_stack.append(alp)

    elif alp in ['+', '-']:
        
        # (1) '(' 만나기 전까지 res에 반영
        while len(res_stack) != 0 and res_stack[-1] != '(':
            data = res_stack.pop()
            res = res + data
        
        # (2) 현재( '+', '-' ) 추가
        res_stack.append(alp)
    
    else:
        
        # (1) res에 반영
        res = res + alp    
    
    #print(f'{alp} ->', res, res_stack)

# 계산2:
# -> (X) ')'로 끝날 경우 
# -> (O) '영어'로 끝날 경우
while len(res_stack) != 0:
    data = res_stack.pop()
    if data in ['+', '-' ,'*', '/']:
        res = res + data
        
#print('끝 ->', res, res_stack)

# 출력
print(res)