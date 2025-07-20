def myKnapSackProblem(Ca, wt, val, n):
    K = [[0 for x in range(Ca + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(Ca + 1):

            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w - wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][Ca]

if __name__ == '__main__':

    profit_input = input("Enter profits separated by spaces (e.g., 10 15 40): ")
    profit = list(map(int, profit_input.strip().split()))

    weight_input = input("Enter weights separated by spaces (e.g., 1 2 3): ")
    weight = list(map(int, weight_input.strip().split()))

    Ca = int(input("Enter knapsack capacity (e.g., 6): "))

    n = len(profit)

    if n != len(weight):
        print("Error: Number of profits and weights must be the same.")

    else:
        result = myKnapSackProblem(Ca, weight, profit, n)
        print("Maximum profit possible:", result)
