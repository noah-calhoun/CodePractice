

def solution(a, k):
    memo = {}
    count = 0
    for value in a:
        rem = value % k
        if rem in memo:
            memo[rem] += 1
        else:
            memo[rem] = 1
    
    for value in a:
        rem = value % k
        b = (k - rem) % k
        
        if rem == b:
            count += memo.get(rem,0) -1
        else:
            count += memo.get(b, 0)
    
    return count // 2
        


a=[1, 2, 3, 4, 5]
k= 3
solution(a,k)