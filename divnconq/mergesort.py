def merge_sort(S):
    if len(S) < 2:
        return S
    
    mid = len(S) // 2
    left = S[:mid]
    right = S[mid:]
    
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    
    return merge(sorted_left, sorted_right)

def merge(L, R):
    res = [0] * (len(L) + len(R))  
    left, right = 0, 0
    index = 0  
    while left < len(L) and right < len(R):
        if L[left] < R[right]:
            res[index] = L[left]
            left += 1
        else:
            res[index] = R[right]
            right += 1
        index += 1
    
    while left < len(L):
        res[index] = L[left]
        left += 1
        index += 1
    while right < len(R):
        res[index] = R[right]
        right += 1
        index += 1
    
    return res

if __name__ == "__main__":
    arr = [4, 2, 7, 1, 9, 5, 3, 8, 6]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)

            