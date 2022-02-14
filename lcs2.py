# python3

# dynamic programming to find longest common (in order) subsequence of two strings. created as part of the Algorithms course offered by HSE/UC Davis on Coursera
# time complexity is O(n^2)

import numpy as np

def lcs2(first_sequence, second_sequence):
    first_sequence = str(first_sequence)
    second_sequence = str(second_sequence)
    mtx = np.zeros((len(first_sequence)+1, len(second_sequence)+1))
    for i in range(1,len(first_sequence)+1):
        for j in range(1,len(second_sequence)+1):
            # print(i,j)
            if first_sequence[i-1] == second_sequence[j-1]:
                # it has to be i-1 and j-1 because the matrix is padded with zeros, i.e.
                # if the strings are 'abc' and 'abb' then the corresponding matrix looks like this
                #   0 a b c
                # 0 0 0 0 0
                # a 0 x x x
                # b 0 x x x
                # b 0 x x x
                # (we are using a different algo and matrix than in the videos, which make it unecessarily complicated)
                # where the xs are to be filled in by the algorithm. so the prepended zeros for the matrix
                # need to be considered in the string. since i and j are indices over the matrix and we haven't
                # added a zero (or other placeholder) in front of the string, we need to reflect this when
                # we look for matches in the two strings. in short mtx[i,j] is equal to string1[i-1] and string2[j-1]

                mtx[i,j] = mtx[i-1,j-1] + 1 # if the characters are a match we take the result from the previous diagonal element plus 1
            else:
                mtx[i,j] = max(mtx[i-1,j], mtx[i,j-1], mtx[i-1,j-1]) # if the characters don't match we just take the max of the surrounding elements and carry that over in this cell of the matrix
    # print(mtx)
    return int(mtx[-1,-1])


# fs1 = 'editing'
# fs2 = 'distance'
# fs1 = 'short'
# fs2 = 'ports'
# fs1 = 275
# fs2 = 25
# fs1 = 1
# fs2 = 10
# fs1 = 2783
# fs2 = 5287
# fs1 = 123
# fs2 = 321
# fs1  = 1
# fs2 = 10

# print(_lcs2(fs1, fs2))

# import random
# for i in range(100):
#     r1 = random.randint(0,5000)
#     r2 = random.randint(0,5000)
#     res1 = lcs2(r1, r2)


if __name__ == '__main__':
    n = int(input())
    a = str(input().replace(' ', ''))#list(map(int, input().split()))
    # assert len(a) == n

    m = int(input())
    b = str(input().replace(' ', ''))#str(input().split(' '))#list(map(int, input().split()))
    # assert len(b) == m

    print(lcs2(a, b))
