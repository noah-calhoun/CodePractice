
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, 
# where 0 means empty and 1 means not empty, and an integer n, r
# eturn true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


def canPlaceFlowers( flowerbed, n):
    empty = 0 if flowerbed[0] else 1

    for f in flowerbed:
        if f:
            n -= int((empty - 1) / 2)  # int division, round toward zero
            empty = 0
        else:
            empty += 1

    n -= (empty) // 2
    return n <= 0

def canPlaceFlowers1( flowerbed, n):

    for i in range(len(flowerbed)):

        if n==0:
            return True
        
        if ((i == 0 or flowerbed[i - 1] == 0)
            and (flowerbed[i] == 0) 
            and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):
            
            n -= 1
            flowerbed[i] = 1

    return not bool(n)





if __name__ == '__main__':
    flowerbed = [1,0,0,0,1]
    flowerbed = [1,0,0,0,1,0,0]
    n = 2
    print(canPlaceFlowers1(flowerbed, n))