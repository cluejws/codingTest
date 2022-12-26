def recur(s,start,end, cnt):
    if(start >= end): return (1,cnt)
    elif (s[start] != s[end]): return (0,cnt)
    else: return recur(s,start+1,end-1, cnt+1)

def isPalindrome(s):
    check, cnt = recur(s, 0, len(s)-1, 1)
    return (check,cnt)

# 입력
tc = int(input())
for _ in range(tc):
    res = isPalindrome(input())
    print(res[0], res[1])