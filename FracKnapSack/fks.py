class Item:
    def __init__(self, profit, weight):
        self.profit = float(profit)
        self.weight = float(weight)

def fractionalKnapsack(W, arr):
    res = 0.0
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    for item in arr:
        if item.weight <= W:
            W -= item.weight
            res += item.profit
        else:
            res += item.profit * W / item.weight
            break
    return res

if __name__ == "__main__":
    arr = []
    WeightTotal = float(input("Enter the maximum weight that can be held: "))
    addingItems = True
    while addingItems:
        ItemProfit = float(input("Provide the profit of the item altogether: "))
        ItemWeight = float(input("Enter the weight of the item altogether: "))
        arr.append(Item(ItemProfit, ItemWeight))
        response = input("Would you like to add another item? Type 'q' to exit item adding: ").strip().lower()
        if response == 'q':
            addingItems = False
    max_val = fractionalKnapsack(WeightTotal, arr)
    print("The maximum value in the knapsack is:", max_val)

        
        
        
    
    