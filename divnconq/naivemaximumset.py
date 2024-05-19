class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def MaximumSetBuilder(S):
    res = []
    for p in S:
        if isMax(S, p):
            res.append(p)
    return res
        
def isMax(S, p):
    for q in S:
        if q != p and (q.x > p.x and q.y > p.y):
            return False
    return True 
              
if __name__ == "__main__":
    S = [Point(3, 4), Point(3, 5), Point(2, 4), Point(8, 3), Point(1, 3), Point(3, 7), Point(4, 7), Point(1, 2), Point(5, 3)]
    MaxSet = MaximumSetBuilder(S)
    for point in MaxSet:
        print(f"({point.x}, {point.y})")


