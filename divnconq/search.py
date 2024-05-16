def func(Arr, x, i):
    if i >= len(Arr): 
        return False
    if Arr[i] > x:
        return False
    elif Arr[i] == x:
        return True
    else:
        i += 1
        return func(Arr, x, i)  

if __name__ == "__main__":
    Arr = [4, 6, 7, 23, 56, 78, 232, 346, 567, 578, 678, 894, 902, 1023]
    i = 0
    x = input("Enter a number: ")
    x = int(x)
    res = func(Arr, x, i)
    print(res)
