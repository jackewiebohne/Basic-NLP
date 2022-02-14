def keygram_vec(wordlist, keyword, window_size=5, equalise=False, return_type=None):
    '''
    vectorised n-gram function for a keyword.
    inputs:
        wordlist = ordered list of (pre-processed) tokens
        keyword (string) = keyword to get n-gram for
        window_size (int) = takes window_size many tokens on either side of keyword
        equalise (boolean) = if e.g. set to False function will only return as much as or less than window_size many tokens
                            to the right and left of the keyword. if set to True, function will always return (window_sizw*2 + keyword)
                            many tokens (if keyword_index-window_size is shorter than document, the difference will be added to the right;
                            and vice versa if keyword_index+window_size is longer than document). In short, the keygrams returned will
                            all be of equal length, regardless of keywords' index positions in the document
        return_type (str) = possible inputs: 'str': list['str'], 'list': list[list], default: list[numpy.array]
    '''
    assert(type(wordlist)==list)
    arr = np.array(wordlist)
    L = len(arr)
    indexes = np.where(arr==keyword)[0] # returns tuple(array, array_dtype), but we only want the arrays, hence the [0] slice
    
    if indexes.shape[0]==0: # if nothing is found return empty list
        return []

    left = indexes[0] - window_size # to check if we can grab window_size many words to left of first keygram, if negative, we can't
    right = indexes[-1] + window_size # to check if we can grab window_size many words to right of last keygram, if right > L, we can't
    
    keygram_list = []
    
    # first find of keyword
    if left >= 0:
        keygram_list.append(arr[indexes[0]-window_size:indexes[0]+window_size+1])
    else:
        if not equalise:
            try:
                keygram_list.append(np.hstack((arr[:indexes[0]], arr[indexes[0]:indexes[0]+window_size+1])))
            except:
                # exception needed, in case arr[:indexes[0]] is empty (i.e. keyword is at very beginning of doc)
                keygram_list.append(arr[indexes[0]:indexes[0]+window_size+1])
        else:
            try:
                keygram_list.append(np.hstack((arr[:indexes[0]], arr[indexes[0]:indexes[0]+window_size+abs(left)+1])))
            except:
                keygram_list.append(arr[indexes[0]:indexes[0]+window_size+abs(left)+1])
                
    # any find of keyword other than first and last
    for i in range(1, len(indexes)-1):
        keygram_list.append(arr[indexes[i]-window_size:indexes[i]+window_size+1])
    
    #last find of keyword
    if indexes[0] != indexes[-1]: # make sure first and last keyword are not the same
        if right > L:
            if not equalise:
                try:
                    keygram_list.append(np.hstack((arr[indexes[-1]-window_size-1:indexes[-1]], arr[indexes[-1]:])))
                except:
                    keygram_list.append(arr[indexes[-1]-window_size-1:indexes[-1]])
            else:
                try:
                    keygram_list.append(np.hstack((arr[indexes[-1]-window_size-(right-L)-1:indexes[-1]], arr[indexes[-1]:])))
                except:
                    keygram_list.append(arr[indexes[-1]-window_size-(right-L)-1:indexes[-1]])
        else:
            keygram_list.append(arr[indexes[-1]-window_size-1:indexes[-1]+window_size])

    if not return_type:
        return keygram_list
    elif return_type == 'list':
        keygram_list = [ele.tolist() for ele in keygram_list]
        return keygram_list
    elif return_type == 'str':
        keygram_list = [' '.join(ele) for ele in keygram_list]
        return keygram_list
    else:
        raise ValueError('Only "str" (returns list of str), "list" (list of lists), or "None" (list of np.arrays) allowed')