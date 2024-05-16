def func(Arr, x):
    length = len(Arr)
    if length == 0:
        return False
    mid = length // 2 
    if Arr[mid] == x:
        return True
    elif Arr[mid] > x:
        return func(Arr[:mid], x)  
    else:
        return func(Arr[mid + 1:], x)  
    
if __name__ == "__main__":
    Arr = [4, 6, 7, 23, 56, 78, 232, 346, 567, 578, 678, 894, 902, 1023]
    x = int(input("Enter a number: "))
    res = func(Arr, x)
    print(res)
