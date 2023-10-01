
def canBeIncreasing(numbers):
    previous = -1
    count = 0
    
    for i in range(len(numbers)):
        if numbers[i] <= previous:
            count += 1
            if count > 1:
                return False
            
            # Try swapping the previous number's digits
            prev_str = str(previous)
            for j in range(len(prev_str)):
                for k in range(j + 1, len(prev_str)):
                    # Swap the digits at positions j and k
                    prev_list = list(prev_str)
                    prev_list[j], prev_list[k] = prev_list[k], prev_list[j]
                    mod_prev_str = ''.join(prev_list)
                    
                    # Convert the modified previous string to an integer
                    mod_prev = int(mod_prev_str)
                    
                    if mod_prev < numbers[i]:
                        previous = mod_prev
                        numbers[i-1] = previous
                        if numbers[i-1] == numbers[i-2]:
                            return False
                        break
                    
        previous = numbers[i]
    
    return True

# Example usage:
nums = [13, 31, 30]
result = canBeIncreasing(nums)
print(result) 