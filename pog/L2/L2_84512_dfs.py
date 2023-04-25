def getId(word, list_word):
    
    for i in range(len(list_word)):
        if word == list_word[i]:
            return i
    
    return -1

def solution(word):
    
    # dfs
    def getResult(word):
        
        # 1. 기저조건
        if len(word) >= 5:
            return

        # 2. dfs
        for i in range(5):
            new_word = word + alp[i]
            list_word.append(new_word)
            getResult(new_word)
    
    # 계산1: dfs
    alp = ['A','E','I','O','U']
    list_word = []
    getResult('')
    
    # 계산2: 순서 찾기
    id = getId(word, list_word)
    return id + 1