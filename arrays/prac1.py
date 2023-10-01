def solution3(queries):
    
    district = set()
    longest = 0
    out = []
    memo = {}
    
    for house in queries:
        l, r = 0, 0
        district.add(house)
        check = house - 1
        while check in district:
            l += 1
            check -= 1
        
        check = house + 1
        while check in district:
            r += 1
            check += 1
        
        longest = max(longest, l + r + 1)
        out.append(longest)
        
    return out

# def solution2(arr):
#     out = []
#     i = 1
#     while i < len(arr):
         
#     # for i in range(1,len(arr) - 1):
#         if arr[i] > arr[i-1] and i%2 == 1:
#             out.append(arr[i-1])
#             out.append(arr[i])
#         else:
#             out.append(arr[i])
#             out.append(arr[i-1])
#         i += 2
    
#     return

def solution1(arr):

    for i in range(0, len(arr) - 1, 2):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]    
    
    return arr



awds = [1, 5, 7, 3, 2, 1]
solution1(awds)
