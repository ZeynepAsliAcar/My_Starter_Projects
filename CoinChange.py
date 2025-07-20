def count(coinset, n, sum):
    table = [[0 for x in range(n)] for x in range(sum+1)]
  
    for i in range(n):
        table[0][i] = 1

    for i in range(1, sum+1):
        for j in range(n):
            x = table[i - coinset[j]][j] if i - coinset[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0

            table[i][j] = x + y

    return table[sum][n-1]

if __name__ == '__main__':
    coin_input = input("Enter coin denominations separated by spaces (e.g., 1 2 3): ")
    coinset = list(map(int, coin_input.strip().split()))
    
    sum = int(input("Enter the total sum to make: "))
    
    n = len(coinset)
    
    print("Number of ways to make the sum:", count(coinset, n, sum))
