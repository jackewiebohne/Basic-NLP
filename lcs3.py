# python3


# dynamic programming to find longest common (in order) subsequence of three strings. created as part of the Algorithms course offered by HSE/UC Davis on Coursera
# note that time complexity is O(n^3); so not feasible for very long strings

import numpy as np

def lcs3(first_sequence, second_sequence, third_sequence):
    first_sequence = str(first_sequence)
    second_sequence = str(second_sequence)
    third_sequence = str(third_sequence)
    mtx = np.zeros((len(first_sequence)+1, len(second_sequence)+1, len(third_sequence) + 1))

    for i in range(1,len(first_sequence)+1):
        for j in range(1,len(second_sequence)+1):
            for k in range(1, len(third_sequence)+1):
                if first_sequence[i-1] == second_sequence[j-1] == third_sequence[k-1]:
                    mtx[i,j,k] = mtx[i-1,j-1, k-1] + 1 # if the characters are a match we take the result from the previous diagonal element plus 1
                else:
                    mtx[i,j,k] = max(mtx[i-1,j,k], mtx[i,j-1,k], mtx[i,j,k-1],
                                   mtx[i-1, j-1, k], mtx[i-1, j, k-1], mtx[i, j-1, k-1],
                                   mtx[i-1,j-1,k-1]) # if the characters don't match we just take the max of the surrounding elements and carry that over in this cell of the matrix
    # print(mtx)
    return int(mtx[-1,-1,-1])

# import random
# diff = []
# for i in range(200):
#     r1 = random.randint(0,5000)
#     r2 = random.randint(0,5000)
#     r3 = random.randint(0,5000)
#     res1 = lcs3(r1, r2, r3)
#     res2 = _lcs3(r1, r2, r3)
#     if res1 != res2:
#         diff.append((res1, res2, r1, r2, r3))
# print(len(diff))
# print(diff)

if __name__ == '__main__':
    n = int(input())
    a = str(input().replace(' ', ''))
    # assert len(a) == n

    m = int(input())
    b = str(input().replace(' ', ''))
    # assert len(b) == m

    q = int(input())
    c = str(input().replace(' ', ''))
    # assert len(c) == q

    print(lcs3(a, b, c))
