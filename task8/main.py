def backpack(values, weights, capacity):
    val_n_weig=list(zip(values,weights))
    val_n_weig = sorted(val_n_weig, key=lambda x: x[0], reverse=True)
    income = 0
    print(val_n_weig)
    for i in val_n_weig:
        if i[1] <= capacity:
            income += i[0]
            capacity -= i[1]

    return income


if __name__ == "__main__":

    N = int(input("Input a number of laptops what a student can buy: "))
    C = int(input("Input a student start capital: "))
    gains = list(map(int, input("Input array of laptop gains separete with space: ").split(" ")))
    prices = list(map(int, input("Input array of laptop prices separete with space: ").split(" ")))

    if len(gains) != len(prices):
        print("Lent of gains, prices and N must be the same")
    else:
        capital = backpack(gains, prices, C)
        print("Capital on the end of summer:", capital)

    input("Exit")

