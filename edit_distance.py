# python3

# edit distance using dynamic programming (was created in context of Algorithms course offered by HSE/UC Davis on Coursera

import  numpy as np

def edit_distance(first_string, second_string):
    # good explanation:
    # https://www.youtube.com/watch?v=We3YDTzNXEk&ab_channel=TusharRoy-CodingMadeSimple
    mtx = np.zeros((len(first_string)+1, len(second_string)+1))
    mtx[:,0] = [i for i in range(len(first_string)+1)]
    mtx[0,:] = [j for j in range(len(second_string)+1)]
    for i in range(1,len(first_string)+1):# has to be len(string)+1 b/c we're otherwise stopping short of last row/column
        for j in range(1,len(second_string)+1):
            insertion = mtx[i,j-1] + 1
            deletion = mtx[i-1,j] + 1
            match = mtx[i-1,j-1]
            mismatch = mtx[i-1,j-1] + 1
            if first_string[i-1] == second_string[j-1]:
                # it has to be i-1 and j-1 because the matrix is padded with zeros, i.e.
                # if the strings are 'abc' and 'abb' then the corresponding matrix looks like this
                #   0 a b c
                # 0 0 1 2 3
                # a 1 x x x
                # b 2 x x x
                # b 3 x x x
                # where the xs are to be filled in by the algorithm. so the prepended zeros for the matrix
                # need to be considered in the string. since i and j are indices over the matrix and we haven't
                # added a zero (or other placeholder) in front of the string, we need to reflect this when
                # we look for matches in the two strings. in short mtx[i,j] is equal to string1[i-1] and string2[j-1]
                mtx[i,j] = min(insertion, deletion, match)
            else:
                mtx[i,j] = min(insertion, deletion, mismatch)
    # print(mtx)
    return int(mtx[-1,-1])

# str1 = 'ports'
# str2 = 'short'
# str1 = 'editing'
# str2 = 'distance'
# print(edit_distance(str1, str2))

if __name__ == "__main__":
    print(edit_distance(input(), input()))
